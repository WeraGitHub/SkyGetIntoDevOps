from flask import render_template
from application import app


@app.route('/')
def hello_from_flask():
    return """
        <html>
            <head>
                <title>Flask App</title>
            </head>
            <body>
                <h1>Home Page</h1>
                <p>Welcome to our application</p>
                <hr>
            </body>
        </html>
        """