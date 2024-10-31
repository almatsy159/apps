FROM ansible/ansible:ubuntu1404

COPY . /master

RUN apt update && apt install -y openssh-server
#EXPOSE 80/tcp

