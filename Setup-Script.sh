#!/bin/sh
# Script to build a Raspi-Zero up from lite image to usable for loop-tuner
# currently running on 0.64 pi-zero
# sudo apt-get install git
#git clone http://192.168.0.12:8668/git/jhagerman/SatTracker-pi.git
#git clone https://github.com/merlinscomputing/loop-tuner-pi.git
#cd ~/loop-tuner-pi
#sudo chmod +x Setup-Script.sh 
#./Setup-Script.sh

sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev -y
sudo apt-get install libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev -y
sudo apt-get install python3-pip -y
sudo apt-get install apache2 php -y
#sudo apt-get install python-smbus i2c-tools -y

cd /home/jhagerman
#wget https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tar.xz
#wget https://www.python.org/ftp/python/3.9.0/Python-3.9.7.tar.xz
#tar xf Python-3.9.7.tar.xz
#cd Python-3.9.0
#./configure
#make 
#sudo make altinstall
# for now we are going to use the default python 3.7 distribution with raspi os. will try newer python later

#cd /home/jhagerman
#wget https://files.pythonhosted.org/packages/ba/60/59844a5cef2428cb752bd4f446b72095b1edee404a58c27e87cd12a141e2/websockets-7.0.tar.gz
#sudo python3 -m pip install websockets-7.0.tar.gz
sudo python3 -m pip install websockets
#sudo python3 -m pip install python-smbus

#sudo pip install RPi.GPIO
#cd /home/jhagerman
#git clone https://github.com/adafruit/Adafruit_Python_SSD1306.git
#cd Adafruit_Python_SSD1306
#sudo python setup.py install

sudo python3 -m pip install rpi.gpio

#cd /home/jhagerman/TC-IFC
#cp stats-jjh.py /home/jhagerman/Adafruit_Python_SSD1306/examples/stats-jjh.py

sudo chown -R www-data /var/www
sudo chgrp -R www-data /var/www
sudo chmod 775 /var/www/html
cd /var/www/html 
ln ~/SatTracker-pi/SatTracker.html SatTracker.html
cd

#cp -r ~/TC-IFC/TC-IFC-PHP /var/www/html/
#sudo chmod 777 /var/www/html/TC-IFC-PHP/TC-IFC-PY.log

git config --global user.email merlin@merlinscomputing.net
git config --global user.name jhagerman
