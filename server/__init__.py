from flask import Flask
from flask_restful import Resource, Api, reqparse
from .endpoint import *
#import pandas as pd

app = Flask(__name__)
api = Api(app)

# API endpoints. Example:
# http://URL:port/device?deviceId=2&visitorCount=100
api.add_resource(GetStatus, '/getstatus')

# Device endpoints
api.add_resource(Device, '/device')

# Mobile app endpoints
api.add_resource(RegisterBusiness, '/registerbusiness')
api.add_resource(Customer, '/customer')

@app.route("/")
def not_found():
    return '404 Nothing here'

if __name__ == '__main__':
    app.run()
