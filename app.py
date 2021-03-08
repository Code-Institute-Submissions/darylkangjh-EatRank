from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world"
    
    
if __name__ == '__main__':
   app.run(host=os.environ.get('IP'), #host: where is it hosted at.. rep the address
           port=int(os.environ.get('PORT')), #port:  which port, environment variable
           debug=True)