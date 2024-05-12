setup:
	@pip install -r requirements.txt

run:
	@fastapi dev

build:
	@docker build -t doacoesrs-be .

up:
	@docker run --rm --name doacoesrs-be -p 8000:8000 --env-file .env --cpus 0.5 --memory 256mb doacoesrs-be

test:
	@pytest

deploy:
	@gcloud run deploy --source .
