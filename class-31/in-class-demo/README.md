# Docker steps:

- must have a `requirements.txt`

1. `Dockerfile` goes in the root of your project
2. `docker-compose.yml` also goes in the root of your project
3. command in your terminal: `$ docker compose up`
4. To stop control c or `docker compose down`

To delete everything:
- docker container stop $(docker container ls -a -q); docker system prune -a -f --volumes
