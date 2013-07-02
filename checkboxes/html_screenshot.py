#!/usr/bin/python
"""
Takes a 3x-zoomed screenshot of an HTML file in the same directory
(in this case simple_form.html)

Setup:
1. pip install Ghost.py

Usage:
python html_screenshot.py
"""

import SimpleHTTPServer
import SocketServer
import threading

from ghost import Ghost

def start_server():
	""" Start up server to handle 1 request """
	handler = SimpleHTTPServer.SimpleHTTPRequestHandler
	httpd = SocketServer.TCPServer(("", 8010), handler)
	httpd.handle_request()

t = threading.Thread(target=start_server)
t.daemon = True
t.start()

ghost = Ghost()
page, extra_resources = ghost.open("http://127.0.0.1:8010/simple_form.html")

ghost.wait_for_selector('button')
ghost.capture_to('simple_form.png', zoom_factor=3.0)
