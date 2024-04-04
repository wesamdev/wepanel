# db.py
from flask import jsonify, request, redirect, url_for
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["wepanel"] 
users_collection = db["users"]


# make this func json def get_user_coins(userid):

def get_user_coins(userid):
    if request.method == "POST":
        user = users_collection.find_one({"userid": userid})
        return jsonify({"coins": user["coins"]})
    else:
        return redirect(url_for("login"))
