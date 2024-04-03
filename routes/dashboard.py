from flask import render_template, session

def dashboard():
    username = session.get('username')
    avatarurl = session.get('avatarurl')
    userid = session.get('userid')

    if username and avatarurl and userid:
        return render_template('dashboard.html', user_name=username, user_id=userid, avatar_url=avatarurl)
    else:
        return 'User information not available'
