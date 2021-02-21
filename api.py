from flask import Flask
from flask_restful import Resource, Api, reqparse, abort, marshal, fields
from flask_cors import CORS

# Initialize Flask
app = Flask(__name__)
CORS(app)
api = Api(app)

# A List of Dicts to store all of the books
books = [{
        "bookTitle": "Learning Docker" ,
        "bookImage": "https://itbook.store/img/books/9781784397937.png",
        "bookDescription": "Docker is a next-generation platform for simplifying application containerization life-cycle. Docker allows you to create a robust and resilient environment in which you can generate portable, composable, scalable, and stable application containers.",
        "bookAuthors" : "Pethuru Raj, Jeeva S. Chelladhurai, Vinod Singh"
    },
    {
        "bookTitle": "Kubernetes Best Practices" ,
        "bookImage": "https://itbook.store/img/books/9781492056478.png",
        "bookDescription": "In this practical guide, four Kubernetes professionals with deep experience in distributed systems, enterprise application development, and open source will guide you through the process of building applications with container orchestration.",
        "bookAuthors" : "Brendan Burns, Eddie Villalba"
    },
    {
        "bookTitle": "Site Reliability Engineering" ,
        "bookImage": "https://itbook.store/img/books/9781491929124.png",
        "bookDescription": "The overwhelming majority of a software system's lifespan is spent in use, not in design or implementation. So, why does conventional wisdom insist that software engineers focus primarily on the design and development of large-scale computing systems?",
        "bookAuthors" : "Betsy Beyer, Chris Jones, Jennifer Petoff"
    },
]

# Schema For the Book Request JSON
bookFields = {
    "bookTitle": fields.String,
    "bookImage": fields.String,
    "bookDescription": fields.String,
    "bookAuthors": fields.String
}


class BookList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()

    def get(self):
        return{"books": [marshal(book, bookFields) for book in books]}


api.add_resource(BookList, "/books")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
