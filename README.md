Quiz App
This is a simple web application built using Python Flask. The app allows users to take, create, and manage their quizzes. Users can log in, take quizzes, and view their scores.

Features
-	User Authentication: Users can register and log in to access their quizzes.
-	Quiz Creation: Users can create new quizzes with titles and questions.
-	Quiz Management: Users can manage their quizzes, including adding, editing, and deleting questions.
-	Quiz Taking: Users can take quizzes and view their scores.
-	Recent Scores: Users can view their recent quiz scores on the dashboard.

API Endpoints
- GET /login: Login page for users.
- GET /register: Registration page for new users.
- GET /dashboard: User dashboard to view quizzes and recent scores.
-	GET /create_quiz: Create a new quiz.
-	GET /manage_quiz/int:quiz_id: Manage a specific quiz.
-	GET /take_quiz/int:quiz_id: Take a specific quiz.
-	GET /quiz_result: View quiz results after submission.

Required Software:
- Visual Studio Code (VS Code)
- Python 
- pip 

Dependencies:
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-Login
- Flask-WTF
- email-validator
