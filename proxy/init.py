#!/usr/bin/python

# Flask is used to create a somewhat lightweight listening server
from flask import Flask
from requests import get


def spawn_proxy():
    myproxy = Flask('__name__')

    # Quick health check override
    @myproxy.route('/healthcheck', methods=['GET'])
    def health():
        return "OK"

    # Let's not spam google if we don't get a query, and return a Bad Request.
    @myproxy.route('/', methods=['GET'])
    def empty():
        return "Empty search string", 400

    # This is a very dumb proxy, we're only doing GET.
    @myproxy.route('/<path:req>', methods=['GET'])
    def proxy(req):
        # We're only going to google here, so let's just keep it in the proxy settings for now.
        target = 'https://www.google.com/'
        return get(f'{target}/search?q={req}').content

    return myproxy
