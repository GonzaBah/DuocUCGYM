#!/bin/bash
export TNS_ADMIN=$HOME/Documentos/secrets
export LD_LIBRARY_PATH=/opt/oracle/instantclient_21_10:$LD_LIBRARY_PATH
echo "Environment setted!"
python3 manage.py runserver
