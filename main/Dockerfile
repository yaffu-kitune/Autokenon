FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9-slim

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r  requirements.txt

WORKDIR /opt/app

COPY ./app /app
