# Microservice Deployment - Sneakers Consultation

Tugas Besar II3160 - Teknologi Sistem Terintegrasi

## Create Virtual Environtment

```bash
python -m venv env
```

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install [FastAPI Uvicorn](https://fastapi.tiangolo.com/deployment/manually/)

```bash
pip install fastapi uvicorn
```

## Run Code

```python
uvicorn sneakersconsult:app --reload
```

## Using Docker

Create Dockerfile:

```Docker
# Use the official Python image from the Docker Hub
FROM python:3

# Set the working directory inside the container
ADD <file_name.py> .

# Copy the current directory contents into the container at /app
COPY . /<folder_name>
WORKDIR /<folder_name>

# Install any necessary dependencies
RUN pip install fastapi uvicorn <other packages>

# Command to run the FastAPI server when the container starts
CMD ["uvicorn", "<folder_name>", "--host", "0.0.0.0", "--port", "80"]
```

## Deploy in Microsoft Azure

1. Create [Azure Container Registry Service](https://azure.microsoft.com/en-us/products/container-registry)
2. Open this directory, Login to Azure Server Container Registry using Docker
```Docker
docker login <container_server> -u <container_username> -p <container_password>
```
3. Build Docker Image
```Docker
docker build -t <container_server>/<image_name>:<image_tag> .
```
4. Push Docker Image
```Docker
docker push <container_server>/<image_name>:<image_tag>
```
5. Create [Azure Container Instance](https://azure.microsoft.com/en-us/products/container-instances)


