import os
from flask import render_template, session
from flask import redirect, url_for
import json
from flask_discord import DiscordOAuth2Session, Unauthorized

with open('config.json') as f:
    config = json.load(f)


def login():
    return render_template('login.html')

discord=None
def init_outh(app):
    global discord
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "true"      # !! Only in development environment.

    app.config["DISCORD_CLIENT_ID"] = config['discord']['client_id']    # Discord client ID.
    app.config["DISCORD_CLIENT_SECRET"] = config['discord']['client_secret']             # Discord client secret.
    app.config["DISCORD_REDIRECT_URI"] = config['discord']['redirect_uri']               # URL to your callback endpoint.
    # app.config["DISCORD_BOT_TOKEN"] = ""                    # Required to access BOT resources.

    discord = DiscordOAuth2Session(app)
    @app.errorhandler(Unauthorized)
    def redirect_unauthorized(e):
        return redirect(url_for("login"))


def callback():
    discord.callback()
    user = discord.fetch_user()
    session['username'] = user.name
    session['avatarurl'] = user.avatar_url
    session['userid'] = user.id
    print(session)
    return redirect(url_for(".dashboard"))




def discord_login():
    return discord.create_session()

