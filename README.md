# apps
to be complete this project may need github actions.

pull this project and
"docker-compose run master -p"

contain Dockerfile, dockercompose, apps dir, tool dir

this repo is a test to acces all application that i want to get easily (pgm analisys , img tools ...) and contain various environnement for test purpose 
see the note on best practice.
# Ubuntu 
was copied from python mais not be accurate (should be reviewed before build) it is the master.
Need to find paparwork about linux and linux software

# Python
suppose that you have a server.py file and requirements.txt , need to work on the workflow depend on ubunutu !

# Ansible 
  as i want to explore this tools i want to implement it inside a docker that runs my app seem to be a good choice , 
  ansible is flexible and docker is not based on vm. it is designed to Linux for linux , 
  might consider terraform implementation to handle various system . This set up should allow it by runnig this container from terraform.
  
# DB
try implement postgre 
for this project mysql should be fine
