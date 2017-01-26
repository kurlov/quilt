"""
Config file for dev. Overrides values in config.py.
"""
import os

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost/quilt'
OAUTH = dict(
    base_url='https://quilt-heroku.herokuapp.com',
    client_id='chrOhbIPVtJAey7LcT1ez7PnIaV9tFLqNYXapcG3',
    client_secret=os.getenv('OAUTH_CLIENT_SECRET')
)

AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')
PACKAGE_BUCKET_NAME = 'quilt-dpm-test'

SQLALCHEMY_ECHO = True
