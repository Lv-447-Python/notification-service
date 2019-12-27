from notification_service import APP, socketio
from notification_service.views.notification import NotificationResourse

if __name__ == '__main__':
    socketio.run(APP, debug=True, host='0.0.0.0')