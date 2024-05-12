FROM python:3.11.9-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ENV PORT 8000

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir -r /code/requirements.txt

COPY ./app /code/app

CMD exec gunicorn --bind :$PORT -k uvicorn.workers.UvicornWorker --workers 1 --threads 8 --timeout 0 app.main:app
