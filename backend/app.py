from flask import Flask

#UPLOAD_FOLDER = 'static/uploads/'
UPLOAD_FOLDER = './'
app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
