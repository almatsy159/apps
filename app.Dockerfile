FROM python:3.10.12:alpine3.17
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 2044
ENV DEFAULT = "index.html"
ENV API = "./api.json"
RUN curl(https://raw.githubusercontent.com/almatsy159/apps/main/api/api.json) >> ${API}
CMD ["python3","app.py"]
