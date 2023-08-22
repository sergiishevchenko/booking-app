# Booking App

The main task of the **App** is to search for hotels and book rooms.

## Start project
The uvicorn web server is used to run **FastAPI**. The command to run looks like this:
```
uvicorn app.main:app --reload
```
It must be run on the command line, always being in the root directory of the project.

### Celery & Flower
To start Celery use the command
```
celery --app=app.tasks.celery:celery worker -l INFO -P solo
```
Note that `-P solo` is only used on **Windows**, as **Celery** has problems working on **Windows**.\
To start **Flower** use the command
```
celery --app=app.tasks.celery:celery flower
```

### Dockerfile
To run a web server (**FastAPI**) inside a container, you need to uncomment the code inside the **Dockerfile** and have an already running **PostgreSQL** instance on your machine.\
Command to run **Dockerfile**:
```
docker build .
```
The command is also run from the root directory where the **Dockerfile** resides.

### Docker compose
To start all services (**DB, Redis, Web Server (FastAPI), Celery, Flower, Grafana, Prometheus**), you need to use the **docker-compose.yaml** file and the commands
```
docker compose build
docker compose up
```
Moreover, the `build` command needs to be run only if you changed something inside the **Dockerfile**, that is, you changed the logic for compiling the image.
