#!/bin/bash
export TNS_ADMIN=$HOME/Documents/secrets
export LD_LIBRARY_PATH=/opt/oracle/instantclient_21_10:$LD_LIBRARY_PATH
echo "Environment setted!"
python manage.py runserver
