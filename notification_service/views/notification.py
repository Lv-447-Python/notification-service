from flask import make_response, request
from flask_restful import Resource
from flask_api import status
from flask_socketio import emit, send
from notification_service import socketio
from notification_service import API


@socketio.on('disconnect', namespace='/notification')
def test_disconnect():
    print('Client disconnected')
    emit("disconnect", namespace='/notification', broadcast=True)


@socketio.on('connect', namespace='/notification')
def test_connect():
    send("hi")
    print("Connected")


@socketio.on('message', namespace='/notification')
def handle_message(message):
    print('received message: ' + message)
    emit('message', message, namespace='/notification', broadcast=True)


class NotificationResourse(Resource):
    """Notification Resourse class. """

    def post(self):
        req_data = request.get_json()
        print(req_data)
        try:
            message = req_data["message"]
            handle_message(message)
            test_disconnect()
            return make_response({},status.HTTP_200_OK)
        except KeyError:
            return make_response({}, status.HTTP_400_BAD_REQUEST)


API.add_resource(NotificationResourse, '/notification/api/notify')
