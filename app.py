#!/usr/bin/python

# Flask is used to create a somewhat lightweight listening server
from flask import Flask
from requests import get


class Proxy:
    proxy = Flask(__name__)


# This is a very dumb proxy, we're only doing GET.
    @proxy.route('/<path:req>', methods=['GET'])
    def proxy(req):
        # We're only going to google here, so let's just keep it in the proxy settings for now.
        target = 'https://www.google.com/'
        return get(f'{target}/?q={req}').content

    proxy.run(host='0.0.0.0', port=8080)


Proxy()
