from flask import render_template, request, Blueprint
from flaskblog.models import Post
from flask_login import  login_required
from flaskblog import Db
from firebase_admin import auth,storage

main = Blueprint('main', __name__)


@main.route('/')
def null():
    return render_template('null.html',title='null')
   
@main.route("/home")
def home():
    # page = request.args.get('page', 1, type=int)
    # posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=4)
    return render_template('home1.html')


@main.route("/about")
@login_required
def about():
    return render_template('about.html', title='About')