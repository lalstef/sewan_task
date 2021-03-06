from flask import Flask, jsonify, request
from sewan.notifiers import registered_notifiers

app = Flask(__name__)


@app.route("/api/v1.0/notification/", methods=['POST'])
def receive_notification():
    notification = request.json.get('notification')

    # Re-dispatch the notification to all registered notifiers
    for notifier in registered_notifiers:
        try:
            notifier.notify(notification)
        except Exception as e:
            print('Notifier {} failed with the following error: {}'.format(str(notifier), e))

    # Let the other end know that the notification was properly received
    if notification:
        return jsonify(message="Notification received: {}.".format(notification))
    else:
        return jsonify(message="Empty notification received")