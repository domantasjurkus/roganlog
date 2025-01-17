import os

from flask import Flask, redirect

from data import db
import auth
import blog
import podcasts

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'roganlog.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app

app = create_app()

db.init_app(app)

app.register_blueprint(podcasts.bp)
app.register_blueprint(auth.bp)
app.register_blueprint(blog.bp)

# app.add_url_rule('/', endpoint='index')
# app.add_url_rule('/podcasts', endpoint='podcasts')

@app.route('/')
def index():
    return redirect('/podcasts')

if __name__ == '__main__':
    app.run()