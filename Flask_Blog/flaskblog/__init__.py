from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore,auth
import pyrebase



firebaseConfig={

  "apiKey": "AIzaSyBcoJLRqdLjrCg8cAG4Z7MI7P_ijDcHC5g",
  "authDomain": "vitual-share-market.firebaseapp.com",
  "databaseURL": "https://vitual-share-market.firebaseio.com",
  "projectId": "vitual-share-market",
  "storageBucket": "vitual-share-market.appspot.com",
  "messagingSenderId": "128045272026",
  "appId": "1:128045272026:web:8783f651c827b9ef790ee3",
  "measurementId": "G-84V4VLM34K",
  "type": "service_account",
  "project_id": "vitual-share-market",
  "private_key_id": "c72ce91212714bb47cc0bdb8ad026fadb6694f6a",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCXpCynW+bjh0OV\nwSnQi738649vg29PAJr8AssIb57ye8qOKUN6viRUyiiHW2u913vbTFFw+WmRK5IC\nM3DQ3c9bNkZ1i5HkRsnuWLLaMGhzx9R1ouAYu2qn/JsRSMTzdUWXwLv41aVvPzmz\n6oBWo7KoZFfxUExuldrewQkrRZ6x88QcWE6QuPslHTCSpuZr2iN0qf5sTHGNTGX7\nOQ4yui8O19nunDsiQxKoor/OtBtzJ7A0i0P2WLnXOPoVxSiHs+dnpkUyv/tecg7d\nlZQBEujCe+x5c0xKarPG/GAgVMQmc3vcUJgPwyfWwSr2pBaeXlShVzcVCYiWclMy\n4c8MX/zTAgMBAAECggEAIXyjUcgFOlyuC52PBts9NuOsFrOfOoKHNzzEqlW/84tr\nxS4OlUX1DvZfsdh59//kfZ6iY4Dok6LcCPlkIfPBrUJUl/Oc4ZzSTfyvbmh/QIYy\nAFJaC4wjtvodIlmACMVue18YA5DmiiUbsIQKGFfpBa+3DfauEkOshEF7rV8f9urn\nZXva/TYr0o3i/jWknzMgXHw6Sv6yj+clRtJAXaSsIiTVy5+Wpi0ln4t9ic6FRXSg\n7vZYgOkv3eZzj+3Y/m6ZHHaWG8OHENyYZXgSEO4YD2+WSxQZtQ3GHPGn3fUh+znf\nu0sL1VR4WfOOQaohpyDr1PcHo3B7Z3t7w53h2jYVaQKBgQDLMsErEMSxGym0EGiq\nYl2nTwB1wZ5vYWspsomcyClJheUww1oO9zV8YOIbrSErRnQ+VDZxAdEMVY+rsrBy\n7FtJ/6YQeL6C1S0i0SUQy28lqWl1lTtJvg/CJi1JwmuWOAlfGBSAvr+WqzOZFBkx\n2KAtq3mYOgnkFMSuBMhpYUbj+wKBgQC/C7mkGHszUpPKIAqxTGFwFNj4VyvjpdJ6\n271wunBRZSoHD7phWDmOTuEJW8KOCbtspc2je6RUHXC2ONC3H4O/gAuNUHjxh20/\nbpzLriHmiWkbyqkUfaE1l9zO7c8ATkWxKcEU3COiLeF2upXxh74VBqwkspz1wqRh\nfg74XjubCQKBgCvCuHsv10xVDzwqNIBNQuIfT3gMxLQ0BMIsIxrSuKGO5ncD+0cx\n0iEBNHDFbllFiQ9LT5Yyz/SaEKDnkLyPTnG3TupJNq4yfs/6vsLJLRytSXr7MpOF\nDRvA4Qv7hPQLCWmjY/b+HYCzSh9zhqGHh6eOQFeaWDr4hgr8GLUpL/01AoGAA0eL\nP0LgUog3Wz/jjxmVjpv9AX5VlYnSLCO7g8TfirYm24osk+E007mM6WE23MNUAVBz\nUDweHQeIWMhu5MXYuB/Vku5vtQ2zFWSrsl9h25g+Qqje8Cgb7VSXCMJSTFoLnjfu\nRZJl1jHdbfFUA5pl6+x6ZgLe6OUXd0j3rtHHSikCgYBrKgOGboxvaBBk5L466YjR\n/WSNlXa0w6heb1jJiqC/yoFNMDrMQdnNtcFVwWba0e0a9ibGL3qyq328XVDAkWKR\n4K4N+ZWHkTpFGclcxN29QH9BgNFOTHhKWAF6eNsm9yepKVMDbjsz5C7c7sZUMMaH\nVzuoaAuJVyqdaFPtUn0qkQ==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-1qz7s@vitual-share-market.iam.gserviceaccount.com",
  "client_id": "114767129082450117507",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-1qz7s%40vitual-share-market.iam.gserviceaccount.com"

}


cred=credentials.Certificate(firebaseConfig)
firebaseapp=firebase_admin.initialize_app(cred)
Db=firestore.client()
firebase=pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)


    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    from flaskblog.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)
    with app.app_context():
        db.create_all()

    return app