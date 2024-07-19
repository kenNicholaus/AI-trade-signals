import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
#from earnings.config import Config

app = Flask(__name__)
#app.config.from_object(Config)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)

from earnings import routes

#from earnings.users.routes import users
#from earnings.posts.routes import posts
#from earnings.main.routes import main

#app.register_blueprint(users)
#app.register_blueprint(posts)
#app.register_blueprint(main)

#def create_app(config_class=Config):
#    app = Flask(__name__)
#    app.config.from_object(Config)
#
#    db.init_app(app)
#    bcrypt.init_app(app)
#    login_manager.init_app(app)
#    mail.init_app(app)
#
#    from earnings.users.routes import users
#    from earnings.posts.routes import posts
#    from earnings.main.routes import main
#    app.register_blueprint(users)
#    app.register_blueprint(posts)
#    app.register_blueprint(main)
#
#    return app
