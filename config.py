# config.py


import os

# grabs the folder where the script runs
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'actionlog.db'
USERNAME = 'admin'
PASSWORD = 'admin'
CSRF_ENABLED = True
SECRET_KEY = 'something_complex_and cryptic'

# defines the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)
