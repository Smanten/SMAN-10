from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask('__name__', template_folder='sim/templates', static_folder='sim/static')
app.config['SECRET_KEY'] = "petugas"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sim_petugas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from sim.mahasiswa.routes import rpetugas
app.register_blueprint(rpetugas)