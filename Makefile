PUBLIC_NAME=laika-public
PUBLIC_IMAGE_NAME=sancahs/$(PUBLIC_NAME):v1

build:
	docker build -f deploy/public/Dockerfile -t $(PUBLIC_IMAGE_NAME) .

runserver:
	docker container rm $(PUBLIC_NAME) --force
	docker run -d -p 8080:8080 --name $(PUBLIC_NAME) $(PUBLIC_IMAGE_NAME)

rundb:
	docker container rm laika_psql --force
	docker run \
		--rm \
		--name laika_psql \
		-e POSTGRES_USER=laika \
		-e POSTGRES_PASSWORD=laika123 \
		-e POSTGRES_DB=laika \
		-p 5433:5432 \
		-d postgres \

makemigrations:
	cd src && uv run alembic revision --autogenerate

runmigrations:
	cd src && uv run alembic upgrade head

devserver:
	cd src/laika && uv run fastapi dev

test:
	uv run pytest -v
