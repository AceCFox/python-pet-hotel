import os
import sys
from flask import Flask
from flask import request, jsonify, render_template
import psycopg2



# Create and configure the app
app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
)



# if test_config is None:
#     # Load the instance config, if it exists, when not testing
#     app.config.from_pyfile('config.py', silent=True)
# else:
#     # Load the test config if passed in
#     app.fonfig.from_mapping(test_config)

# Ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

conn = psycopg2.connect("dbname=pet_hotel user=acefox" )

cur = conn.cursor()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/getpets', methods=['GET'])
def getpets():
    print("in getpets")
    cur.execute("SELECT * FROM pet;")
    result = cur.fetchall()
    # (1, 100, "abc'def")
    return "data from pets table is {}".format(result)

@app.route('/user', methods = ['GET'])
def getUser():
    cur.execute("SELECT * FROM owner;")
    result = cur.fetchall()
#    for row in result:
#        print("Id = ", row[0] )

    return "data from pets table is {}".format(result)




# cur.close()
# conn.close()

app.run()

