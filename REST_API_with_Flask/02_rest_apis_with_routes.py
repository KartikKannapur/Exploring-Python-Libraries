__author__ = "Kartik Kannapur"

"""
Flask-RESTful API 
"""

# #Python Library Imports
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Vehicle(Resource):
    def get(self):
        return {'id' : '1', 'value' : 'BMW'}

api.add_resource(Vehicle, '/vehicle')

if __name__ == '__main__':
    app.run(debug=True)





