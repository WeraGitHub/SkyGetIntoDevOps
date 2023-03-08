# app.py is the main file responsible for running the app
from flask import Flask

# instantiate the Flask application object
app = Flask(__name__)


# set up a route and bind a function as its response
@app.route('/')
def hello_from_flask():
    return "Hello from FLASK"


# if this script is invoked directly (rather than being imported), run the flask app
if __name__ == "__main__":
    app.run(debug=True)
