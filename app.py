#!/usr/bin/python

# Flask is used to create a somewhat lightweight listening server
from flask import Flask
from requests import get


myproxy = Flask('__name__')


class Proxy:

    # Quick health check override
    @myproxy.route('/healthcheck', methods=['GET'])
    def health(self):
        return "OK"

    # This is a very dumb proxy, we're only doing GET.
    @myproxy.route('/<path:req>', methods=['GET'])
    def proxy(req):
        # We're only going to google here, so let's just keep it in the proxy settings for now.
        target = 'https://www.google.com/'
        return get(f'{target}/search?q={req}').content

    myproxy.run(host='0.0.0.0', port=8080)


Proxy()