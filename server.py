import flask
from flask import request, jsonify, render_template
import psycopg2

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def index():
    return render_template('index.html')

conn = psycopg2.connect("dbname=pet_hotel user=acefox")

cur = conn.cursor()

cur.close()
conn.close()

app.run()