FROM python:3.9-slim
WORKDIR /apps


#COPY . /app
LABEL owner="alma159"
LABEL version="v1.0" 
# may run a py prog to check version in files .

ENV DEFAULT = "index.html"

ENV API = "./api.json"
#USER test
#ARG USER_NAME
#RUN adduser -D ${APP_USER}
#RUN res=$(curl(https://raw.githubusercontent.com/almatsy159/apps/main/api/api.json))
#apk add --no-cache curl=8.0

#COPY --chown=${APP_USER} requirements requirements 
COPY . ./apps

#RUN pip install --upgrade pip
RUN pip install -r apps/requirements.txt


#USER ${APP_USER}:${APP_USER}
EXPOSE 3000


#CMD ["python3","-m-","flask","run","--host=0.0.0.0"]
CMD ["python3","app.py",">>","log.txt"]


# thanks xavki !
