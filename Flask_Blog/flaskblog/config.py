import os


class Config:
    SECRET_KEY = '16d2ef57a678d559ce99b6e6116a568f'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'wewillrecreateindia@gmail.com'
    MAIL_PASSWORD = 'companymen'
class firebaseConfig:
    projectId= "vitual-share-market"
    apiKey= "AIzaSyBcoJLRqdLjrCg8cAG4Z7MI7P_ijDcHC5g"
    authDomain= "vitual-share-market.firebaseapp.com"
    databaseURL= "https://vitual-share-market.firebaseio.com"
    storageBucket= "vitual-share-market.appspot.com"
    messagingSenderId= "128045272026"
    appId= "1:128045272026:web:8783f651c827b9ef790ee3"
    measurementId= "G-84V4VLM34K"
