from flask import render_template,url_for,Blueprint,request,redirect
from datetime import datetime
from .models import Blogpost
from app import db

views = Blueprint('views',__name__)

@views.route('/')
def index():
    posts = Blogpost.query.order_by(Blogpost.date_posted.desc()).all()
    
    return render_template('index.html', posts=posts)

@views.route('/about')
def about():
    return render_template('about.html')

@views.route('/post/<int:post_id>')
def post(post_id):
    post = Blogpost.query.filter_by(id=post_id).one()

    return render_template('post.html', post=post)

@views.route('/add')
def add():
    return render_template('add.html')

@views.route('/addpost', methods=['POST','GET'])
def addpost():
        if request.method == 'POST':
            title = request.form.get('title')
            subtitle = request.form.get('subtitle')
            author = request.form.get('author')
            content = request.form.get('content')

            post = Blogpost(title=title,   subtitle=subtitle, author=author, content=content, date_posted=datetime.now())

            db.session.add(post)
            db.session.commit()

            return redirect(url_for('views.index'))

        return render_template('add.html')
