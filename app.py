#!/usr/bin/python

# Flask is used to create a somewhat lightweight listening server
from proxy.init import spawn_proxy
from logging.config import dictConfig
from gevent.pywsgi import WSGIServer

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '%(asctime)s - %(levelname)s - %(message)s'
    }},
    'handlers': {'stdout': {
        'class': 'logging.StreamHandler',
        'level': 'INFO',
        'stream': 'ext://sys.stdout',
        'formatter': 'default'
    }},
    'waitress': {
        'level': 'INFO',
        'handlers': ['stdout']
    }
})

app = spawn_proxy()

if __name__ == '__main__':
    http_server = WSGIServer(('', 8080), app)
    http_server.serve_forever()
