from flask import Flask, render_template, url_for
app = Flask(__name__)

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


if __name__ == "__main__":
    app.run(debug=True)
