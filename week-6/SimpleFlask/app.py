# appw7.py is the main file responsible for running the app
from flask import Flask, Response, request

# instantiate the Flask application object
app = Flask(__name__)


# set up a route and bind a function as its response
@app.route('/')
def hello_from_flask():
    return "Hello from FLASK"


@app.route('/bye', methods=['GET'])  # don't have to specify methods if it's get, because it is a default
def goodbye_from_flask():
    return "Goodbye from FLASK"


@app.route('/get/text')
def get_text():
    return Response("Hello from FLASK using RESPONSE object")


# http post request only
@app.route('/post/text', methods=['POST'])
def post_text():
    data_sent = request.data.decode('utf-8')
    return Response("You posted this data to the Flask App: " + data_sent)


@app.route('/dynamic/<word>')
def say_word(word):
    return word


@app.route('/square/<int:number>')
def square(number):
    squared = number ** 2
    line = "Your number squared is " + str(squared)
    return line


@app.route('/name/<name>')
def say_hello(name):
    return "Hello " + name


@app.route('/namePage/<name>')
def say_hello_name(name):
    return """
    <html>
    <head>
        <title>Sample - Flask routes</title>
    </head>
    <body>
        <h1>Name page</h1>
        <p>Hello {}!</p>
    </body>
    </html>
    """.format(name)


# if this script is invoked directly (rather than being imported), run the flask app
if __name__ == "__main__":
    app.run(debug=True)
