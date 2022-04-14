from pymongo import MongoClient
from config import Config


class MongodbService:
    _instance = None
    _client = None
    _db = None
    _collection = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls.__init__(cls._instance)
        return cls._instance

    def __init__(self):
        self._client = MongoClient(Config.MONGODB_URI)
        self._db = self._client[Config.DB_NAME]
        self._collection = self._db[Config.DB_COLLECTION]

    def save(self, data):
        self._collection.insert_one(data)

    def get_by_id(self, _id: int):
        return self._collection.find_one(filter={'_id': _id})

    def get_all(self):
        return list(self._collection.find())

    def delete_all(self):
        self._collection.delete_many({})

    def delete_by_id(self, data: dict):
        self._collection.delete_one(filter=data)

    def update(self, data: dict):
        self._collection.update_one(filter={"_id": data['_id']}, update={'$set': data})
