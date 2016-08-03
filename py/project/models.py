import datetime
import os
from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask, request, render_template, jsonify
app = Flask(__name__)
app.debug = True

db = SQLAlchemy(app)
basedir = os.path.abspath(os.path.dirname(__file__))
DATABASE = 'flaskr.db'
DEBUG = True
SECRET_KEY = 'secretkey'





DATABASE_PATH = os.path.join(basedir, DATABASE)
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
db = SQLAlchemy(app)

class Question(db.Model):
	__tablename__='questions'
	id = db.Column('question_id', db.Integer(), primary_key=True)
	subject = db.Column('subject', db.String(), unique=False)
	body = db.Column('body', db.String(), unique=False)

	def __init__(self, subject, body):
		self.subject = subject
		self.body = body

class Answer(db.Model):
	___tablename__='answers'
	id = db.Column('answer_id', db.Integer(), primary_key=True)
	question_id = db.Column(db.Integer(), unique=False)
	body = db.Column('body', db.String(), unique=False)

	def __init__(self, question_id, body):
		self.question_id = question_id
		self.body = body
	