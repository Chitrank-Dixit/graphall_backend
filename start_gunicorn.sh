#!/bin/bash

NAME="graphall"                                  # Name of the application
DJANGODIR=/home/ubuntu/$NAME/             # Django project directory
SOCKFILE=/home/ubuntu/$NAME/run/gunicorn.sock  # we will communicte using this unix socket
#USER=hello                                        # the user to run as
#GROUP=webapps                                     # the group to run as
NUM_WORKERS=3                                     # how many worker processes should Gunicorn spawn
ADDRESS=127.0.0.1:8000
DJANGO_SETTINGS_MODULE=graphall.settings             # which settings file should Django use
DJANGO_WSGI_MODULE=graphall.wsgi                     # WSGI module name

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
#cd $DJANGODIR
source ~/.bashrc
workon graphall
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec ../bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS\
  --bind=$ADDRESS \
  --log-level=debug \
  --log-file=-
