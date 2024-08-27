from werkzeug.security import generate_password_hash, check_password_hash
import hashlib
from flask_login import LoginManager, UserMixin
from app import app, db

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

def generate_md5_hash(value):
    return hashlib.md5(value.encode()).hexdigest()



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    email = db.Column(db.String(80), nullable=False, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)
    

    def to_dict(self):
       return{
         "id": self.id,
         "username": self.username,
         "email": self.email
    }


    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)        

    

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()

