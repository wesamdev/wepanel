from flask import render_template, session

def userinfo():
    # user = discord.fetch_user()
    # session['username'] = user.name
    # session['avatarurl'] = user.avatar_url
    # session['userid'] = user.id
    username = session.get('username')
    avatarurl = session.get('avatarurl')
    userid = session.get('userid')

    if username and avatarurl and userid:
        return render_template('userinfo.html', user_name=username, user_id=userid, avatar_url=avatarurl)
    else:
        return 'User information not available'
