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
COLLECTION_REVIEW = 'reviews'
COLLECTION_RESTAURANT = 'restaurants'

# Connection to MONGODB
connect = pymongo.MongoClient(MONGO_URI)
db_review =connect[DATABASE_NAME][COLLECTION_REVIEW]
db_restaurant =connect[DATABASE_NAME][COLLECTION_RESTAURANT]
print("**** Connected to MongoDB Database ****")

# HOME ROUTE 
@app.route('/')
def index():
    reviews = db_review.find({})
    restaurants = [{'name':'test'}]
    return render_template('index.html', reviews=reviews, restaurants=restaurants)

# CREATE REVIEW ROUTE
@app.route('/create_review', methods=["GET", "POST"])
def create_review():
    if request.method == "POST":
        restaurant = request.form.get("restaurant")
        db_review.insert({
            'restaurant': restaurant
        })
        return redirect(url_for('index'))
    return render_template('create_review.html')

# UPDATE REVIEW ROUTE
@app.route('/update_review/<task_id>', methods=["GET", "POST"])
def update_review(task_id):
    if request.method == "POST":
        restaurant = request.form.get("restaurant")
        db_review.update({
            "_id" : ObjectId(task_id)
        },{
            '$set': {
            'restaurant': restaurant
            }
        }) 
        return redirect(url_for('index'))

    review_edit = db_review.find_one({
      "_id":ObjectId(task_id)
    })
    return render_template('update_review.html', review=review_edit)

# DELETE REVIEW ROUTE
@app.route('/delete_review/<task_id>')
def delete_review(task_id):
    db_review.delete_one({
        '_id':ObjectId(task_id)
    })
    return redirect(url_for('index'))





if __name__ == '__main__':
   app.run(host=os.environ.get('IP'), #host: where is it hosted at.. rep the address
           port=int(os.environ.get('PORT')), #port:  which port, environment variable
           debug=True)