#!/bin/bash
cp *.py /var/www/FlaskApp/FlaskApp
cp *.csv /var/www/FlaskApp/FlaskApp

systemctl reload apache2