from flask import Flask, jsonify, request

app = Flask(__name__)

data = [
    {
        'name': 'raymond',
        'lang': 'py',
    },
    {
        'name': 'jon',
        'lang': 'c#'
    }
]

@app.route('/developers/<string:name>', methods=['GET', 'DELETE'])
def developer(name):
    if request.method == 'GET':
        for dev in data:
            if name == dev['name']:
                return dev
        else:
            return 'dev not found', 404
    else:
        pass # implement

@app.route('/developers', methods=['GET', 'POST'])
def developers():
    if request.method == 'POST':
        # add that item to the list
        pass
    else:
        return jsonify(data)
