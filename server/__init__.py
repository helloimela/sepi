from flask import Flask, render_template
from flask_restful import Resource, Api, reqparse
from endpoint import *
import sqlite3
#import pandas as pd

app = Flask(__name__)
api = Api(app)

# API endpoints. Example:
# http://URL:port/device?deviceId=2&visitorCount=100
api.add_resource(GetStatus, '/api/getstatus')

# Device endpoints
api.add_resource(Device, '/api/device')

# Mobile app endpoints
api.add_resource(RegisterBusiness, '/api/registerbusiness')
api.add_resource(Customer, '/api/customer')

#@app.route("/")
#def not_found():
    #return '404 Nothing here'

@app.route("/")
def home():
    con = sqlite3.connect('example.db')
    cur = con.cursor()
    rows = cur.execute('SELECT * FROM stocks ORDER BY price')
    return render_template('home.html', rows = rows)

if __name__ == '__main__':
    app.run()
