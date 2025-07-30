from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return 'API is live!'

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    result = data['a'] + data['b']
    return jsonify({'result': result})
