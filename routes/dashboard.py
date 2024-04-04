from flask import render_template, session
import requests
import json

with open('config.json') as f:
    config = json.load(f)
def dashboard():
    username = session.get('username')
    avatarurl = session.get('avatarurl')
    userid = session.get('userid')
    print("Requesting")
    # use jsonfiy to get coins
    usercoins = requests.post(f"{config['panel']['url']}/api/user/{userid}" + "/coins", headers={"Authorization": config['panel']['apikey']})
    if usercoins.status_code == 200:
        coins_data = usercoins.json()
        coins = coins_data.get("coins")
        print(username, avatarurl, userid, coins)
        if username and avatarurl and userid and coins:
            return render_template('dashboard.html', user_name=username, user_id=userid, avatar_url=avatarurl,user_coins = coins)
        else:
            return 'User information not available'
    else:
        return 'User information not available'
