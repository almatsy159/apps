# Docker
docker --help
docker run --help
docker run -it ubuntu bash (it interactif => cl)

docker ps
docker stop ubuntu
docker start ubuntu 
docker rm id 

0 install docker
1 making a dir for docker app
2 moving toward dir : cd docker_dir
3 creating file app.py and requirement.txt
4 install venv
5 creating and activating venv 
6 python -m pip install flask
7 app.py
    @app('route/<var>')
8 flask run to test and check
prod et dev flask !! if __name__ bloc
security 
9 CREATE Dockerfile
    FROM python:3.10.12
    WORKDIR /app
    COPY . /app
    RUN pip install -r requirements.txt
    EXPOSE 1024
    ENV NOM ALMA

    CMD ["python3","app.py"]

10 docker build -t secondimg .
11 docker run -p 1024:1024 secondimg .
12 docker-compose.yml
    version:"3"
    service: 
        my_app:
            image: secondimg
        depends_on:
            - redis
        ports:
            - 1024:1024
        networks:
            - monreseau
    redis:
        image: redis
        ports: 
            -"6379:6379"
        networks : monreseau
    networks:
        - monreseau
13 docker run -it secondimg bash
14 docker-compose 