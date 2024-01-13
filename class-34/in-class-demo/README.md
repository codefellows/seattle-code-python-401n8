# Docker steps:

- must have a `requirements.txt`

1. `Dockerfile` goes in the root of your project
2. `docker-compose.yml` also goes in the root of your project
3. command in your terminal: `$ docker compose up`
4. To stop control c or `docker compose down`

To delete everything:
- docker container stop $(docker container ls -a -q); docker system prune -a -f --volumes

##  Psychopg 2 for PostgreSQL
1. `$ pip install psycopg2-binary`
2. `$ docker compose exec web bash`

## Class 33
- pip install djangorestframework-simplejwt
- pip install gunicorn
- Django Sessions link:
- https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Sessions
- JWT tool
- https://www.jstoolset.com/jwt

## Class 34
- Whitenoise: https://whitenoise.readthedocs.io/en/stable/index.html
- ElephantSQL: https://www.elephantsql.com/
- .env: $ pip install django-environ
- $ python -c "import secrets; print(secrets.token_urlsafe())"
- cors headers: https://pypi.org/project/django-cors-headers/

