FROM python:3.9

RUN mkdir /booking

WORKDIR /booking

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

# COMMENT BELOW IS FOR DOCKER COMPOSE ONLY. UNCOMMENT THE CODE IF YOU USE ONLY DOCKERFILE
# Gives access to the container to run a bash script if needed
# It is impossible to run bash scripts without access to them on Linux OS. On Windows, perhaps
# but since containers run on Linux, you have to grant access regardless of your OS.
# RUN chmod a+x /booking/docker/*.sh

# COMMENT BELOW IS FOR DOCKER COMPOSE ONLY. UNCOMMENT THE CODE IF YOU USE ONLY DOCKERFILE
# This command is output to bash script
# RUN alembic upgrade head

# COMMENT BELOW IS FOR DOCKER COMPOSE ONLY. UNCOMMENT THE CODE IF YOU USE ONLY DOCKERFILE
# This command is in the bash script
# CMD ["gunicorn", "app.main:app", "--workers", "1", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind=0.0.0.0:8000"]