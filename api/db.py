# db.py
from flask import request, session, redirect, url_for
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["wepanel"] 
users_collection = db["users"]


def get_user_coins(userid):
    if request.method == "POST":
        userid = request.form.get("userid")
        user = users_collection.find_one({"userid": userid})
        return user["coins"]
    else:
        return redirect(url_for("login"))