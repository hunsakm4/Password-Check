import argparse  # allow script to run with arguments
from flask import Flask, render_template

# When creating the flask app, we can specify the templates and static folder
# where we are keeping our html, css, and js files. This allows for
# tidy organization of code and keeping the main flask script clean.
app = Flask(__name__, template_folder="templates", static_folder="static")


@app.route("/")
def home():
    return render_template("checkpassword.html")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check Password")
    parser.add_argument(
        "--port",
        type=int,
        default=5000,
        help="Port to listen on (default: 5000)",
    )
    args = parser.parse_args()
    app.run(debug=True, port=args.port)
