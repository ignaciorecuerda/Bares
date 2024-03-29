FROM ubuntu:latest

#Autor
MAINTAINER Antonio Miguel Pozo Cámara <antoniopozo26@gmail.com>

#Actualizar Sistema Base
RUN sudo apt-get -y update

#Descargar app
RUN sudo apt-get install -y git
RUN git clone https://github.com/AntonioPozo/Bares.git

#Instalar python
RUN sudo apt-get install -y python-setuptools
RUN sudo apt-get -y build-dep python-imaging --fix-missing
RUN sudo apt-get -y install libffi-dev
RUN sudo apt-get -y install python-dev
RUN sudo apt-get -y install build-essential
RUN sudo apt-get -y install python-psycopg2
RUN sudo apt-get -y install libpq-dev
RUN sudo apt-get -y install python2.7
RUN sudo easy_install pip
RUN sudo easy_install Pillow
RUN sudo pip install --upgrade pip

#Instalar app
RUN sudo apt-get update
RUN	sudo apt-get install -y python-dev
RUN	sudo apt-get install -y python-pip
RUN	sudo pip install --upgrade pip
RUN	cd Bares && sudo pip install -r requirements.txt
