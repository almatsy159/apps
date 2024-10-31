# Docker

## good practice 

0. Don't use latest v 

        docker manifest inspect image @sha256 or -tag
1. use slimest verison possible
2. delete cache after apt pip (pip no cache ...)
3. group layer ? && \
4. dockerignore
5. create default user (cmd entry$) (switch user)
6. versionning of install
7. check from
8. think about who and where you push
9. avoid monolith (proxy extern ...)
10. linter ?
11. clause arg !!! (version ...)
12. avoid debug tools ?
13. normalize label
14. scan vulnaribilty (clair falco)
15. avoid . .
16. define workdir
17. multi stage build (to check) 
18. maintain image 

        docker --help
        docker run --help
        docker run -it ubuntu bash (it interactif => cl)

        docker ps
        docker stop ubuntu
        docker start ubuntu 
        docker rm id 


## let's get into it 

0. install docker
1. making a dir for docker app
2. moving toward dir : cd docker_dir
3. creating file app.py and requirement.txt
4. install venv
5. creating and activating venv 
6. python -m pip install flask
7. app.py

    @app('route/<var>')

8. flask run to test and check

prod et dev flask !! if __name__ bloc
security 

9. CREATE Dockerfile

        FROM python:3.10.12-alpine
        WORKDIR /app
        COPY . /app
        RUN pip install -r requirements.txt
        EXPOSE 1024
        ENV NOM ALMA

        CMD ["python3","app.py"]

10. docker build -t secondimg .
11. docker run -p 1024:1024 secondimg . 
12. docker-compose.yml

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

13. docker run -it secondimg bash
14. docker-compose 