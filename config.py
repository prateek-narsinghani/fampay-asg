from dotenv import load_dotenv
import os

class Config:
    _api_key = None

    def __init__(self):
        load_dotenv()

    @staticmethod
    def get_api_key():
        if Config._api_key is None:
            Config._api_key = os.getenv('API_KEY')
        return Config._api_key