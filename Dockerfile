FROM ubuntu:14.04

RUN echo "deb http://mirrors.163.com/ubuntu/ trusty main restricted universe multiverse\n\
deb http://mirrors.163.com/ubuntu/ trusty-security main restricted universe multiverse\n\
deb http://mirrors.163.com/ubuntu/ trusty-updates main restricted universe multiverse\n\
deb http://mirrors.163.com/ubuntu/ trusty-proposed main restricted universe multiverse\n\
deb http://mirrors.163.com/ubuntu/ trusty-backports main restricted universe multiverse\n\
deb-src http://mirrors.163.com/ubuntu/ trusty main restricted universe multiverse\n\
deb-src http://mirrors.163.com/ubuntu/ trusty-security main restricted universe multiverse\n\
deb-src http://mirrors.163.com/ubuntu/ trusty-updates main restricted universe multiverse\n\
deb-src http://mirrors.163.com/ubuntu/ trusty-proposed main restricted universe multiverse\n\
deb-src http://mirrors.163.com/ubuntu/ trusty-backports main restricted universe multiverse\n\
" > /etc/apt/sources.list

RUN apt-get update -y && apt-get install --no-install-recommends -y -q build-essential python2.7 python2.7-dev python-pip git
RUN pip install -U pip
RUN pip install virtualenv