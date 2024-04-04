from flask import render_template, session
import requests
import json

with open('config.json') as f:
    config = json.load(f)


def userinfo():
    username = session.get('username')
    avatarurl = session.get('avatarurl')
    userid = session.get('userid')

    if username and avatarurl and userid:
        usercoins = requests.get(f"{config['panel']['url']}/api/user/{userid}" + "/coins", headers={"Authorization": config['panel']['apikey']})
        if usercoins.status_code == 200:
            coins_data = usercoins.json()
            coins = coins_data.get("coins")
            return render_template('userinfo.html', user_name=username, user_id=userid, avatar_url=avatarurl,user_coins = coins)
    else:
        return 'User information not available'
