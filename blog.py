from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT fname, lname, email'
        ' FROM user'
    ).fetchall()
    return render_template('blog/index.html', posts=posts)
	# maybe have to change the .fetchall() thing? maybe no