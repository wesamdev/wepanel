# db.py
from flask import jsonify, request, redirect, url_for
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["wepanel"] 
users_collection = db["users"]
import json

with open('config.json') as f:
    config = json.load(f)

apikey = config['panel']['apikey']


def get_user_coins(userid):
    if request.method == "GET" and request.headers.get("Authorization"):
        if apikey != request.headers.get("Authorization"):
            return jsonify({"error": "Invalid API key"}), 401
        user = users_collection.find_one({"userid": userid})
        if user:
            return jsonify({"coins": user["coins"]})
        else:
            return jsonify({"error": "User not found"}), 404
    else:
        return jsonify({"error": "Method not allowed"}), 405