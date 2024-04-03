# logout.py
from flask import session, redirect, url_for
def logout():
    session.clear()
    return redirect(url_for("login"))