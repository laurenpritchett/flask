from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


# YOUR ROUTES GO HERE

@app.route('/')
def index():
    """Return homepage."""

    return render_template("index.html")


@app.route("/application-form")
def application_form():
    """Return application form."""

    jobs = ["Software Engineer", "QA Engineer", "Product Manager"]

    return render_template("application-form.html", jobs=jobs)


@app.route("/application-success", methods=["POST"])
def application_response():
    """Return application response."""

    first_name = request.form.get("firstname")
    last_name = request.form.get("lastname")

    salary = float(request.form.get("salaryrequirement"))
    job = request.form.get("select")

    return render_template("application-response.html", first_name=first_name, last_name=last_name, salary=salary, job=job)

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
