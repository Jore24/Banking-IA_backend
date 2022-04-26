from flask import Flask, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)

@app.route("/")
def home_page():
    online_users = mongo.db.users.find({"online": True})
    return render_template("index.html", online_users=online_users)
    
mongo = PyMongo(app)

