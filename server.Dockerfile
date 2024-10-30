FROM python 
WORKDIR /server
COPY . /server
RUN pip install -r requirements.txt
ENV SERVEUR = "curl","https://github.com/almatsy159/apps/api/server"
EXPOSE 2044
ENV DEFAULT = "index.html"
CMD ["python3","server.py"]

  
