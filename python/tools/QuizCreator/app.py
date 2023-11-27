
from flask import Flask, render_template, request, redirect
from views.quiz import quiz_bp
from views.creator import creator_bp
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(creator_bp)
app.register_blueprint(quiz_bp)

@app.route('/')
def index():
    return redirect('/creator')

if __name__ == '__main__':
    app.run()
