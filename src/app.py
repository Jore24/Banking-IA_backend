from flask import Flask
from flask_cors import CORS
from src.controllers.auth import *

app = Flask(__name__) 
app.secret_key = 'group2'

CORS(app, resources={r"/*": {"origins": "*"}})


# User Authentication
@app.route('/auth/login', methods=['POST'])
def login():
    return user_login()


# User Register
@app.route('/auth/register', methods=['POST'])
def register():
    return user_register()
