import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql + psycopg2://tracy:wangari775@localhost/blog'

db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True)