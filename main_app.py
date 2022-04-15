from database import MongodbService
from flask import Flask, request, jsonify
from config import Config
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
storage = MongodbService()


@app.route('/get-all', methods=['GET'])
def get_all():
    data = storage.get_all()
    return jsonify(data)


@app.route('/save', methods=['POST'])
def save():
    data = request.get_json(force=True)
    storage.save(data)
    return 'saved'


@app.route('/delete-by-id', methods=['POST'])
def delete_by_id():
    data = request.get_json(force=True)
    storage.delete_by_id(data)
    return 'deleted'


@app.route('/update', methods=['POST'])
def update():
    data = request.get_json(force=True)
    storage.update(data)
    return 'updated'


if __name__ == '__main__':
    app.run()
