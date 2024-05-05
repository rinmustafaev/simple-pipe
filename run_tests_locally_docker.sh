docker-compose -f infra/docker-compose.yml down -v
#if you need to rebuild the image
#docker-compose -f infra/docker-compose.yml up --build --force-recreate

docker-compose -f infra/docker-compose.yml up --abort-on-container-exit
docker-compose -f infra/docker-compose.yml down