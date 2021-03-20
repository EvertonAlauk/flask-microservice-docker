# Internet Banking

- Flask
- SQLAlchemy
- Flask-Migrate
- Postgres
- Gunicorn
- PyJWT
- Docker & docker-compose

### Build the image and create the container:

``` shell
docker-compose up -d --build
```

### With [httpie](https://httpie.io/):

## User

``` shell
http -f POST :5001/user username="user" email="user@teste.com" password="password123" name="user"
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
        "username": "user"
    }
]
```

## Create a JWT to run private endpoints

``` shell
http -f POST :5001/auth -a user:password123
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
    "token": "token"
}
```

## Bank Account

> Credit

``` shell
http -f POST :5002/credit credit="2.6" 'Authorization: Bearer {token}'
```

``` json
HTTP/1.1 200 OK
Connection: close
Content-Length: 38
Content-Type: application/json
Date: Sat, 20 Mar 2021 22:33:03 GMT
Server: gunicorn/20.0.4

{
    "credit": 2.6,
    "id": 1,
    "user_id": 1
}
```