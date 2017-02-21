#!/bin/bash

## Téléchargement des données

wget $HOME/NoSQLTheoVleeschouwers https://data.cityofnewyork.us/api/views/j8gx-kc43/rows.json
cd $HOME/NoSQLTheoVleeschouwers 
mv rows.json farmermarket.json

wget $HOME/NoSQLTheoVleeschouwers https://data.cityofnewyork.us/api/views/xszr-btpb/rows.json
mv rows.json estores.json

## Installation Logiciel Python
sudo apt-get install spyder

## Installation Mongo
# Importation Clé Publique
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6

# Creation liste fichier Mongo
echo "deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list

# Rechargement package database
sudo apt-get update

# Installation mongodb

sudo apt-get install -y mongodb-org

sudo service mongod start