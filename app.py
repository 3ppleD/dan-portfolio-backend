from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
import cloudinary


app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "https://dan-portfolio-backend.onrender.com"}})

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


# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///MyPortfolioDB.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['DBHUB_API_KEY'] = 'XdPOtCf7emmaTY4shQszPYI5V9E9ID282jjBcmFWM5_49NUKLgsz4A'
app.config['DBHUB_DB_NAME'] = 'MyPortfolioDB.db'
# app.config['DBHUB_USERNAME'] = 'your_dbhub_username' 


db = SQLAlchemy(app)
migrate = Migrate(app, db)


with app.app_context():
    db.create_all()

from portfolioRoute import port_bp
app.register_blueprint(port_bp)
from userRoute import user_bp
app.register_blueprint(user_bp)



