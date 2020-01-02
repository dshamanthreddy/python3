import json
import pymongo
from flask import Flask,request,jsonify
app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'shamanth'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/shamanth'

mongo = PyMongo(app)

@app.route("/app", methods=['POST'])
def add():
	collection1 = mongo.db.collection1 

    #name = request.json['name']
    #language = request.json['language']
	c_id = collection1.insert({"name" : "name", "language" : "language"})
	#new_record = collection1.find_one({"_id" : c_id})
	#output = {"name" : new_record["name"], "language" : new_record["language"]}
    #return "done"

if __name__ == '__main__':
    app.run(debug=True)