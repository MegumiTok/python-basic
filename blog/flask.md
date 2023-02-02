# Flask[^1]

A minimal Flask application looks something like this:
```py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
```
>1. First we imported the Flask class. An instance of this class will be our WSGI application.
>2. …(略)…([公式ドキュメント](https://flask.palletsprojects.com/en/0.12.x/quickstart/)で詳しく確認)
>3. We then use the route() decorator to tell Flask what URL should trigger our function.
>4. The function is given a name which is also used to generate URLs for that particular function, and returns the message we want to display in the user’s browser.

# WSGI (Web Server Gateway Interface) 
>WSGI is an interface between web servers and web apps for python.

>Flask is a WSGI application. A WSGI server is used to run the application, converting incoming HTTP requests to the standard WSGI environ, and converting outgoing WSGI responses to HTTP responses.[^2]

>WSGI servers have HTTP servers built-in. However, a dedicated HTTP server may be safer, more efficient, or more capable. Putting an HTTP server in front of the WSGI server is called a “reverse proxy.”[^2]

# WSGI and ASGI

[参照させていただいた記事](https://developer.vonage.com/en/blog/how-wsgi-vs-asgi-is-like-baking-a-cake)

>WSGI stands for Web Server Gateway Interface, and ASGI stands for Asynchronous Server Gateway interface. They both specify the interface and sit in between the web server and a Python web application or framework.[^3]

[^1]:https://flask.palletsprojects.com/en/0.12.x/quickstart/

[^2]:https://flask.palletsprojects.com/en/2.2.x/deploying/

[^3]:https://developer.vonage.com/en/blog/how-wsgi-vs-asgi-is-like-baking-a-cake