from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

# To prevent from various attacks
app.config['SECRET_KEY'] = '967d1767432f72c86aab457ed23dcf7d'

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


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)
