#!/usr/bin/env python3
import socketserver
import http.server
import ssl

httpd = socketserver.TCPServer(('0.0.0.0', 2211), http.server.SimpleHTTPRequestHandler)

httpd.socket = ssl.wrap_socket(httpd.socket, certificate='/home/server.pem', key='/home/server.key', server_side=True)

httpd.server_forever()
