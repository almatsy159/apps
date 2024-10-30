ENV UBUNTU_V 24.4

FROM UBUNTU:${ENV}

WORKDIR /master
COPY . /master
#RUN pip install -r requirements.txt
#EXPOSE 80/tcp
ENV DEFAULT = "index.html"

