import unittest
from app import create_app, db
from app.models import User, Quiz, Question

class TestQuizApp(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.appctx = self.app.app_context()
        self.appctx.push()
        db.create_all()
        
        # Create a test user
        self.user = User(username='testuser', email='test@example.com', password='testpassword')
        db.session.add(self.user)
        db.session.commit()
        
        # Create a test quiz
        self.quiz = Quiz(title='Test Quiz', user_id=self.user.id)
        db.session.add(self.quiz)
        db.session.commit()
        
        # Create a test question
        self.question = Question(text='Test Question', options='Option1,Option2', correct_answer='Option1', quiz_id=self.quiz.id)
        db.session.add(self.question)
        db.session.commit()
    
    
    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
            db.engine.dispose()
    

    def test_create_user(self):
        user = User.query.filter_by(username='testuser').first()
        self.assertEqual(user.username, 'testuser')

    
    def test_create_quiz(self):
        quiz = Quiz.query.first()
        self.assertEqual(quiz.title, 'Test Quiz')
    
    def test_create_question(self):
        question = Question.query.first()
        self.assertEqual(question.text, 'Test Question')
    
    def test_login(self):
        tester = self.app.test_client()
        response = tester.post('/login', data={'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 200)
    
    def test_create_quiz_route(self):
        tester = self.app.test_client()
        with self.app.test_client() as client:
            client.post('/login', data={'username': 'testuser', 'password': 'testpassword'})
            response = client.post('/create_quiz', data={'title': 'New Quiz'})
            self.assertEqual(response.status_code, 302)
    
    def test_manage_quiz_route(self):
        tester = self.app.test_client()
        with self.app.test_client() as client:
            client.post('/login', data={'username': 'testuser', 'password': 'testpassword'})
            response = client.get('/manage_quiz/1', follow_redirects=True)
            self.assertEqual(response.status_code, 200)
    
    def test_take_quiz_route(self):
        tester = self.app.test_client()
        with self.app.test_client() as client:
            client.post('/login', data={'username': 'testuser', 'password': 'testpassword'})
            response = client.get('/take_quiz/1')
            self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
