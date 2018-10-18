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
            resultTeacher = self.queryAll(dedent("""\
                SELECT d.cedula, d.nombre, d.apellido, d.correo, d.grado, d.area_trabajo, d.sexo, d.nacionalidad, e.nombre AS escalafon
                FROM docente AS d 
                INNER JOIN escalafon AS e
                ON (e.id = d.id_escalafon)"""))
            
            # consultar facultad
            resultfaculty = self.queryAll(dedent("""SELECT nombre FROM facultad"""))

            # consultar escalafon
            resultScale = self.queryAll(dedent("""SELECT nombre FROM escalafon"""))

            #consultar publicaciones
            resultPublication = self.queryAll(dedent("""SELECT id AS codigo, tipo, autor, titulo, fecha, revista FROM publicacion"""))
            publicationList = []
            for row in resultPublication:
                row['fecha'] = row['fecha'].strftime('%Y-%m-%d')
                publicationList.append(row)
            resultPublication = publicationList

            # consultar relaciones
            resultRelationship = self.queryAll(dedent("""\
                SELECT d.cedula, p.id AS publicacion
                FROM docente AS d
                INNER JOIN docente_publicacion AS dp
                ON (dp.id_docente = d.id)
                INNER JOIN publicacion AS p
                ON (dp.id_publicacion = p.id)"""))
            
            # consultas para obtener las citas por cada publicacion
            resultCitation = self.queryAll(dedent("""\
                SELECT p.id AS publicacion, COUNT(c.id) AS citas
                FROM publicacion AS p
                INNER JOIN publicacion_citacion AS pc
                ON (pc.id_publicacion = p.id)
                INNER JOIN citacion AS c
                ON (c.id = pc.id_citacion)
                GROUP BY p.id"""))
            
            for r1 in resultCitation:
                for r2 in resultRelationship:
                    if r1['publicacion'] == r2['publicacion']:
                        r2['citas'] = r1['citas']
            
            resultTeacherFaculty = self.queryAll(dedent("""\
                SELECT d.cedula, f.nombre AS facultad
                FROM docente AS d
                INNER JOIN docente_facultad AS df
                ON (d.id = df.id_docente)
                INNER JOIN facultad AS f
                ON (df.id_facultad = f.id)"""))

            for r1 in resultTeacherFaculty:
                for r2 in resultRelationship:
                    if r1['cedula'] == r2['cedula']:
                        r2['facultad'] = r1['facultad']

            
            

            response = {
                "dim-docente": {"items": resultTeacher},
                "dim-facultad": {"items": resultfaculty},
                "dim-publicacion": {"items": resultPublication},
                "dim-escalafon": {"items": resultScale}, 
                "hechos-docente-publicacion": {"items": resultRelationship}
            }  
        except DatabaseError as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(response), 200, { 'Access-Control-Allow-Origin': '*' }