from flask import Flask, render_template, request
import os, pymongo
from dotenv import load_dotenv

# SET UP FLASK
app = Flask(__name__)

# SET UP FLASK SECRET KEY
app.secret_key = os.environ.get('SECRET_KEY')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_review')
def create_review():
    return render_template('create-review.html')


if __name__ == '__main__':
   app.run(host=os.environ.get('IP'), #host: where is it hosted at.. rep the address
           port=int(os.environ.get('PORT')), #port:  which port, environment variable
           debug=True)