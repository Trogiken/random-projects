from flask import Blueprint, render_template, request, redirect

quiz_bp = Blueprint('quiz', __name__, template_folder='templates/quiz', static_folder='static/quiz', static_url_path='/static/quiz', url_prefix='/quiz')

@quiz_bp.route('/', methods=['GET', 'POST'])
def quiz():
    return render_template('quiz/quiz.html')
