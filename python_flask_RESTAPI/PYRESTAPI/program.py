from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask("__name__")

app.config['MONGO_DBNAME'] = "shamanth"
app.config['MONGO_URI'] = "mongodb://localhost:27017/shamanth"

mongo = PyMongo(app)

@app.route('/')
def hello():
	return "flask is running"

@app.route('/addorder', methods=['POST'])
def post_order():
	new_order={"name":request.json["name"]}
	#new_order={"name":request.json["name"]}
	mongo.db.o1.insert(new_order)
	return "order_inserted"

@app.route('/getorder', methods=['GET'])
def get_order():
	records=mongo.db.o1.find()
	orders=[]
	for i in records:
		i.pop('_id')
		orders.append(i)
	return jsonify(orders)	


@app.route('/modifyorder', methods=['PUT'])
def put_order():
	#get name to be modified
	name = request.args.get('name')
	#build query
	myquery = { "name": name }
	#get new name to be updated from input json request
	newName = request.json["name"]
	#set name to latest name
	newvalues = { "$set": { "name": newName } }
	#update the document with new name
	mongo.db.o1.update_one(myquery, newvalues)
	return "order updated"


@app.route('/deleteorder', methods=['DELETE'])
def del_order():
	name = request.args.get('name')
	m = { "name": name}
	mongo.db.o1.delete_one(m)
	return "deletedorder"


if __name__ == "__main__": app.run(debug=True)
