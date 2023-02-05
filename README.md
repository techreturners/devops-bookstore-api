# DevOps Bookstore API

A Python [Flask REST API](https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask) to fetch book information in the form of [JSON](https://www.json.org/json-en.html)

## Instructions

### Running in Docker

The application can be deployed as a Docker container.

Firstly build the Docker image

```
docker build -t bookstore-api:1.0 .
```

Once the image has built you can start up the container by running:

```
docker run --rm -it -p 5050:5000 bookstore-api:1.0
```

Then you should be able to open up your browser and head to [http://localhost:5050/books](http://localhost:5050/books) to see the JSON response

