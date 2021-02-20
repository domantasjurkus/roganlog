from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
# from roganlog_flask.auth import login_required
# from roganlog_flask.data.db import get_db, get_podcasts
from auth import login_required
from data.db import get_db, get_podcasts

bp = Blueprint('podcasts', __name__)

@bp.route('/podcasts')
def podcasts():
    db = get_db()
    podcasts = get_podcasts(db)

    return render_template('index.html', entries=podcasts)