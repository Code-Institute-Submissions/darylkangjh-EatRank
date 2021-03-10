from flask import Flask, render_template, request, redirect, url_for
from bson.objectid import ObjectId
import os
import pymongo
from dotenv import load_dotenv
import random

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
db_review = connect[DATABASE_NAME][COLLECTION_REVIEW]
db_restaurant = connect[DATABASE_NAME][COLLECTION_RESTAURANT]
print("**** Connected to MongoDB Database ****")

# SET UP CLOUDINARY
CLOUD_NAME = os.environ.get('CLOUD_NAME')
UPLOAD_PRESET = os.environ.get('UPLOAD_PRESET')

# HOME ROUTE 
@app.route('/')
def index():
    reviews = db_review.find({})
    restaurants = db_restaurant.find({})
    return render_template('index.html', reviews=reviews, restaurants=restaurants)



if __name__ == '__main__':
   app.run(host=os.environ.get('IP'), #host: where is it hosted at.. rep the address
           port=int(os.environ.get('PORT')), #port:  which port, environment variable
           debug=True)