from flask import Flask

from config import Config

from .auth.routes import auth
from .models import db, User, Pokemon
from flask_migrate import Migrate
from flask_login import LoginManager
from .api.routes import api


from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config.from_object(Config)

login = LoginManager()

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

db.init_app(app)
migrate = Migrate(app, db)

login.init_app(app)
login.login_view = 'auth.login'

app.register_blueprint(auth)
app.register_blueprint(api)

from . import routes

from . import models