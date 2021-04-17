minikube:
	minikube start
	minikube status
	minikube addons enable ingress

kubernetes:
	@echo "Apply namespace and envvars..."
	kubectl apply -f k8s/config
	kubectl -n internet-banking apply -f k8s/ingress
	kubectl -n internet-banking apply -f k8s/postgres
	kubectl -n internet-banking apply -f k8s/user
	kubectl -n internet-banking apply -f k8s/bank_account

databases:
	@echo "Creating the microservices databases..."
	kubectl -n internet-banking exec -it services/user-svc -- /usr/src/app/entrypoint.sh
	kubectl -n internet-banking exec -it services/bank-account-svc -- /usr/src/app/entrypoint.sh

kube-events:
	kubectl -n internet-banking get events

kube-pods:
	kubectl -n internet-banking get pods

kube-services:
	kubectl -n internet-banking get services

kube-ingress:
	kubectl -n internet-banking get ingress

kube-all:
	kubectl -n internet-banking get all

start-postgres:
	kubectl -n internet-banking exec -it services/postgres-svc -- /bin/bash

start-user:
	kubectl -n internet-banking exec -it services/user-svc -- /bin/bash

start-bank-account:
	kubectl -n internet-banking exec -it services/bank-account-svc -- /bin/bash
