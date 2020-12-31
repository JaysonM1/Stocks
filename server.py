from flask import Flask, request, render_template, send_from_directory
import stocks
from glob import iglob
import os


app = Flask(__name__)

dailyIndexes = stocks.graphIndexes()
dailyGainers = stocks.graphGainers(stocks.getGainers())
@app.route('/upload/<filename>')
def send_image(filename):
  if (filename in os.listdir("indexes/")):
    return send_from_directory("indexes",filename)
  elif(filename in os.listdir("gainers/")):
   return send_from_directory("gainers",filename)
  else:
    return send_from_directory("losers",filename)
@app.route("/")
def home():
  indexes = os.listdir('./indexes')
  gainers = os.listdir('./gainers')
  losers = os.listdir('./losers')
  return render_template("index.html", ind = indexes, ga = gainers, losers = losers)
  
if __name__ == "__main__":
  stocks.run()
  app.run()
