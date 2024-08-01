from flask import Flask, render_template, request, redirect, url_for, session
import random
import os
#from dbase import Question
from dbase import Question, create_db
from db import db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'
db.init_app(app)


@app.route('/')
def home():
    all_questions = Question.query.all()
    questions = random.sample(all_questions, min(len(all_questions), 5))
    session['questions'] = [q.id for q in questions]
    high_score = session.get('high_score', 0)
    return render_template('home.html', questions=questions, high_score=high_score)

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        score = 0
        answers = {}
        question_ids = session.get('questions', [])
        for question_id in question_ids:
            question = Question.query.get(question_id)
            user_answer = request.form.get(str(question.id))
            answers[question.id] = {'question': question.to_dict(), 'user_answer': user_answer}
            if user_answer == question.answer:
                score += 20
        session['score'] = score
        session['answers'] = answers  
        #print("Answers saved in session:", answers)  # Debug print
        high_score = session.get('high_score', 0)
        if score > high_score:
            session['high_score'] = score
        
        return redirect(url_for('result'))

@app.route('/result')
def result():
    score = session.get('score', 0)
    answers = session.get('answers', {})
    high_score = session.get('high_score', 0)
    return render_template('result.html', score=score, answers=answers, high_score=high_score)


if __name__ == '__main__':
    with app.app_context():
        create_db()
    app.run(debug=True)
