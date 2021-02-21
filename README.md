# DevOps Bookstore API

A Python [Flask REST API](https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask) to fetch book information in the form of [JSON](https://www.json.org/json-en.html)

## Instructions

### Running Locally

The instructions assume that you have Python 3 installed.

If you do not have `pipenv` installed you'll need to install this first

```
pip install pipenv
```

Once **pipenv** is installed you can run the application locally by running:

```
pipenv install
```

followed by

```
pipenv run python api.py
```

### Running in Docker

The application can be deployed as a Docker container.

Firstly build the Docker image

```
docker build -t bookstore-api:1.0 .
```

Once the image has built you can start up the container by running:

```
docker run --rm -it -p 5000:5000 bookstore-api:1.0
```

Then you should be able to open up your browser and head to [http://localhost:5000/books](http://localhost:5000/books) to see the JSON response

