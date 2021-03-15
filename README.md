## A sample microservice with Flask, SQLAlchemy, Postgres and Docker


### Build the image and create the container:

``` shell
docker-compose up -d --build
```

``` shell
docker-compose exec web python manage.py create_db
```

### With [httpie](https://httpie.io/):

``` shell
http -f POST :5000/user username="user" email="user@teste.com" password="password123" name="user"
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
        "created": "2021-03-15T00:08:14.180200",
        "email": "user@teste.com",
        "id": 1,
        "name": "user",
        "password": "pbkdf2:sha256:150000$bPfNRntx$a8adcecc568ca2a76f1f40a51040d45d54161f794232d764a373987a62e5837e",
        "username": "user"
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
        "created": "2021-03-15T00:08:14.180200",
        "email": "user@teste.com",
        "id": 1,
        "name": "user",
        "password": "pbkdf2:sha256:150000$bPfNRntx$a8adcecc568ca2a76f1f40a51040d45d54161f794232d764a373987a62e5837e",
        "username": "user"
    }
]
```

## Create a JWT to run private endpoints

``` shell
http -f POST :5000/auth -a user:password123
```


``` json
HTTP/1.1 200 OK
Connection: close
Content-Length: 54
Content-Type: application/json
Date: Sun, 14 Mar 2021 23:39:01 GMT
Server: gunicorn/20.0.4

{
    "expired": 1615813569.092066,
    "message": "Auth validated.",
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InVzZXIiLCJleHBpcmVkIjoxNjE1ODEzNTY5LjA5MjA2Nn0.1Y0P40QycZs6HpdkYSp3d2ZKArJLjGELno1vmkqb44U"
}
```