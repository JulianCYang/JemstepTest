# JemstepTest
Create a sample docker compose file by following a simple getting started tutorial... and list steps here (and also the compose file)

1.1) Install the Docker (Prerequisite with the assumption that you are using Ubuntu):

 [Install Docker](`https://docs.docker.com/install/linux/docker-ce/ubuntu/`)

1.2) Uninstall  old version: 

`sudo apt-get remove docker docker-engine docker.io containerd runc`

1.3)Setting up the repository:

 `sudo apt-get update`  

`sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common`

`curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -`

`sudo apt-key fingerprint 0EBFCD88`

`sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"`



1.4) Actual installation:

 `sudo apt-get update`

`sudo apt-get install docker-ce docker-ce-cli containerd.io`

`sudo docker run hello-world` (Verifies if the Docker CE has been installed correctly)

2.1) Getting started with Docker Compose

[Docker Compose](`https://docs.docker.com/compose/gettingstarted/`)

2.2) Setup:

Create a directory for the project:

`mkdir composetest`

`cd composetest`


Create a file called app.py containing the following

```python
import time

import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)
```

Create another file called requirements.txt containing the following

```
flask
redis
```

2.3) Create a file named Dockerfile containing the following

```
FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["flask", "run"]
```

2.4)Create a file called docker-compose.yml containing the following

```
version: '3'
services:
  web:
    build: .
    ports:
      - "5000:5000"
  redis:
    image: "redis:alpine"
```

2.5) Start the application with the following line

`docker-compose up`

2.6) Enter http://localhost:5000/ in a browser to see the application running, it should return 

```
Hello World! I have been seen 1 times.
```

the number should increment as you refresh the page.

2.7) Edit the compose file to add a [bind mount](https://docs.docker.com/storage/bind-mounts/) 

```
version: '3'
services:
  web:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - .:/code
    environment:
      FLASK_ENV: development
  redis:
    image: "redis:alpine"
```

2.8) Re-build and run the app with Compose with the above command.

Note: Update the application when other changes are made.

