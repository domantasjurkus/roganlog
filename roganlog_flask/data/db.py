import os
import pickle
import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

def init_db():
    db = get_db()

    db_dir = os.path.dirname(__file__)
    schema_dir = os.path.join(db_dir, 'schema.sql')

    with current_app.open_resource(schema_dir) as f:
        db.executescript(f.read().decode('utf8'))
    
    click.echo('Initialized the database.')
    return db

def insert(db, p):
    query = "INSERT INTO podcast (spotify_id, title, body) VALUES (?, ?, ?);"
    args = (p[0], p[1], p[2])
    db.execute(query, args)
    db.commit()

def import_parsed_data(db):
    print('Importing pickled podcast data...')
    podcasts_pickle_dir = os.path.join(os.path.dirname(__file__), 'scrapped', 'podcasts.pickle')

    file = open(podcasts_pickle_dir, 'rb')
    podcasts = pickle.load(file)
    file.close()

    for i in range(len(podcasts)-1, -1, -1):
        result = insert(db, podcasts[i])
    
    print('Podcasts imported')

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

def get_podcasts(db):
    query = "SELECT * FROM podcast ORDER BY id DESC"
    results = db.execute(query).fetchall()

    return results

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    db = init_db()
    import_parsed_data(db)
