from flask import Flask, render_template, request
import os
import pymongo
from dotenv import load_dotenv

# SET UP FLASK
app = Flask(__name__)

# SET UP FLASK SECRET KEY
app.secret_key = os.environ.get('SECRET_KEY')

# SET UP MONGODB
MONGO_URI = os.environ.get('MONGO_URI')
DATABASE_NAME = 'Eat_rank'
COLLECTION_NAME = 'reviews'

# Connection to MONGODB
connect = pymongo.MongoClient(MONGO_URI)
db_review =connect[DATABASE_NAME][COLLECTION_NAME]
print("**** Connected to MongoDB Database ****")

@app.route('/')
def index():
    result = db_review.find({})
    return render_template('index.html', data=result)

@app.route('/create_review', methods=["GET", "POST"])
def create_review():
    if request.method == "POST":
        print("Post")
        return "POST"
    return render_template('create-review.html')


if __name__ == '__main__':
   app.run(host=os.environ.get('IP'), #host: where is it hosted at.. rep the address
           port=int(os.environ.get('PORT')), #port:  which port, environment variable
           debug=True)