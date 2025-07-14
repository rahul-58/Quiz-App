from flask import Blueprint, render_template
from app.models import Quiz, UserAnswer, db, Question, QuizResult
from flask_login import login_required, current_user

bp = Blueprint('main', __name__)

# Public landing page
@bp.route('/')
def landing():
    return render_template('landing.html')

# call index.html
@bp.route('/quizzes')
@login_required
def index():
    quizzes = Quiz.query.all()
    return render_template('index.html', quizzes=quizzes)

# call dashboard.html
@bp.route('/dashboard')
@login_required
def dashboard():
    quizzes = Quiz.query.filter_by(user_id=current_user.id).all()

    recent_scores = QuizResult.query.filter_by(user_id=current_user.id).order_by(QuizResult.timestamp.desc()).limit(5).all()
    
    return render_template('dashboard.html', quizzes=quizzes, recent_scores=recent_scores)