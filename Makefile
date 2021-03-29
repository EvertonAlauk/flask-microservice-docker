kube-apply:
	kubectl apply -f k8s/config
	kubectl -n internet-banking apply -f k8s/nginx
	kubectl -n internet-banking apply -f k8s/postgres
	kubectl -n internet-banking apply -f k8s/user
	kubectl -n internet-banking apply -f k8s/bank_account

kube-events:
	kubectl -n internet-banking get events -w

kube-pods:
	kubectl -n internet-banking get pods -w

kube-services:
	kubectl -n internet-banking get services

build-tables:
	kubectl -n internet-banking exec -it services/user-svc -- /usr/src/app/entrypoint.sh
	kubectl -n internet-banking exec -it services/bank-account-svc -- /usr/src/app/entrypoint.sh

start-postgres:
	kubectl -n internet-banking exec -it services/postgres-svc -- /bin/bash

start-user:
	kubectl -n internet-banking exec -it services/user-svc -- /bin/bash

start-bank-account:
	kubectl -n internet-banking exec -it services/bank-account-svc -- /bin/bash
