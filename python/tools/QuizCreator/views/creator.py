from flask import Blueprint, render_template, request, redirect

creator_bp = Blueprint('creator', __name__, template_folder='templates/creator', static_folder='static/creator', static_url_path='/static/creator', url_prefix='/creator')

@creator_bp.route('/', methods=['GET', 'POST'])
def quiz():
    return render_template('creator/creator.html')
