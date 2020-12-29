from flask import Flask, request, render_template, send_from_directory
import stocks
from glob import iglob
import os


app = Flask(__name__)
@app.route('/upload/<filename>')
def send_image(filename):
  return send_from_directory("indexes",filename)
@app.route("/")
def home():
  pngs = os.listdir('./indexes')
  return render_template("index.html", pngs = pngs)
  
if __name__ == "__main__":
  stocks.graphIndexes()
  app.run()
