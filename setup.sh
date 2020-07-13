#!/bin/bash
#https://github.com/volatilityfoundation/volatility/issues/535

##if errors, install mongodb3.6
wget -qO - https://www.mongodb.org/static/pgp/server-3.6.asc | sudo apt-key add -

echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.6 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.6.list

apt update

apt install -y python3 python3-pip mongodb json tcpxtract

pip3 install -r requirements.txt

python manage.py migrate
