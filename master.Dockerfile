FROM ubuntu:14.04
COPY . /master


RUN apt update && apt install -y openssh-server
#EXPOSE 80/tcp
#RUN openssh -


