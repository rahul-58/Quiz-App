from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify
from flask_login import login_required, current_user
from ..models import Quiz, Question, db, UserAnswer, QuizResult
from app.forms import QuizForm, QuestionForm

bp = Blueprint('quiz', __name__)


# Allows the user to create a new quiz
@bp.route('/create_quiz', methods=['GET', 'POST'])
@login_required
def create_quiz():
    form = QuizForm()
    if form.validate_on_submit():
        new_quiz = Quiz(title=form.title.data, user_id=current_user.id)
        db.session.add(new_quiz)
        db.session.commit()
        flash("Quiz created successfully!", "success")
        return redirect(url_for('quiz.manage_quiz', quiz_id=new_quiz.id))
    return render_template('create_quiz.html', form=form)


# Allows the user to manage quizzes and add questions 
@bp.route('/manage_quiz/<int:quiz_id>', methods=['GET', 'POST'])
@login_required
def manage_quiz(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    
    # Check if the user owns the quiz
    if quiz.user_id != current_user.id:
        flash('You can only manage your own quizzes.', 'danger')
        return redirect(url_for('main.index'))
    
    form = QuestionForm()
    if form.validate_on_submit():
        options_list = [opt.strip() for opt in form.options.data.split(',')]
        new_question = Question(
            text=form.question.data,
            options=','.join(options_list),
            correct_answer=form.correct_answer.data,
            quiz_id=quiz.id,
        )
        db.session.add(new_question)
        db.session.commit()
        flash("Question added successfully!", "success")
        return redirect(url_for('quiz.manage_quiz', quiz_id=quiz.id))
    
    return render_template('manage_quiz.html', quiz=quiz, form=form)



# Allows the user to update questions 
@bp.route('/edit_question/<int:question_id>', methods=['GET', 'POST'])
@login_required
def edit_question(question_id):
    question = Question.query.get_or_404(question_id)
    if request.method == 'POST':
        question.text = request.form['question']
        question.options = request.form['options']
        question.correct_answer = request.form['correct_answer']
        db.session.commit()
        return redirect(url_for('quiz.manage_quiz', quiz_id=question.quiz_id))
    return render_template('edit_question.html', question=question)


# Allows the user to delete questions 
@bp.route('/remove_question/<int:question_id>', methods=['POST'])
@login_required
def remove_question(question_id):
    question = Question.query.get_or_404(question_id)
    quiz_id = question.quiz_id
    db.session.delete(question)
    db.session.commit()
    return redirect(url_for('quiz.manage_quiz', quiz_id=quiz_id))


# Allows the user to take quiz
@bp.route('/take_quiz/<int:quiz_id>', methods=['GET', 'POST'])
@login_required
def take_quiz(quiz_id):
    quiz = Quiz.query.get_or_404(quiz_id)
    
    if request.method == 'POST':
        score = 0
        for question in quiz.questions:
            user_answer = request.form.get(f'question_{question.id}')
            if user_answer == question.correct_answer:
                score += 1
        
        total_questions = len(quiz.questions)

        quiz_result = QuizResult(user_id=current_user.id, quiz_id=quiz.id, score=score, total=total_questions)
        db.session.add(quiz_result)
        db.session.commit()
        
        return render_template('quiz_result.html', score=score,total=total_questions,)
    
    return render_template('take_quiz.html', quiz=quiz)


# Allows the user to edit question
@bp.route('/edit_question_ajax', methods=['POST'])
@login_required
def edit_question_ajax():
    try:
        question_id = request.form['question_id']
        question = Question.query.get_or_404(question_id)
        
        # Check if the user owns the quiz
        if question.quiz.user_id != current_user.id:
            return jsonify({'success': False, 'error': 'Unauthorized'}), 403
        
        # Validate that correct answer is one of the options
        options_list = [opt.strip() for opt in request.form['options'].split(',')]
        if request.form['correct_answer'] not in options_list:
            return jsonify({'success': False, 'error': 'Correct answer must be one of the options'}), 400
        
        question.text = request.form['question']
        question.options = request.form['options']
        question.correct_answer = request.form['correct_answer']
        
        db.session.commit()
        return jsonify({'success': True})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500


# Allows the user to remove question
@bp.route('/remove_question_ajax', methods=['POST'])
@login_required
def remove_question_ajax():
    try:
        question_id = request.form['question_id']
        question = Question.query.get_or_404(question_id)
        
        # Check if the user owns the quiz
        if question.quiz.user_id != current_user.id:
            return jsonify({'success': False, 'error': 'Unauthorized'}), 403
        
        UserAnswer.query.filter_by(question_id=question_id).delete()
        
        db.session.delete(question)
        db.session.commit()
        return jsonify({'success': True})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500
