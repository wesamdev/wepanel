import os
from flask import render_template, session, redirect, url_for
import json
from flask_discord import DiscordOAuth2Session, Unauthorized
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["wepanel"] 
users_collection = db["users"]

with open('config.json') as f:
    config = json.load(f)

def login():
    return render_template('login.html')

discord = None

def init_oauth(app):
    global discord
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "true"  # !! Only in development environment.

    app.config["DISCORD_CLIENT_ID"] = config['discord']['client_id']    # Discord client ID.
    app.config["DISCORD_CLIENT_SECRET"] = config['discord']['client_secret']  # Discord client secret.
    app.config["DISCORD_REDIRECT_URI"] = config['discord']['redirect_uri']   # URL to your callback endpoint.

    discord = DiscordOAuth2Session(app)

    @app.errorhandler(Unauthorized)
    def redirect_unauthorized(e):
        return redirect(url_for("login"))

def callback():
    discord.callback()
    user = discord.fetch_user()

    # Check if user is already registered
    existing_user = users_collection.find_one({"userid": user.id})
    if existing_user:
        # If user is registered, update username and avatar if changed
        if existing_user["username"] != user.name or existing_user["avatar"] != user.avatar_url:
            users_collection.update_one({"_id": existing_user["_id"]},
                                        {"$set": {"username": user.name, "avatar": user.avatar_url}})
    else:
        # If user is not registered, create user document in the database
        user_data = {
            "username": user.name,
            "userid": user.id,
            "avatar": user.avatar_url,
            "coins": 0,  # Initial number of coins
            "servers": []  # Empty list of servers
        }
        users_collection.insert_one(user_data)

    session['username'] = user.name
    session['avatarurl'] = user.avatar_url
    session['userid'] = user.id

    return redirect(url_for(".dashboard"))

def discord_login():
    return discord.create_session()
