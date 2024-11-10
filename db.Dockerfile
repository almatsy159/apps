FROM mysql:9.1
COPY . /db

#USER = 'root'
# Set environment variables for the new user
#ENV MYSQL_ROOT_PASSWORD = "pwd"
#ENV MYSQL_USER = USER
#ENV MYSQL_PASSWORD=password
#ENV MYSQL_DATABASE=apps


# Run the following commands to create the new user and grant them the necessary permissions
#RUN mysql -u root -p -e "CREATE USER '$MYSQL_USER'@'%' IDENTIFIED BY '$MYSQL_PASSWORD';"
#RUN mysql -u root -p -e "GRANT ALL PRIVILEGES ON $MYSQL_DATABASE.* TO '$MYSQL_USER'@'%';"
#RUN mysql -u root -p -e "FLUSH PRIVILEGES;"

EXPOSE 3500
#CMD ["mysqld"]



