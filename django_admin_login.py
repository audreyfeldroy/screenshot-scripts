#!/usr/bin/env python

"""
Takes a 3x-zoomed screenshot of the Django admin login box.

Setup:
1. pip install Ghost.py
2. pip install Pillow
2. Start up Django runserver for a Django project, with admin at admin/

Usage:
python django_admin_login.py <username> <password>
(where the username and password are entered into the corresponding boxes)
"""
import sys

from ghost import Ghost
import Image

username = sys.argv[1]
password = sys.argv[2]
django_admin_url = "http://127.0.0.1:8000/admin/"
image_file = "django_admin_login.png"

ghost = Ghost()
page, extra_resources = ghost.open(django_admin_url)

ghost.wait_for_selector('#id_username')
ghost.wait_for_selector('#id_password')
ghost.fill("#login-form", {'username': username, 'password': password})

ghost.capture_to(image_file, zoom_factor=3.0)
print "Captured django_admin_login.png"

# Crop bad space at the top due to the odd page layout
im = Image.open(image_file)
box = (0, 300, 1014, 1062)
region = im.crop(box)
region.save(image_file)
