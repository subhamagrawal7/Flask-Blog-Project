from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# To prevent from various attacks
app.config['SECRET_KEY'] = '967d1767432f72c86aab457ed23dcf7d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskblog import routes