# config.py

import os

# Grabs folder where the script runs
BASEDIR = os.path.abspath(os.path.dirname(__file__))

# App variables
DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True
SECRET_KEY = 'my_precious'

# Defines the full path for the database
DATABASE_PATH = os.path.join(BASEDIR, DATABASE)
