import os


class Config:

    # SERVER_PORT = 8888
    # DB_HOST = 'localhost'
    # DB_PORT = 27017
    DB_NAME = 'tasks-db'
    DB_COLLECTION = 'tasks'
    MONGODB_URI = os.getenv('MONGODB_URI')
