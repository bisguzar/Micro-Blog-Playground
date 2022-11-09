# import modules is required
from flask import Flask, render_template, url_for
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


# main driver function
if __name__ == "__main__":
    app.run(debug=True)
