from flask import Flask, request, render_template, send_from_directory
import newStyle
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == '__main__':
  newStyle.run()
  app.run()