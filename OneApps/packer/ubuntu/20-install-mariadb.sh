#!/usr/bin/env bash

# Configure and enable service context.

exec 1>&2
set -eux -o pipefail

apt update
apt install mariadb-server -y
sed -i 's/^bind-address\s*=.*/bind-address = 0.0.0.0/' /etc/mysql/mariadb.conf.d/50-server.cnf

sync