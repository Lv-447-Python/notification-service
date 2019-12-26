from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_socketio import SocketIO

async_mode = None
APP = Flask(__name__)
CORS(APP)
API = Api(APP)
APP.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(APP, cors_allowed_origins="*")

