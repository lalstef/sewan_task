from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route("/api/v1.0/notification", methods=['POST'])
def receive_notification():
    notification = request.json.get('notification')
    if notification:
        return jsonify(message="Notification received: {}.".format(notification))
    else:
        return jsonify(message="Empty notification received")