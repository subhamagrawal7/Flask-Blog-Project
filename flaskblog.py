from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
# To prevent from various attacks
app.config['SECRET_KEY'] = '967d1767432f72c86aab457ed23dcf7d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


# Create user model (or user table)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False,
                           default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    # One-to-many relationship between users and posts. The lazy attribute defines when the SQL Alchemy loads the data from the database as necessary in one go
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    # In above Post capital as class being referenced. Here we are referencing the users table and column
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"User('{self.title}','{self.date_posted}')"


posts = [
    {
        'author': 'Subham Agrawal',
        'title': 'Blog Post 1',
        'content': 'First Post content',
        'date_posted': 'March 11,2020'
    },
    {
        'author': 'Ravi Bhadoria',
        'title': 'Blog Post 2',
        'content': 'Second Post content',
        'date_posted': 'March 12,2020'
    }
]

# decorator creates an association between the URL given as an argument and the function
@app.route("/")
@app.route("/home")
def home():
    # The first posts is the variable to be used in some other file and second posts is the dummy data defined above
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessfull. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)
