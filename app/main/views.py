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
