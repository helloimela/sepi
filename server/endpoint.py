from flask_restful import Resource, Api, reqparse
import pandas as pd

class Locations(Resource):
    def get(self):
        data = pd.read_csv('location_list.csv')
        data = data.to_dict()
        return {'data': data}, 200  # return data and 200 OK code

class ClientApp(Resource):
    pass
