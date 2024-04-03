from flask import render_template
from flask import redirect, url_for, session
from authlib.integrations.flask_client import OAuth

def login():
    return render_template('login.html')

oauth=None
discord=None
def init_outh(app):
    global oauth, discord
    oauth = OAuth(app)
    discord = oauth.register(
        name='discord',
        client_id='your_discord_client_id',
        client_secret='your_discord_client_secret',
        authorize_url='https://discord.com/api/oauth2/authorize',
        authorize_params=None,
        access_token_url='https://discord.com/api/oauth2/token',
        access_token_params=None,
        refresh_token_url=None,
        client_kwargs={'scope': 'identify'}
    )


def callback():
    token = discord.authorize_access_token()
    session['user'] = token
    return redirect(url_for('home'))
def discord_login():
    redirect_uri = url_for('callback', _external=True)
    return discord.authorize_redirect(redirect_uri)

