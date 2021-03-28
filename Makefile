kube-apply:
	kubectl apply -f k8s/config
	kubectl -n internet-banking apply -f k8s/nginx
	kubectl -n internet-banking apply -f k8s/postgres
	kubectl -n internet-banking apply -f k8s/user

kube-events:
	kubectl -n internet-banking get events -w

kube-pods:
	kubectl -n internet-banking get pods -w

kube-services:
	kubectl -n internet-banking get services

exec-postgres:
	kubectl -n internet-banking exec -it services/postgres-svc -- /bin/bash

build-user:
	kubectl -n internet-banking exec -it services/user-svc -- /usr/src/app/entrypoint.sh
