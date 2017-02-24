# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# NOTE: DO *NOT* EDIT THIS FILE.  IT IS GENERATED.
# PLEASE UPDATE Dockerfile.txt INSTEAD OF THIS FILE
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
FROM selenium/node-chrome:3.0.1-carbon
MAINTAINER Selenium <qpenguin25@gmail.com>

USER root

#====================================
# Scripts to run Selenium Standalone
#====================================
COPY entry_point.sh /opt/bin/entry_point.sh
RUN chmod +x /opt/bin/entry_point.sh

#====================================
## Install python2.7.12
##====================================

RUN mv /var/lib/dpkg/info /var/lib/dpkg/info.bak
RUN mkdir /var/lib/dpkg/info

RUN apt-get update   -y
RUN apt-get upgrade -y 
RUN apt-get install -y    build-essential 
RUN apt-get install -y    ca-certificates 
RUN apt-get install -y    gcc 
RUN apt-get install -y    git 
RUN apt-get install -y    libpq-dev 
RUN apt-get install -y    make 
RUN apt-get install -y    python-pip 
RUN apt-get install -y    python2.7 
RUN apt-get install -y    python2.7-dev 
RUN sudo apt-get install -y python-pip
RUN sudo pip install selenium
RUN sudo pip install --upgrade pip
RUN pip install BeautifulSoup
RUN pip install bs4
RUN pip install requests

USER seluser

EXPOSE 4444

