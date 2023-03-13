# app.py is the main file responsible for running the app
from flask import Flask, Response, request, url_for

# instantiate the Flask application object
app = Flask(__name__)


# set up a route and bind a function as its response
@app.route('/')
def hello_from_flask():
    about_url_endpoint = url_for('about')
    return """
        <html>
            <head>
                <title>Flask App</title>
            </head>
            <body>
                <h1>Home Page</h1>
                <p>Welcome to our application</p>
                <hr>
                <a href="{}">About</a>
            </body>
        </html>
        """.format(about_url_endpoint)


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


@app.route('/hello/<name>/<int:age>')
def say_hello_name_age_page(name, age):
    return """
    <html>
        <head>
            <title>Flask App</title>
        </head>
        <body>
            <h1>Name & Age Page</h1>
            <p>Hello {}!</p>
            <p>You are {} years old.</p>
        </body>
    </html>
    """.format(name, age)


@app.route('/hellowithurl/<name>/<int:age>')
def say_hello_name_age_page_url(name, age):
    url_home_page_endpoint = url_for('hello_from_flask')  # pass a name of another function as a string
    return """
    <html>
        <head>
            <title>Flask App</title>
        </head>
        <body>
            <h1>Name & Age Page</h1>
            <p>Hello {}!</p>
            <p>You are {} years old.</p>
            <br>
            <a href="{}">Home</a>
        </body>
    </html>
    """.format(name, age, url_home_page_endpoint)


@app.route('/about')
def about():
    url_home_page_endpoint = url_for('hello_from_flask')  # pass a name of another function as a string
    return """
    <html>
        <head>
            <title>Flask App</title>
        </head>
        <body>
            <h1>About Page</h1>
            <p>This is a lovely about page</p>
            <hr>
            <a href="{}">Home</a>
        </body>
    </html>
    """.format(url_home_page_endpoint)


# if this script is invoked directly (rather than being imported), run the flask app
if __name__ == "__main__":
    app.run(debug=True)
