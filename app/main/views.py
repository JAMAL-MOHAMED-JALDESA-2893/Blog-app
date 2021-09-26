from flask import render_template, request, redirect, url_for, abort, flash
from . import main
from flask_login import login_required, current_user
from ..models import User, Post, Comment
from .forms import UpdateProfile, PostForm, CommentForm
from .. import db, photos
from ..request import get_quotes


@main.route('/')
def index():
    quote = get_quotes()
    return render_template('index.html', quote = quote)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user)

