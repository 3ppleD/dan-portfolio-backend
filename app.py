from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
import cloudinary


app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})

# @app.after_request
# def after_request(response):
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
#     response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Accept, Accept-Language, Accept-Encoding')
#     return response

cloudinary.config(
    cloud_name="dosvdonf0",
    api_key = "161476777338785",
    api_secret = "vZaBT-wQRnK3dSHzFmknUbFl5WY"
)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///MyPortfolioDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mysecretkey'


db = SQLAlchemy(app)
migrate = Migrate(app, db)


with app.app_context():
    db.create_all()

from portfolioRoute import port_bp
app.register_blueprint(port_bp)
from userRoute import user_bp
app.register_blueprint(user_bp)



