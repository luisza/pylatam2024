#!/bin/bash 
 
NAME="pylatam" # Name of the application 
DJANGODIR=/pylatam # Django project directory 
SOCKFILE=/run/gunicorn.sock # we will communicte using this unix socket
NUM_WORKERS=2 # how many worker processes should Gunicorn spawn 
DJANGO_SETTINGS_MODULE=pylatam2024.settings # which settings file should Django use 
DJANGO_WSGI_MODULE=pylatam2024.wsgi # WSGI module name 

USER=pylatam # the user to run as
GROUP=pylatam # the group to run as
 
# Activate the virtual environment 
cd $DJANGODIR 

# Start your Django Unicorn 
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon) 
exec gunicorn ${DJANGO_WSGI_MODULE}:application --name $NAME \
--user=$USER --group=$GROUP \
--workers $NUM_WORKERS \
--bind=unix:$SOCKFILE \
--log-level=info \
--pid="/run/pylatam_`date  +"%Y%m%d%H%M%S"`.pid" \
--log-file=-
