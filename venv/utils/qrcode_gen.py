from flask import Flask, json
import requests
import logging
import jinja2
import qrcode
import os, sys
import imgurpython
from datetime import datetime
from imgurpython import ImgurClient
# from jinja2 import FileSystemLoader, Environment

app = Flask(__name__)


@app.route("/")
def index():
    return "Welcome to API Library"


@app.route('/tx/<inputText>', methods=['GET'])
def gen_tx_qrcode(inputText):

    img = qrcode.make(inputText)
    img.save('qrcode.png')

    album = None
    image_path = 'qrcode.png'
    clientId = 'xxxxxxxx' # Please get your own ClientId from imgur

    url = "https://api.imgur.com/3/image"
    payload = {'image': open(image_path, 'rb').read(), 'type': 'file'}
    headers = {'authorization': 'Client-ID ' + clientId}  # notice the space after Client-ID, concat

    response = requests.request("POST", url, data=payload, headers=headers) # post image anonymously to imgur

    # return json.dumps(response.text)

    temp_obj = json.loads(response.text) # json encode response again since it's a string
    responseURL = temp_obj["data"]["link"]

    return responseURL

@app.route('/raw/<inputText>', methods=['GET'])
def gen_raw_qrcode(inputText):
    # return inputText

    img = qrcode.make(inputText)
    img.save('qrcode.png')
    # image = 'qrcode.png'

    album = None
    image_path = 'qrcode.png'
    clientId = 'F5a0da0ee22b6b9'

    url = "https://api.imgur.com/3/image"
    payload = {'image': open(image_path, 'rb').read(), 'type': 'file'}
    headers = {'authorization': 'Client-ID ' + clientId}  # notice the space after Client-ID, concat

    response = requests.request("POST", url, data=payload, headers=headers) # post image anonymously to imgur

    return json.dumps(response.text, sort_keys=True, indent=4, separators=(',', ': '))


if __name__ == '__main__':
    app.run(debug=True)



