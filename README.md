# Internet Banking

## Requirements

- Flask
- SQLAlchemy
- Flask-Migrate
- Postgres
- Gunicorn
- PyJWT
- Docker & docker-compose

## Sumary

- [API User](#api-user)
- [API Auth with JWT](#api-auth)
- [API Bank Account Balance](#api-balance)
- [API Bank Account Credit](#api-credit)
- [API Bank Account Debit](#api-debit)
- [API Bank Account Statement](#api-statement)

## Build the image and create the container

``` shell
docker-compose up --build
```

At now, will created two microservices and both have your own port.
User have the `:5001` and bank account thave the `:5002` port connection.

## With [httpie](https://httpie.io/):

### User <a name="api-user">

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

### Auth JWT <a name="api-auth">

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

### Bank Account: Balance <a name="api-balance">

It's important, just one time, to include a balance for user.
In this case, use the POST method.

``` shell
http -f POST :5002/balance value="2500.00" 'Authorization: Bearer {token}'
```

``` json
HTTP/1.1 200 OK
Connection: close
Content-Length: 40
Content-Type: application/json
Date: Sun, 21 Mar 2021 13:58:50 GMT
Server: gunicorn/20.0.4

{
    "id": 1,
    "user_id": 1,
    "value": 2500.0
}
```

Otherwise, GET method for check the balance.

``` shell
http :5002/balance 'Authorization: Bearer {token}'
```

``` json
HTTP/1.1 200 OK
Connection: close
Content-Length: 40
Content-Type: application/json
Date: Sun, 21 Mar 2021 13:58:50 GMT
Server: gunicorn/20.0.4

{
    "id": 1,
    "user_id": 1,
    "value": 2500.0
}
```

### Bank Account: Credit <a name="api-credit">

``` shell
http -f POST :5002/credit value="2.6" 'Authorization: Bearer {token}'
```

``` json
HTTP/1.1 200 OK
Connection: close
Content-Length: 38
Content-Type: application/json
Date: Sat, 20 Mar 2021 22:33:03 GMT
Server: gunicorn/20.0.4

{
    "id": 1,
    "user_id": 1,
    "value": 2.6
}
```

### Bank Account: Debit <a name="api-debit">

``` shell
http -f POST :5002/debit value="2.6" 'Authorization: Bearer {token}'
```

``` json
HTTP/1.1 200 OK
Connection: close
Content-Length: 38
Content-Type: application/json
Date: Sat, 20 Mar 2021 22:33:03 GMT
Server: gunicorn/20.0.4

{
    "id": 1,
    "user_id": 1,
    "value": 2.6
}
```

### Bank Account: Statement <a name="api-statement">

``` shell
http :5002/statement 'Authorization: Bearer {token}'
```

``` json
HTTP/1.1 200 OK
Connection: close
Content-Length: 142
Content-Type: application/json
Date: Sun, 21 Mar 2021 13:57:57 GMT
Server: gunicorn/20.0.4

{
    "credits": [
        {
            "id": 1,
            "user_id": 1,
            "value": 2.6
        },
        {
            "id": 2,
            "user_id": 1,
            "value": 5.1
        }
    ],
    "debits": [
        {
            "id": 1,
            "user_id": 1,
            "value": 4.9
        }
    ]
}
```

## Monitoring and metrics

### Prometheus

``` shell
http://localhost:9090
```

### Grafana

``` shell
http://localhost:3000
```

## Automation Testing

### Jenkins

```
http://localhost:8081
```

``` shell
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

Copy the password and join the Jenkins plataform.

## Kubernetes

### Minikube

``` shell
minikube start
```

``` shell
minikube status
```

``` shell
minikube
type: Control Plane
host: Running
kubelet: Running
apiserver: Running
kubeconfig: Configured
timeToStop: Nonexistent
```

``` shell
minikube dashboard
```

### Namespace and apps

``` shell
make kube-apply
```

### Tables

``` shell
make start-tables
```

### Minikube tunnel

Keep this command running:

``` shell
minikube tunnel
```

``` shell
Status:	
	machine: minikube
	pid: 42901
	route: 10.96.0.0/12 -> 192.168.49.2
	minikube: Running
	services: [nginx-svc, postgres-svc, user-svc, bank-account-svc]
    errors: 
		minikube: no errors
		router: no errors
		loadbalancer emulator: no errors
```

### Run the user API throught the kubernetes container

Get the service external IP:

``` shell
http -f POST <user-svc-external-ip>:5001/user username="user" email="user@teste.com" password="password123" name="user"
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