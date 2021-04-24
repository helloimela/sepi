from flask_restful import Resource, Api, reqparse
import pandas as pd
import csv

class RegisterBusiness(Resource):
    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('deviceId', required=True)
        parser.add_argument('location', required=True)
        parser.add_argument('type', required=True)
        parser.add_argument('maxVisitor', required=True)
        parser.add_argument('franchise', required=True)
        parser.add_argument('takeaway', required=True)

        args_dict = parser.parse_args()  # return dictionary
        print(args_dict)

        with open(r'business_list.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(list(args_dict.values()))

        return 200

class Device(Resource):
    def post(self):
        # TODO handler for bad request
        parser = reqparse.RequestParser()
        parser.add_argument('deviceId', required=True)
        parser.add_argument('visitorCount', required=True)
        args = parser.parse_args()  # parse to dictionary
        print(args)
        return 200

class Customer(Resource):
    pass
