from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'rahulreddygangapuram@1234567890'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz_app.db'

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    from .routes import auth, quiz, main
    app.register_blueprint(auth.bp)
    app.register_blueprint(quiz.bp)
    app.register_blueprint(main.bp)

    return app
