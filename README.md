# scraper-service

docker build . -t scrapertest
docker run -d --name test1 -p 8080:80 -p 9095:9095 scrapertest