#!/usr/bin/env bash

# Configure and enable service context.

exec 1>&2
set -eux -o pipefail

apt update
apt install python3-pip python3-venv git -y
python3 -m venv .

sync