This is a simple web application built using Python Flask. The app allows users to take, create, and manage their quizzes. Users can log in, take quizzes, and view their scores.

## Features:
-	**User Authentication**: Users can register and log in to access their quizzes.
-	**Quiz Creation**: Users can create new quizzes with titles and questions.
-	**Quiz Management**: Users can manage their quizzes, including adding, editing, and deleting questions.
-	**Quiz Taking**: Users can take quizzes and view their scores.
-	**Recent Scores**: Users can view their recent quiz scores on the dashboard.

## API Endpoints:
- **GET /login**: Login page for users.
- **GET /register**: Registration page for new users.
- **GET /dashboard**: User dashboard to view quizzes and recent scores.
-	**GET /create_quiz**: Create a new quiz.
-	**GET /manage_quiz/int:quiz_id**: Manage a specific quiz.
-	**GET /take_quiz/int:quiz_id**: Take a specific quiz.
-	**GET /edit_question/<int:question_id>**: Edit a specific question.
-	**GET /remove_question/<int:question_id>**: Remove a specific question.

## Software Stack:
- **Backend Framework**: Flask
- **Database ORM**: Flask-SQLAlchemy
- **CI Tool**: CircleCI
- **Containerization**: Docker
- **Cloud Platform**: AWS

## Dependencies:
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-Login
- Flask-WTF
- email-validator

## Database Design:
The application uses Flask-SQLAlchemy to manage a database with tables for User, Quiz, Question, Answer, and QuizResult.

## Security Measures:
- **Authentication**: Flask-Login is used for user authentication.
- **Password Hashing**: Secure password hashing protects user credentials.

## Deployment:
The application is deployed on AWS using Docker containers. CircleCI handles continuous integration.

## Architecture
The application architecture includes an EC2 instance running a Docker container with the Flask app, connected to an RDS database.
