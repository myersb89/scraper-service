# scraper-service
Service to scrape HTTP status codes from a given URL

## Build the Docker Container
```
docker build . -t scraper-app
```

## Simple Test Deploy to Docker
```
docker run -d --name test1 -p 8080:8080 -p 9095:9095 scraper-app

# Generate some traffic (ctrl+c to quit)
python generate_traffic.py 8080

# browse to view the metrics
localhost:9095

```

## Kubernetes Deployment + Prometheus instance
```
# Create an account for Prometheus to monitor the cluster
kubectl create -f deployment/prometheus-role.yml
kubectl create -f deployment/prometheus-account.yml
kubectl create -f deployment/prometheus-binding.yml

# Create a configmap for the Prometheus configuration
kubectl create -f deployment/prometheus-config.yml

# Create the Prometheus deployment and expose it over port 31536
kubectl create -f deployment/prometheus-service.yml
kubectl create -f deployment/prometheus-deployment.yml

# Create the Scraper service deployment and expose it, port 31534 for the service and port 31535 for the metrics endpoint
kubectl create -f deployment/app-service.yml
kubectl create -f deployment/app-deployment.yml

# Generate some traffic (ctrl+c to quit)
python generate_traffic.py

# Browse to view the Prometheus instance and run PromQL queries
localhost:31536

```

### PromQL queries
Some basic queries for the scraper service counter

```
# All combinations of status code and url for the counter
http_get_total

# Total times the scraper service has been invoked
sum(http_get_total)

# Increase in gets over the last 15 by url
sum(increase(http_get_total[15m])) by (url)

# Rate of each status code over the last minute
sum(rate(http_get_total[1m])) by (code)
```