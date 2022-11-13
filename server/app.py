# import modules is required
from flask import Flask
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)


@app.route("/")
def index():
    return "<p>Hello, Flask!</p>"


# main driver function
if __name__ == "__main__":
    app.run(debug=True)
