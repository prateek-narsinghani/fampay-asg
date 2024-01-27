from dotenv import load_dotenv
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    _api_key = None
    _predefined_search_query = None
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')

    def __init__(self):
        load_dotenv()

    @staticmethod
    def get_api_key():
        if Config._api_key is None:
            Config._api_key = os.getenv('API_KEY')
        return Config._api_key
    
    @staticmethod
    def get_predefined_search_query():
        if Config._predefined_search_query is None:
            Config._predefined_search_query = os.getenv('QUERY_TERM')
        return Config._predefined_search_query