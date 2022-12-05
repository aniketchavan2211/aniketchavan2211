#!/usr/bin/env python3

# on Command-line
# python3 -m http.server <port> --bind=127.0.0.1
# python-version3 -m <module-name> <port-number>

import socketserver
import http.server

httpd = socketserver.TCPServer(('0.0.0.0', 2211), http.server.SimpleHTTPRequestHandler)

httpd.serve_forever()
