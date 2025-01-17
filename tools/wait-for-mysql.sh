#!/bin/sh

# Modified from: https://cweiske.de/tagebuch/docker-mysql-available.htm

# wait until MySQL is really available
maxcounter=45
 
counter=1
while ! mysql -u"$DB_USER" -p"$DB_PASSWORD" -h"$DB_HOST" --execute="show databases;"

do
    echo "Waiting for Mysql..."
    sleep 1
    counter=`expr $counter + 1`
    if [ $counter -gt $maxcounter ]; then
        >&2 echo "We have been waiting for MySQL too long already; failing."
        exit 1
    fi;
done
