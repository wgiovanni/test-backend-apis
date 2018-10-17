# -*- coding: utf-8 -*-
from flask import Flask, make_response, request
from flask_cors import CORS
from flask_restful import Api
import os
from werkzeug.utils import secure_filename
from flask_restful import reqparse, abort, Api, Resource
import simplejson as json

# Resources
from resources.Student import StudentInsertInitial, StudentUpdate
from resources.Teacher import TeacherInsertInitial

UPLOAD_FOLDER = 'C:/Users\wilke/Desktop/flask-vue'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'xlsx'])


# instantiate the app
app = Flask(__name__)
api = Api(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# enable CORS
CORS(app)


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class File(Resource):
    representations = {'application/json': make_response}
    parser = reqparse.RequestParser()

    def post(self):
        #args = parser.parse_args()
        file = request.files['file']
        print(file.filename)
        if file and allowed_file(file.filename):
            # From flask uploading tutorial
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #return redirect(url_for('uploaded_file', filename=filename))
            return json.dumps({'carga':'exitosa'}), 201, { 'Access-Control-Allow-Origin': '*' }
        else:
            # return error
            return json.dumps({'carga':'error'}), 201, { 'Access-Control-Allow-Origin': '*' }

# estudiantes route
api.add_resource(StudentInsertInitial, '/estudiantes')
api.add_resource(StudentUpdate, '/estudiantes/<date_update>')
api.add_resource(TeacherInsertInitial, '/profesores')
api.add_resource(File, '/upload')





if __name__ == '__main__':
    app.run(debug=True, port=int('8082'))