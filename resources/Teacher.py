from flask_restful import abort, Resource, reqparse
import simplejson as json
from psycopg2 import DatabaseError
from textwrap import dedent
from common.BD import BD
from flask import make_response, jsonify, request
from datetime import datetime


class TeacherInsertInitial(BD, Resource):
    representations = {'application/json': make_response}
    parser = reqparse.RequestParser()

    def get(self):
        try:
            # consultar docente
            resultTeacher = self.queryAll(dedent("""SELECT cedula, nombre, apellido, correo, grado, area_trabajo, sexo FROM docente"""))
            response = {
                "dim-docente": {"items": resultTeacher}  
            }  
        except DatabaseError as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(response), 200, { 'Access-Control-Allow-Origin': '*' }