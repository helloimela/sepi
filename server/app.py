from flask import Flask
from flask_restful import Resource, Api, reqparse
from endpoint import *
#import pandas as pd
#import ast

app = Flask(__name__)
api = Api(app)

api.add_resource(Locations, '/locations')  # 'entry point: URL/locations'
api.add_resource(ClientApp, '/clientapp')

if __name__ == '__main__':
    app.run()