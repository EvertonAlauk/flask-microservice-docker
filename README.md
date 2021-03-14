## A sample micreservice with Flask, SQLAlchemy, Postgres and Docker


### Build the image and create the container:

``` shell
docker-compose up -d --build
```

``` shell
docker-compose exec web python manage.py create_db
```

### With [httpie](https://httpie.io/):

``` shell
http -f POST :5000/user email="user@teste.com"
```

``` json
HTTP/1.1 200 OK
Connection: close
Content-Length: 54
Content-Type: application/json
Date: Sun, 14 Mar 2021 23:38:35 GMT
Server: gunicorn/20.0.4

[
    {
        "active": true,
        "email": "user@teste.com",
        "id": 1
    }
]
```


``` shell
http :5000/user
```

``` json
HTTP/1.1 200 OK
Connection: close
Content-Length: 54
Content-Type: application/json
Date: Sun, 14 Mar 2021 23:39:01 GMT
Server: gunicorn/20.0.4

[
    {
        "active": true,
        "email": "user@teste.com",
        "id": 1
    }
]
```