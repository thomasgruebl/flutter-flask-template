from flask import Flask
from werkzeug.serving import WSGIRequestHandler

from routes.routes import info_api, index_api, image_api

HOSTNAME = '0.0.0.0'
PORT = 5000

UPLOAD_FOLDER = '../images/api_uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def create_app():
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    WSGIRequestHandler.protocol_version = "HTTP/1.1"

    app.register_blueprint(index_api, url_prefix='/api')
    app.register_blueprint(info_api, url_prefix='/api')
    app.register_blueprint(image_api, url_prefix='/api')

    return app


app = create_app()
app.run(host=HOSTNAME, port=PORT)
