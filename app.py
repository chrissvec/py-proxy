#!/usr/bin/python

# Flask is used to create a somewhat lightweight listening server
from proxy.init import spawn_proxy

app = spawn_proxy()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
