#!/usr/bin/env bash
#
sudo apt-get update -y
sudo apt-get install -y nginx
sudo mkdir -p /data/web_static/releases/test/
sudo echo "HOLA BEBÉ" > /data/web_static/releases/test/index.html
rm /data/web_static/current
ln -s /data/web_static/current /data/web_static/releases/test/
chown -R ubuntu:ubuntu /data/
sudo sed -i '38i \\\tlocation /hbnb_static/ {\n\talias /data/web_static/current/;\n\t}\n'  /etc/nginx/sites-available/default
sudo service nginx start
