from flask import render_template, request, redirect, url_for, abort, flash
from ..requests  import  get_quote
from . import main


@main.route('/')
def index():
    quote = get_quote()
    return render_template('index.html', quote = quote)