This is a simple web application built using Python Flask. The app allows users to take, create, and manage their quizzes. Users can log in, take quizzes, and view their scores.

## Features:
-	**User Authentication**: Users can register and log in to access their quizzes.
-	**Quiz Creation**: Users can create new quizzes with titles and questions.
-	**Quiz Management**: Users can manage their quizzes, including adding, editing, and deleting questions.
-	**Quiz Taking**: Users can take quizzes and view their scores.
-	**Recent Scores**: Users can view their recent quiz scores on the dashboard.

## API Endpoints:
- **GET /register**: Registration page for new users.
- **GET /login**: Login page for existing users.
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

## Implementation Details

### **User Registration**
- **Route**: `/register`
- **Method**: `POST`
- **Form Data**: `username`, `email`, `password`
- **Validation"": Ensure that `username`, `email`, and `password` are not empty. 
- **Password Hashing**: Use `Flask-Bcrypt` to securely hash the password.

### **User Login**
- **Route**: `/login`
- **Method**: `POST`
- **Form Data**: `username`, `password`
- **Validation**: Ensure that `username` and `password` are not empty.
- **Authentication**: Use `Flask-Login` to authenticate users.

### **Dashboard** (`/dashboard`)
- **Route**: `/dashboard`
- **Method**: `GET`
- **Functionality**: Display a list of quizzes created by the user.
- **Validation**: Ensure that the user is logged in.
- **Database Queries**: Fetch quizzes created by the current user.

### **Creating a Quiz**
- **Route**: `/create_quiz`
- **Method**: `POST`
- **Form Data**: `title`, `questions` (list of question objects)
- **Validation**: Ensure that `title` is not empty. Validate each question for correctness.

### **Manage Quiz** (`/manage_quiz/<int:quiz_id>`)
- **Route**: `/manage_quiz/<int:quiz_id>`
- **Method**: `GET`, `POST`
- **Functionality**: Display quiz details, add new questions, and manage existing questions.
- **Validation**: Ensure that the quiz ID exists and the user has permission to manage it.
- **Database Queries**: Fetch quiz details and questions from the database.

### **Taking a Quiz**
- **Route**: `/take_quiz/<int:quiz_id>`
- **Method**: `GET`, `POST`
- **Form Data**: `answers` (list of answer IDs)
- **Validation**: Ensure that each question has an answer selected.
- **Scoring**: Calculate score based on correct answers.

### **Edit Question** (`/edit_question/<int:question_id>`)
- **Route**: `/edit_question/<int:question_id>`
- **Method**: `GET`, `POST`
- **Functionality**: Edit an existing question.
- **Validation**: Ensure that the question ID exists and the user has permission to edit it.
- **Database Queries**: Fetch the question from the database and update it.

### **Remove Question** (`/remove_question/<int:question_id>`)
- **Route**: `/remove_question/<int:question_id>`
- **Method**: `POST`
- **Functionality**: Delete a question.
- **Validation**: Ensure that the question ID exists and the user has permission to delete it.
- **Database Queries**: Delete the question from the database.
