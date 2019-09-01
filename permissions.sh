#!/bin/bash
#chown www-data:www-data /var/www/html/ -R
nohup python3 /devportfolio/devfolio/manage.py runserver 0.0.0.0:8000 &
