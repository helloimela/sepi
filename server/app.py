from flask import Flask
from flask_restful import Resource, Api, reqparse
from endpoint import *
#import pandas as pd
#import ast

app = Flask(__name__)
api = Api(app)

# API endpoints. Example:
# http://URL:port/device?deviceId=2&visitorCount=100
api.add_resource(RegisterBusiness, '/registerbusiness')  # 'entry point: URL/locations'
api.add_resource(Device, '/device')
api.add_resource(Customer, '/customer')

if __name__ == '__main__':
    app.run()