import base64
import json

import requests


# change accordingly (default version runs on localhost)
FLASK_IP = '127.0.0.1'
FLASK_PORT = '5000'


def post_image():
    # POST API request

    with open("images/sample_image.jpg", "rb") as f:
        im_bytes = f.read()
    im_b64 = base64.b64encode(im_bytes).decode("utf8")
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    payload = json.dumps({"image": im_b64})
    response = requests.post('http://' + FLASK_IP + ':' + FLASK_PORT + '/api/v1/image', data=payload, headers=headers)
    try:
        data = response.json()
        print(data)
    except requests.exceptions.RequestException:
        print(response.text)
    print("POST request sent")


def delete_image():
    # DELETE API request

    headers = {'content-type': 'application/json'}
    payload = json.dumps({'image': '344c55b90f6c07d6518578a3959db3df8873b462314f9cc1e06b2fc55a9ae2d1'})
    response = requests.delete('http://' + FLASK_IP + ':' + FLASK_PORT + '/api/v1/image', data=payload, headers=headers)
    try:
        data = response.json()
        print(data)
    except requests.exceptions.RequestException:
        print(response.text)
    print("DELETE request sent")


def main():
    post_image()


if __name__ == '__main__':
    main()

