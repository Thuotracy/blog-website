from flask import render_template,url_for,Blueprint,request,redirect,flash,session
from datetime import datetime
from .models import Blogpost, User
from app import db
from .forms import RegistrationForm
from werkzeug.security import generate_password_hash,check_password_hash 

views = Blueprint('views',__name__)

@views.route('/')
def index():
    posts = Blogpost.query.order_by(Blogpost.date_posted.desc()).all()
    
    return render_template('index.html', posts=posts)

@views.route("/register")
def register():
    Registration= RegistrationForm()

    return render_template('register.html', Registration=RegistrationForm)

@views.route('/success', methods=['GET','POST'])
def success():
    if request.method == "POST":
        username = request.form.get('username')
        email = request.form.get('email')
        password1 = request.form.get('psw1')
        password2 = request.form.get('psw2')
        user_info =db.session.query(User).filter(User.email ==email)
        email_exist=User.query.filter_by(email =email).first()
        username_exist = User.query.filter_by(username =username).first()
        if email_exist:
            flash('User with that email address already exist', category='error')
            return render_template('form.html', text ='User with that email address already exist')
        elif username_exist:
            flash('User name already in use', category='error')
            return render_template('form.html', text ='User name already in use.')
        elif password1 != password2 :
            flash( 'Password dont\'t match' , category='error')
            return render_template('form.html', text ='Password don\'t match!')
        elif len(password1) < 6:
            flash('Password is too short', category='error')
            return render_template('form.html', text ='password too short. use at least 6 characters')
        else:
            data = User(username,email,password=generate_password_hash(password1, method='sha256'))
            db.session.add(data)
            db.session.commit()
            # logout_user(data)
            
            return render_template('success.html')

@views.route('/login' )
def login():
    return render_template('login.html')

    
@views.route('/profile', methods=['GET','POST'])
def profile():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('psw')
        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            text='Please check your login details and try again.'
            return render_template('login.html', text=text)
        session['email']=user.email
        name = user.username
        # login_user(user, remember= True)
        return render_template('profile.html',user=user)

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
