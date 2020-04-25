# coding:utf-8
"""
  PYTHON

  Synchro
    serveurs http
  """

import http.server
import socketserver

port = 80
address = ("", port)

handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(address, handler)

print(f"connexion au port {port}")

httpd.serve_forever()
