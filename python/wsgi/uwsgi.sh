#!/bin/sh
uwsgi --http :9090 --plugin python2 --wsgi-file app.py
#uwsgi --socket 127.0.0.1:3031 --plugin python2 --wsgi-file /usr/share/nginx/html/app.py --master --processes 4 --threads 2 --stats 127.0.0.1:9191 --uid --gid
