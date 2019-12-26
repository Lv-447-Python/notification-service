from threading import Lock
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_socketio import SocketIO

async_mode = None
APP = Flask(__name__)
CORS(APP)
API = Api(APP)
APP.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(APP, async_mode=async_mode, cors_allowed_origins="*")
thread = None
thread_lock = Lock()
