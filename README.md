# Day-54-62-Flask-Web-Development
## Flask Web Development Framework

from flask import Flask  
app = Flask(__name__)  

@app.route('/')  
def hello_world():  
return 'Hello, World!'  

### So what did that code do?

1. First we imported the Flask class. An instance of this class will be our WSGI application.

2. Next we create an instance of this class. The first argument is the name of the application’s module or package. If you are using a single module (as in this example), you should use __name__ because depending on if it’s started as application or imported as module the name will be different ('__main__' versus the actual import name). This is needed so that Flask knows where to look for templates, static files, and so on. For more information have a look at the Flask documentation.

3. We then use the route() decorator to tell Flask what URL should trigger our function.

4. The function is given a name which is also used to generate URLs for that particular function, and returns the message we want to display in the user’s browser.  

### Routing
Modern web applications use meaningful URLs to help users. Users are more likely to like a page and come back if the page uses a meaningful URL they can remember and use to directly visit a page.  

Use the route() decorator to bind a function to a URL.  

@app.route('/')  
def index():  
      return 'Index Page'  
  
@app.route('/hello')  
def hello():  
      return 'Hello, World'  
You can do more! You can make parts of the URL dynamic and attach multiple rules to a function.

### URL Building
To build a URL to a specific function, use the url_for() function. It accepts the name of the function as its first argument and any number of keyword arguments, each corresponding to a variable part of the URL rule. Unknown variable parts are appended to the URL as query parameters.  

Why would you want to build URLs using the URL reversing function url_for() instead of hard-coding them into your templates?  

1. Reversing is often more descriptive than hard-coding the URLs.  

2. You can change your URLs in one go instead of needing to remember to manually change hard-coded URLs.  

3. URL building handles escaping of special characters transparently.  

4. The generated paths are always absolute, avoiding unexpected behavior of relative paths in browsers.  

5. If your application is placed outside the URL root, for example, in /myapplication instead of /, url_for() properly handles that for you.  

### HTTP Methods
Web applications use different HTTP methods when accessing URLs. You should familiarize yourself with the HTTP methods as you work with Flask. By default, a route only answers to GET requests. You can use the methods argument of the route() decorator to handle different HTTP methods.

from flask import request  

@app.route('/login', methods=['GET', 'POST'])  
def login():  
    if request.method == 'POST':  
        return do_the_login()  
    else:  
        return show_the_login_form()
