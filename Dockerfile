FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9-slim

RUN pip install --upgrade pip
RUN pip install selenium

COPY ./app /app