import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

# Give access to the project from any Operating System we find ourselves in
# Will allow outside files/folders to be added to the project form the base directory

load_dotenv(os.path.join(basedir, '.env'))

class Config():
    """
    Set config variable for the flask app. 
    Using environment variables where available. 
    Otherwise create the config variable if not done already.
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or "Nana nana boo boo you'll never guess"
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEPLOY_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    