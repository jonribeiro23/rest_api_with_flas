from flask import Flask, jsonify, request, render_template
from operator import itemgetter
from helper import finder
from pprint import pprint

app = Flask(__name__)

stores = [
    {
        'name': 'My Wondeful Store',
        'items': [
            {
                'name': 'My item',
                'price': 15.99
            }
        ]
    }
]


# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


@app.route('/')
def home():
    return render_template('index.html')


# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify('The store was not found')


# GET /store
@app.route('/stores')
def get_stores():
    return jsonify(stores)


# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'items': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'Store not found'})


# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    store = finder.search(stores, name, itemgetter('name'))
    return jsonify({'items': store['items']})


app.run(port=5000, debug=True)
