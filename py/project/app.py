import flask
from flask import Flask
from flask import  request, jsonify, render_template, flash, session, redirect, url_for



from httplib import HTTPException
from operator import attrgetter
from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask, request, render_template, jsonify
import os
app = Flask(__name__)
app.debug = True

db = SQLAlchemy(app)
basedir = os.path.abspath(os.path.dirname(__file__))
DATABASE = 'flaskr.db'
DEBUG = True
SECRET_KEY = 'Thisissomethingwhichissecret'





DATABASE_PATH = os.path.join(basedir, DATABASE)
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
db = SQLAlchemy(app)

class Question(db.Model):
	
	id = db.Column( db.Integer(), primary_key=True)
	subject = db.Column('subject', db.String(), unique=False)
	body = db.Column('body', db.String(), unique=False)

	def __init__(self, subject, body):
		self.subject = subject
		self.body = body

class Answer(db.Model):

	id = db.Column(db.Integer(), primary_key=True)
	question_id = db.Column('question_id', db.Integer(), unique=False)
	body = db.Column('body', db.String(), unique=False)


	def __init__(self, question_id, body):
		self.question_id = question_id
		self.body = body



@app.route('/')
def index():
	questions = Question.query.all()
	for question in questions:
		answers = Answer.query.filter_by(question_id=question.id).all()
	
	return render_template('index.html', questions=questions)

@app.route('/question/<int:question_id>')
def question(question_id):
	question = Question.query.get(question_id)
	db.session.commit()
	answers = Answer.query.filter_by(question_id=question_id).all()
	return render_template('question.html', question=question, answers=answers)


@app.route('/ask', methods=['GET', 'POST'])
def ask():
	if request.method == 'POST':
		subject = request.form['subject']
		body = request.form['body']
		question = Question(subject, body)
		db.session.add(question)
		db.session.commit()
		flash('Question added')
		return redirect(url_for('index'))
	return render_template('ask.html')
	

@app.route('/answer/<int:question_id>', methods=['POST'])
def answer(question_id):
	question = Question.query.get(question_id)
		
	body = request.form['body']
	answer = Answer(question.id,body)
	db.session.add(answer)
	db.session.commit()
	return redirect(url_for('question', question_id=question_id))

if __name__ == '__main__':
	app.secret_key='thiisasecret'
	db.create_all()
	app.run(debug=True)
