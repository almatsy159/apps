FROM python:3.10.12
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 2044
ENV DEFAULT = "index.html"
RUN curl(https://github.com/almatsy159/apps/api) >> ./api.json
CMD ["python3","app.py"]
