"""Server for the app."""
import os

os.system("source ./secrets.sh") #runs command line script in console 

from flask import (Flask, render_template, request, flash, session,
                   redirect, json, jsonify)
from jinja2 import StrictUndefined
import requests

secretkey = os.environ['SECRET_KEY'] #for sessions? do I need this?

app = Flask(__name__)
app.secret_key = secretkey 
app.jinja_env.undefined = StrictUndefined

@app.route('/status')
def show_status():
    """Route 1 - Show Success or Failure status"""

    return render_template('homepage.html')

@app.route('/get-data')
def get_data():
    """Route 2 - Get the blog post data via API from Hatchways"""

    # getting posts with tech and science tags
    tech_data = requests.get('https://api.hatchways.io/assessment/blog/posts?tag=tech')

    # this route must return JSON


