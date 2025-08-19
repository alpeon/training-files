#!/bin/sh
set -e

apk update
apk add --no-cache mariadb mariadb-client

mkdir -p /run/mysqld
chown mysql:mysql /run/mysqld

rm -rf /var/lib/mysql/*
mariadb-install-db --user=mysql --basedir=/usr --datadir=/var/lib/mysql
chown -R mysql:mysql /var/lib/mysql

cat > /etc/my.cnf.d/server.cnf <<EOF
[mysqld]
bind-address = 0.0.0.0
datadir = /var/lib/mysql
socket = /run/mysqld/mysqld.sock
pid-file = /run/mysqld/mariadb.pid
EOF

sed -i 's/skip-networking//g' /etc/my.cnf.d/mariadb-server.cnf

rc-service mariadb start

mysql -u root -e 'CREATE USER IF NOT EXISTS "appuser"@"%" IDENTIFIED BY "appassword";'
mysql -u root -e 'CREATE DATABASE app;'
mysql -u root -e 'GRANT ALL PRIVILEGES ON app.* TO 'appuser'@"%";'