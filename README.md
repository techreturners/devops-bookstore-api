# DevOps Bookstore API

A Python [Flask REST API](https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask) to fetch book information in the form of [JSON](https://www.json.org/json-en.html)

Currently being built via CircleCI

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

### (Optional) Running Locally

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

NOTE: **pipenv** can be tempremental and varies from machine to machine if the above steps do not work skip to **Running in Docker** below

### (Optional) Running Unit Tests

The tests can be ran in the same manner as running the application.

Ensure you are in the root of the project and run:

```
pip install pipenv
```

Once **pipenv** is installed you can run the application locally by running:

```
pipenv run python -m unittest
```


