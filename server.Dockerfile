FROM ubuntu:20.04

#WORKDIR 
RUN apt update && apt install -y openssh-server

RUN mkdir /var/run/sshd
RUN echo "test:ansible" | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin res/' /etc/ssh/sshd_config
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in user profile"

RUN echo "export VISIBLE=now" >> /etc/profile

EXPOSE 22 
CMD ["/usr/sbin/sshd","-D"]
#FROM python 


#WORKDIR /server
#COPY . /server
#RUN pip install -r requirements.txt
#ENV SERVEUR = "curl","https://github.com/almatsy159/apps/api/server"
#EXPOSE 2044
#ENV DEFAULT = "index.html"
#CMD ["python3","server.py"]

