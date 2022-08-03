import base64
import collections
import glob
import hashlib
import io
import os

import numpy as np
from PIL import Image
from flask import Blueprint, request, send_file

from models.models import IndexModel, InfoModel, ImageModel
from schemas.schemas import IndexSchema, InfoSchema, ImageSchema

index_api = Blueprint('index', __name__)
info_api = Blueprint('info', __name__)
image_api = Blueprint('image', __name__)

info_schema = InfoSchema()
index_schema = IndexSchema()


@index_api.route('/', methods=['GET'])
@index_api.route('/v1', methods=['GET'])
def index():
    """
    This is the API index page.
    """
    result = IndexModel()
    return IndexSchema().dump(result), 200


@info_api.route('/v1/info', methods=['GET'])
def info():
    """
    This is the API info page (JSON formatted response)
    """
    result = InfoModel()
    return InfoSchema().dump(result), 200


@image_api.route('/v1/image', methods=['GET', 'POST', 'DELETE'])
def image():
    """
    This is the API image page (allows GET, POST and DELETE requests for image data)
    """

    # Path to image storage (provisionally a directory and not a database)
    path = 'images/'
    if request.method == 'GET':
        """return the image (if one has already been uploaded)"""
        filenames = os.listdir(path)
        modified_times = collections.defaultdict()
        for f in filenames:
            modified_times[f] = os.path.getmtime(path + f)
        file = max(modified_times, key=modified_times.get)

        return send_file(path + file, mimetype='image/jpeg')

    if request.method == 'POST':
        """Upload an image to the server"""
        if not request.json or 'image' not in request.json:
            return 400

        im_b64 = request.json['image']
        img_bytes = base64.b64decode(im_b64.encode('utf-8'))
        img = Image.open(io.BytesIO(img_bytes))
        img_arr = np.asarray(img)

        # save image
        image_name = hashlib.sha256(img_arr).hexdigest()
        im = Image.fromarray(img_arr)
        width, height = im.size
        size = str(width * height / 1000000) + " MP" # size in MP
        filetype = ".jpg"
        image_path = path + str(image_name) + filetype
        im.save(f"{image_path}")

        result = ImageModel(image_name, filetype, size, img_arr.shape,
                            "The image has been successfully uploaded to the server.")
        return ImageSchema().dump(result), 201

    if request.method == 'DELETE':
        """Delete an image"""
        if not request.json or 'image' not in request.json:
            return 400

        with Image.open(path + request.json['image'] + '.jpg') as im:
            shape = im.size
            filetype = im.format
            size = str(im.width * im.height / 1000000) + " MP"  # size in MP
        for f in glob.glob(path + request.json['image'] + '*'):
            os.remove(f)

        result = ImageModel(request.json['image'], filetype, size, shape, "Image " + request.json['image'] +
                            " has been successfully deleted")
        return ImageSchema().dump(result), 200
    else:
        # POST Error 405 Method Not Allowed
        return 405