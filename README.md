# DevOps Bookstore API

A Python [Flask REST API](https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask) to fetch book information in the form of [JSON](https://www.json.org/json-en.html)

## Instructions

### Running in Docker

The application can be deployed as a Docker container.

Firstly build the Docker image.

> ⚠️ Note:
> We specify the platform as linux/amd64 within the build and run commands. By default, Docker will use the host platform architecture which if you are on a Mac might not work when deploying your container on to Lunux platforms.

```
docker build --platform linux/amd64 -t bookstore-api:1.0 .
```

Once the image has built you can start up the container by running:

```
docker run --platform linux/amd64 --rm -it -p 5050:5000 bookstore-api:1.0
```

Then you should be able to open up your browser and head to [http://localhost:5050/books](http://localhost:5050/books) to see the JSON response

