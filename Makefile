PUBLIC_NAME=laika-public
PUBLIC_IMAGE_NAME=sancahs/$(PUBLIC_NAME):v1

build:
	docker build -f deploy/public/Dockerfile -t $(PUBLIC_IMAGE_NAME) .

runserver:
	docker container rm $(PUBLIC_NAME) --force
	docker run -d -p 8080:8080 --name $(PUBLIC_NAME) $(PUBLIC_IMAGE_NAME)

devserver:
	cd laika && uv run fastapi dev
