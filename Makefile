setup:
	@pip install -r requirements.txt

run:
	@fastapi dev

build:
	@docker build -t doacoesrs-be .

up:
	@docker run --rm --name doacoesrs-be doacoesrs-be

test:
	@pytest

deploy:
	@gcloud run deploy --source .
