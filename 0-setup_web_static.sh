#!/usr/bin/env bash
#Sets up your web servers for the deployment of web_static
sudo apt-get update -y
sudo apt-get install -y nginx
sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/
echo "HOLA BEBE" | sudo tee /data/web_static/releases/test/index.html
sudo rm /data/web_static/current
sudo ln -s /data/web_static/current /data/web_static/releases/test/
sudo chown -R ubuntu:ubuntu
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx start
