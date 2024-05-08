FROM python:3.11.9-slim-bookworm

ENV PORT=8000

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port $PORT"]
