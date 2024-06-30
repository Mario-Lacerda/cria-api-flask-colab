from flask import Blueprint, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId

db = MongoClient('mongodb://localhost:27017')
collection = db.developers.developers #COLLECTION CALLED DEVELOPERS

developers = Blueprint('developers', __name__)

#GET ALL DEVELOPERS
@developers.route('/dev', methods=['GET'])
def getDevs():
    developers = []
    for i in collection.find():
        i['_id'] = str(i['_id']) #CONVERT OBJECTID TO STRING
        developers.append(i)

    return jsonify(developers), 200

#INSERT ONE DEVELOPER
@developers.route('/dev', methods=['POST'])
def insertDev():
    data = request.get_json()
    developer = {'name': data['name'], 'language': data['language']}
    collection.insert_one(developer)
    return jsonify(data), 201

#UPDATE DEVELOPER
@developers.route('/dev/<string:id>', methods=['PUT'])
def updateDev(id):
    data = {'name': request.get_json().get('name'), 'language': request.get_json().get('language')}
    collection.update_one({'_id': ObjectId(id)}, {'$set': data})
    return jsonify(data), 200

#DELETE DEVELOPER
@developers.route('/dev/<string:id>', methods=['DELETE'])
def deleteDev(id):
    collection.delete_one({'_id': ObjectId(id)})
    return jsonify({'message': 'Dev is not longer alive'}), 200
