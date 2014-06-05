#!/usr/bin/python

# -*- coding: utf-8 -*-

################
# homepage-gen #
################

import sys

from app import app, db
from app.mod_auth.models import User
from flask import Flask, \
                  render_template, \
                  request#, \
                  #flash, redirect, url_for, session

from os import chmod, \
               getpid, \
               getppid
from shutil import copyfile
from time import time

from config import \
    TEMPLATE_CONFIGURATION, \
    RESTRICT_BY_IP, \
    IPS, \
    HOST, \
    PORT, \
    DEBUG

#app = Flask(__name__)

## old user module hack
# from flask.ext.login import LoginManager
# login_manager = LoginManager()
# login_manager.init_app(app)
# @login_manager.user_loader
# def load_user(userid):
#     try:
#         return User.get(userid)
#     except:
#         return None
# @app.route("/login", methods=['GET', 'POST'])
# def login():    

def getUserList():
    users =  User.query.filter_by(email="arcshams@gmail.com").first()
    return users

@app.route('/')
def index():
    """
    The web application main entry point.
    """   
    users=getUserList()
    return render_template('index.html',
                           users=users,
                           **TEMPLATE_CONFIGURATION)

@app.route('/<user_id>')
def show(user_id):
    return render_template('profile.html', id = user_id )

@app.route('/test')
def test():
    """
    test page.
    """
    if not RESTRICT_BY_IP or ( RESTRICT_BY_IP and request.remote_addr in IPS ):
        return render_template('test.html')
    else:
        return "Access denied."

@app.route('/save', methods=['POST'])
def save_state():
    """
    Save the current state to a local file.
    """
    try:
        state = request.form.get('state')
        state = state.encode('utf-8')
        f = open(".state", "w")
        f.write(state)
        f.close()
        return "1"
    except:
        print e
        return "0"

@app.route('/load', methods=['GET'])
def load_state():
    """
    Load the last state from a local file.
    """
    try:
        f = open(".state", "r")
        state = f.read()
        state = state.decode('utf-8')
        f.close()
        chmod(".state", 0600)
        return state
    except:
        return "|||"

@app.route('/reset', methods=['GET'])
def reset_state():
    """
    Version the current state in a local file and reset it.
    """
    try:
        version = str(time())
        copyfile(".state", ".state.%s" % (version,))
        chmod(".state.%s" % (version,), 0600)
        f = open(".state", "w")
        f.write("")
        f.close()
        chmod(".state", 0600)
        return "1"
    except:
        return "0"

def save_pid():
    """
    Get the process ID and store it in a local file.
    """
    try:
        pid = getpid()
        ppid = getppid()
        if ( ppid != 1 ):
            pid = ppid
        f = open(".pid", "w")
        f.write(str(pid))
        f.close()
        chmod(".pid", 0600)
    except:
        pass

if __name__ == '__main__':
    try:
        print str(getUserList())
        #if not RESTRICT_BY_IP or ( RESTRICT_BY_IP and request.remote_addr in IPS ):
        # First, store the process ID
        save_pid()
        # Configure and start the web application with the given settings.
        app.debug = True #DEBUG
        app.run(host = HOST,
                port = PORT,
                debug = True)
    except:
        raise
