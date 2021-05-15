from bot import ObjectTracker
from flask import Flask, json, request, jsonify

from flask_cors import CORS, cross_origin

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['Access-Control-Allow-Origin'] = '*'

@app.route('/object-tracker', methods=['GET'])
@cross_origin()
def start():
    object_tracker = ObjectTracker()
    response = object_tracker.start_bot()
    return jsonify({"response": response})

app.run('0.0.0.0', 3000, debug=True)
