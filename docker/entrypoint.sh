#!/bin/bash

cd /pylatam

mkdir -p /run/logs/
chown -R pylatam:pylatam /pylatam
runuser -p  -c "python manage.py migrate" pylatam
runuser -p  -c "python manage.py createcachetable" pylatam


python /pylatam/nginx_personalize.py
supervisord -c /etc/supervisor/conf.d/supervisord.conf -n

