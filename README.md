# scraper-service

docker build . -t scrapertest
docker run -d --name test1 -p 8080:80 scrapertest