from flask import Flask, render_template, request, redirect, url_for
from bson.objectid import ObjectId
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
        restaurant = request.form.get("restaurant")
        db_review.insert({
            'restaurant': restaurant
        })
        return redirect(url_for('index'))
    return render_template('create_review.html')

@app.route('/update_review/<task_id>', methods=["GET", "POST"])
def update_review(task_id):
    review_edit = db_review.find_one({
      "_id":ObjectId(task_id)
    })
    return render_template('update_review.html', review=review_edit)

if __name__ == '__main__':
   app.run(host=os.environ.get('IP'), #host: where is it hosted at.. rep the address
           port=int(os.environ.get('PORT')), #port:  which port, environment variable
           debug=True)