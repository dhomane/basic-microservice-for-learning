[![pipeline status](https://gitlab.com/keiran.steele/basic-microservice-for-learning/badges/Development/pipeline.svg)](https://gitlab.com/keiran.steele/basic-microservice-for-learning/commits/Development)

# Basic Microservice for Learning

## Description

Basic Microservice currently written in Python using flask. Provides a functional, easy to understand and lightweight microservice intended for learning Python, Docker, Kubernetes and Microservices in general.

The calculator service calls the random_num service to generate a random number from 1 to 100. The calculator then adds the random number to itself and then posts the original number and the result to the database service which stores them in a SQLite database.

## Usage

1. Ensure docker is installed.

2. Clone the project file.

3. Build the docker images for each of the 3 services using the commands below.

```bash
cd basic_microservice
cd services/calculator
docker build -t calculator .

cd services/database
docker build -t database .

cd services/random_num
docker build -t random_num .
```

4. Run docker compose to bring up the images and expose the calculator service.
This first command is good for seeing the output from each docker container as it won't detach from the container after creation which is handy for seeing what is going on.
To detach from the images when you run docker compose, add the "-d" flag.
```bash
docker-compose up
```

5. Test the app by browsing to http://host-ip:7501/calc in your browser which will show the original number, the original number added to itself and the database response code the post to the database.

Expected reponse:

```json
{
  "db_response": 200, 
  "input": 77, 
  "output": 154
}
```

## Development

A Vagrantfile is provided to assist with development. Running the Vagrantfile will configure an Ubuntu 16.04 VM with docker and docker compose, the services will be built and run from their respective Dockerfiles. Browsing to http://localhost:7501/calc will confirm the services are running. Project files will be mounted into /vagrant, changing them on the host will change them in the VM allowing quick testing and feedback on changes.

Tested with Vagrant 2.2.3 and Virtualbox 6.0.4

1. Clone the project files onto the host

```bash
git clone https://gitlab.com/keiran.steele/basic-microservice-for-learning.git
```

2. Change directory into the project and run the Vagrantfile

```bash
cd basic-microservice-for-learning
vagrant up
```

3. Back on the host, browse to http://localhost:7501/calc in your browser or do a curl from your terminal.

```bash
curl http://localhost:7501/calc
```

4. Make changes to the services on the host as required.

5. Reprovision the Vagrant environment or ssh onto the Vagrant VM and rebuild the docker-compose 

Rebuild docker-compose.yaml
```bash
vagrant ssh
cd /vagrant
sudo docker-compose build
```

Reprovision the Vagrant environment from the host
```bash
vagrant reload --provision
```

6. Destroy the Vagrant VM when no longer required. Changes you have made on the host to your source files will persist and you can recreate the Vagrant environment as required.

```bash
vagrant destroy
```