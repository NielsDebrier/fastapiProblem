FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
MAINTAINER Brainjar "info@brainjar.ai"
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app