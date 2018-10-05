# -*- coding: utf-8 -*-
from flask import Flask
from flask_cors import CORS
from flask_restful import Api


# Resources
from resources.Student import StudentInsertInitial, StudentUpdate

# instantiate the app
app = Flask(__name__)
api = Api(app)

# enable CORS
CORS(app)

# estudiantes route
api.add_resource(StudentInsertInitial, '/estudiantes')
api.add_resource(StudentUpdate, '/estudiantes/<date_update>')

if __name__ == '__main__':
    app.run(debug=True, port=int('8082'))