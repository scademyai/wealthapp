.PHONY: start stop restart build test test-frontend test-backend sh tsh shf tshf logs config psql tpsql migrate tmigrate rollback trollback

# \
!ifndef 0 # \
test_env_setting="DATABASE_URL=$$TEST_DATABASE_URL" # \
!else
test_env_setting=DATABASE_URL=\$$TEST_DATABASE_URL
# \
!endif

container_backend=wealthapp-backend
container_frontend=wealthapp-frontend

# start all the containers
start:
	docker compose up -d

# start the frontend container
start-frontend:
	docker compose up -d $(container_frontend)

# start the backend container
start-backend:
	docker compose up -d $(container_backend)
	
# stop all the containers
stop:
	docker compose down

# restart containers
restart: stop start

# build the app container
build:
	docker compose build

build-backend:
	docker compose build $(container_backend) --no-cache

build-frontend:
	docker compose build $(container_frontend) --no-cache

# run tests
test: test-frontend test-backend

test-frontend:
	docker compose exec -T $(container_frontend) /bin/sh -c "yarn test"

test-backend:
	docker compose exec -T $(container_backend) /bin/sh -c "$(test_env_setting) source .venv/bin/activate && python -m nose2 -v"

# get a shell within the app container
sh:
	docker compose exec $(container_backend) /bin/sh

tsh:
	docker compose exec $(container_backend) /bin/sh -c "$(test_env_setting) sh"

shf:
	docker compose exec $(container_frontend) /bin/sh

tshf:
	docker compose exec $(container_frontend) /bin/sh -c "$(test_env_setting) sh"

# check console output
logs:
	docker compose logs -f

# show the combined compose file used
config:
	docker compose config

# console to the DB
psql:
	docker compose exec postgres psql -U app_dev dev

tpsql:
	docker compose exec postgres psql -U app_test test

# run all migrations
migrate:
	docker compose exec $(container_backend) /bin/sh -c "source .venv/bin/activate && alembic upgrade head"

tmigrate:
	docker compose exec $(container_backend) /bin/sh -c "$(test_env_setting) source .venv/bin/activate && alembic upgrade head"

rollback:
	docker compose exec $(container_backend) /bin/sh -c "source .venv/bin/activate && alembic downgrade -1"

trollback:
	docker compose exec $(container_backend) /bin/sh -c "$(test_env_setting) source .venv/bin/activate&& alembic downgrade -1"
