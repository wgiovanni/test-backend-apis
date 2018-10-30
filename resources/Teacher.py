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
                SELECT cedula, primernombre, primerapellido, correo, areadeinvestigacion, 
                sexo, nacionalidad, segundonombre, segundoapellido, facultad, tipo, escalafon
                FROM docente"""))
            
            #consultar publicaciones
            resultPublication = self.queryAll(dedent("""\
            SELECT id as codigo, cedulaautor, titulopublicacion, urlcitacion, urlpublicacion, numerocitaciones
            FROM public.publicacion"""))

            resultOtherStudio = self.queryAll(dedent("""\
            SELECT id as codigo, cedulaautor, nomtitulo
            FROM public.otro_estudio"""))

            resultPrize = self.queryAll(dedent("""\
            SELECT id as codigo, nombre, cedulaautor
            FROM public.premio"""))

            resultProject = self.queryAll(dedent("""\
            SELECT id as codigo, cedulaautor, titulo
            FROM public.proyecto"""))

            resultTitle = self.queryAll(dedent("""\
            SELECT id as codigo, cedulaautor, nomtitulo, nivel
            FROM public.titulo"""))

            response = {
                "dim-docente": {"items": resultTeacher},
                "dim-docente-otro-estudio": {"items": resultOtherStudio},
                "dim-docente-publicacion": {"items": resultPublication},
                "dim-docente-proyecto": {"items": resultProject},
                "dim-docente-titulo": {"items": resultTitle},
                "dim-docente-premio": {"items": resultPrize}  
                #"hechos-docente-publicacion": {"items": resultRelationship},
                #"hechos-docente-facultad": {"items": resultTeacherFaculty}
            }  
        except DatabaseError as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(response), 200, { 'Access-Control-Allow-Origin': '*' }

class TeacherUpdate(BD, Resource):
    representations = {'application/json': make_response}
    parser = reqparse.RequestParser()

    def get(self, date_update):

        try:
            date_update = datetime.strptime(date_update, '%Y-%m-%d %H:%M:%S')
             # consultar docente
            resultTeacher = self.queryAll(dedent("""\
                SELECT cedula, primernombre, primerapellido, correo, areadeinvestigacion, 
                sexo, nacionalidad, segundonombre, segundoapellido, facultad, tipo, escalafon
                FROM docente WHERE fecha_actualizacion >= %s"""), [date_update])
            
            #consultar publicaciones
            resultPublication = self.queryAll(dedent("""\
            SELECT cedulaautor, titulopublicacion, urlcitacion, urlpublicacion, numerocitaciones
            FROM public.publicacion WHERE fecha_actualizacion >=  %s"""), [date_update])

            resultOtherStudio = self.queryAll(dedent("""\
            SELECT cedulaautor, nomtitulo
            FROM public.otro_estudio WHERE fecha_actualizacion >=  %s"""), [date_update])

            resultPrize = self.queryAll(dedent("""\
            SELECT nombre, cedulaautor
            FROM public.premio WHERE fecha_actualizacion >=  %s"""), [date_update])

            resultProject = self.queryAll(dedent("""\
            SELECT cedulaautor, titulo
            FROM public.proyecto WHERE fecha_actualizacion >=  %s"""), [date_update])

            resultTitle = self.queryAll(dedent("""\
            SELECT cedulaautor, nomtitulo, nivel
            FROM public.titulo WHERE fecha_actualizacion >=  %s"""), [date_update])

            response = {
                "dim-docente": {"items": resultTeacher},
                "dim-otro-estudio": {"items": resultOtherStudio},
                "dim-publicacion": {"items": resultPublication},
                "dim-proyecto": {"items": resultProject},
                "dim-titulo": {"items": resultTitle},
                "dim-premio": {"items": resultPrize}  
                #"hechos-docente-publicacion": {"items": resultRelationship},
                #"hechos-docente-facultad": {"items": resultTeacherFaculty}
            }  

        except DatabaseError as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return jsonify(response), 200, { 'Access-Control-Allow-Origin': '*' }