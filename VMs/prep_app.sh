#!/bin/bash

apk add python3 py3-pip git
python3 -m venv .
source bin/activate
mkdir app
git clone https://github.com/alpeon/test-app.git app
cd app
pip install -r requirements.txt