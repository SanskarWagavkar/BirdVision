from flask import Flask, make_response, jsonify, request
import dataset

app = Flask(__name__)
db = dataset.connect('sqlite:///api.db')

table = db['product']


def fetch_db(product_id):  # Each book scnerio
    return table.find_one(product_id=product_id)


def fetch_db_all():
    product = []
    for product in table:
        product.append(product)
    return product


@app.route('/api/db_populate', methods=['GET'])
def db_populate():
    table.insert({
        "product_id": "1",
        "name": "Ball"
    })

    table.insert({
        "product_id": "2",
        "name": "Rings"
    })

    return make_response(jsonify(fetch_db_all()),
                         200)


@app.route('/api/product_id', methods=['GET', 'POST'])
def api_product_id():
    if request.method == "GET":
        return make_response(jsonify(fetch_db_all()), 200)
    elif request.method == 'POST':
        content = request.json
        product_id = content['product_id_id']
        table.insert(content)
        return make_response(jsonify(fetch_db(product_id)), 201)  # 201 = Created


@app.route('/api/product/<product_id>', methods=['GET', 'PUT', 'DELETE'])
def api_each_product(product_id):
    if request.method == "GET":
        product_obj = fetch_db(product_id)
        if product_obj:
            return make_response(jsonify(product_obj), 200)
        else:
            return make_response(jsonify(product_obj), 404)
    elif request.method == "PUT":  
        content = request.json
        table.update(content, ['product_id'])

        product_obj = fetch_db(product_id)
        return make_response(jsonify(product_obj), 200)
    elif request.method == "DELETE":
        table.delete(id=product_id)

        return make_response(jsonify({}), 204)


if __name__ == '__main__':
    app.run(debug=True)
