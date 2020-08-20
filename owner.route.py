import flask
from flask import request, jsonify, render_template
import psycopg2

app = flask.Flask(__name__)
app.config["DEBUG"] = True

db = "dbname=%s host=%s " % ('pet_hotel', 'localhost')
schema = "schema.sql"
conn = psycopg2.connect(db)
cur = conn.cursor()


@app.route('/user')
def getUser():
    cur.execute("SELECT * FROM owner;")
    bla = cur.fetchall()
   for row in bla:
       print("Id = ", row[0] )

app.run()