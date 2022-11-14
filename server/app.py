# import modules is required
# First we imported the Flask class. An instance of this class will be our WSGI application.
from flask import Flask

# Flask constructor takes the name of
# current module (__name__) as argument.
# Next we create an instance of this class. The first argument is the name of the application’s module or package. __name__ is a convenient shortcut for this that is appropriate for most cases. This is needed so that Flask knows where to look for resources such as templates and static files.
app = Flask(__name__)


# We then use the route() decorator to tell Flask what URL should trigger our function.
@app.route("/")
# The function returns the message we want to display in the user’s browser. The default content type is HTML, so HTML in the string will be rendered by the browser.
def index():
    return "<p>Hello, Flask!</p>"


@app.route("/getCustomerList")
def getCustomerList():
    return "<h1>Customer List</h1>"


# main driver function
if __name__ == "__main__":
    app.run(debug=True)
