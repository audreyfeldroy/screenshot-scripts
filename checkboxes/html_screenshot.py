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

def serve_one_request():
	"""
		Start up a simple web server serving files in the current directory, 
		handle 1 request, and shut down again. 
	"""
	handler = SimpleHTTPServer.SimpleHTTPRequestHandler
	httpd = SocketServer.TCPServer(("", 8010), handler)
	httpd.handle_request()

# Start webserver in new thread
t = threading.Thread(target=serve_one_request)
t.daemon = True
t.start()

# Use Ghost to open HTML page
ghost = Ghost()
page, extra_resources = ghost.open("http://127.0.0.1:8010/simple_form.html")

# Capture a screenshot when the HTML page is ready
ghost.wait_for_selector('button')
ghost.capture_to('simple_form.png', zoom_factor=3.0)
