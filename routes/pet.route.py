import os
import sys
from flask import Flask, request
import psycopg2

# This likely belongs in the referring file
# app = Flask(__name__)

# Set up postgres connection with psycopg2

@app.route('/getpets', methods=['GET'])
def getpets():
    print("in getpets")
    cur.execute("SELECT * FROM pet;")
    result = cur.fetchall()
    (1, 100, "abc'def")
    return "data from pets table is {}".format(result)