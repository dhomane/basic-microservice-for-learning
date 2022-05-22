# Kubernetes Deployment

These YAML files will deploy the working calculator app microservice onto a Kubernetes cluster.

All nodes in the test cluster were running 1.13.1 at the last test.

## Deployment Order

Run the 3 YAML files in the order below to create the 3 services.

1. calculator_svc.yaml
2. randomnum_svc.yaml
3. database_svc.yaml

## Ingress

Remove the Ingress section from calculator_svc.yaml if there is no Ingress controller available or modify it if you aren't running Traefik.

Also set the host for the Ingress. During testing, I delegated an entire subdomain to Traefik using a CoreDNS instance external to the Kubernetes Cluster.

If you elect to remove the Ingress, you can run ```curl <service_ip>/calc``` from the master and it will return a response from the calculator service.