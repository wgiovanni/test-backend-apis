from flask_restful import abort, Resource, reqparse
import simplejson as json
from psycopg2 import DatabaseError
from textwrap import dedent
from common.BD import BD
from flask import make_response, jsonify, request
from datetime import datetime


class GraduateInsertInitial(BD, Resource):
    representations = {'application/json': make_response}
    parser = reqparse.RequestParser()

    def get(self):
        try:
            # consultar egresado
            resultGraduate = self.queryAll(dedent("""\
            SELECT id as codigo, "nombreCertificacion", descripcion, "urlCertificacion", egresado_id
            FROM public.\"EGUC_certificacion\""""))   

            resultStudiosUc = self.queryAll(dedent("""\
            SELECT eu.id AS codigo, eu.facultad, eu.carrera, eu."anhoGrado", eu.titulo, eu."urlCertificacion"
            FROM public.\"EGUC_estudiosuc\" AS eu"""))
            studiosUcList = []
            for row in resultStudiosUc:
                row['anhogrado'] = row['anhogrado'].strftime('%Y-%m-%d')
                studiosUcList.append(row)
            resultStudiosUc = studiosUcList

            graduate = self.queryAll(dedent("""\
                SELECT "idUser", "nombreUsuario", "primerNombre", "segundoNombre", "primerApellido", 
                "segundoApellido", descripcion, intereses, foto, email, telefono, identificacion
                FROM public.\"EGUC_egresado\""""))


            resultRelationshipGraduateStudiosUc = []
            for r in graduate:
                #print(r)
                resultRelationship = self.queryAll(dedent("""\
                    SELECT eu.id AS codigo, eu.facultad, eu.carrera
                    FROM public.\"EGUC_estudiosuc\" AS eu
                    WHERE eu.egresado_id = %s"""),[r['iduser']])

                item = {"egresado": r['nombreusuario'], "estudiosuc": resultRelationship}
                resultRelationshipGraduateStudiosUc.append(item)
            
            resultCertification = self.queryAll(dedent("""\
                SELECT id AS codigo, "nombreCertificacion", descripcion, "urlCertificacion"
                FROM public.\"EGUC_certificacion\""""))

            resultRelationshipGraduateCertification = []
            resultRelationship = []
            for r in graduate:
                #print(r)
                resultRelationship = self.queryAll(dedent("""\
                    SELECT id AS codigo
                    FROM public.\"EGUC_certificacion\" 
                    WHERE egresado_id = %s"""),[r['iduser']])

                item = {"egresado": r['nombreusuario'], "certificacion": resultRelationship}
                resultRelationshipGraduateCertification.append(item)

            resultCourse = self.queryAll(dedent("""\
                SELECT id AS codigo, nombre, url
                FROM public.\"EGUC_cursos\""""))

            resultRelationshipGraduateCourse = []
            resultRelationship = []
            for r in graduate:
                #print(r)
                resultRelationship = self.queryAll(dedent("""\
                    SELECT id AS codigo
                    FROM public.\"EGUC_cursos\"
                    WHERE egresado_id = %s"""),[r['iduser']])

                item = {"egresado": r['nombreusuario'], "cursos": resultRelationship}
                resultRelationshipGraduateCourse.append(item)
            
            resultEducation = self.queryAll(dedent("""\
                SELECT id AS codigo, instituto, "campoEstudio", "tituloObtenido", "urlCertificacion"
                FROM public.\"EGUC_educacion\""""))

            resultRelationshipGraduateEducation = []
            resultRelationship = []
            for r in graduate:
                #print(r)
                resultRelationship = self.queryAll(dedent("""\
                    SELECT id AS codigo
                    FROM public.\"EGUC_educacion\"
                    WHERE egresado_id = %s"""),[r['iduser']])

                item = {"egresado": r['nombreusuario'], "educacion": resultRelationship}
                resultRelationshipGraduateEducation.append(item)

            resultPatents = self.queryAll(dedent("""\
                SELECT id AS codigo, titulo, descripcion, numero, inventores, fecha, url
                FROM public.\"EGUC_patentes\""""))
            patentsList = []
            for row in resultPatents:
                row['fecha'] = row['fecha'].strftime('%Y-%m-%d')
                patentsList.append(row)
            resultPatents = patentsList

            resultRelationshipGraduatePatents = []
            resultRelationship = []
            for r in graduate:
                #print(r)
                resultRelationship = self.queryAll(dedent("""\
                    SELECT id AS codigo
                    FROM public.\"EGUC_patentes\"
                    WHERE egresado_id = %s"""),[r['iduser']])

                item = {"egresado": r['nombreusuario'], "patentes": resultRelationship}
                resultRelationshipGraduatePatents.append(item)

            resultJobs = self.queryAll(dedent("""\
                SELECT id AS codigo, "nombreEmpresa", cargo, descripcion
                FROM public.\"EGUC_trabajos\""""))
            
            resultRelationshipGraduateJobs = []
            resultRelationship = []
            for r in graduate:
                #print(r)
                resultRelationship = self.queryAll(dedent("""\
                    SELECT id AS codigo
                    FROM public.\"EGUC_trabajos\"
                    WHERE egresado_id = %s"""),[r['iduser']])

                item = {"egresado": r['nombreusuario'], "trabajos": resultRelationship}
                resultRelationshipGraduateJobs.append(item)

            resultVolunteering = self.queryAll(dedent("""\
                SELECT id AS codigo, organizacion, descripcion, causa
                FROM public.\"EGUC_voluntariado\""""))

            resultRelationshipGraduateVolunteering = []
            resultRelationship = []
            for r in graduate:
                #print(r)
                resultRelationship = self.queryAll(dedent("""\
                    SELECT id AS codigo
                    FROM public.\"EGUC_voluntariado\"
                    WHERE egresado_id = %s"""),[r['iduser']])

                item = {"egresado": r['nombreusuario'], "voluntariado": resultRelationship}
                resultRelationshipGraduateVolunteering.append(item)


            response = {
                "dim-egresado": {"items": resultGraduate},
                "dim-estudiosuc": {"items": resultStudiosUc},
                "dim-certificacion": {"items": resultCertification},
                "dim-cursos": {"items": resultCourse},
                "dim-educacion": {"items": resultEducation},
                "dim-patentes": {"items": resultPatents},
                "dim-trabajos": {"items": resultJobs},
                "dim-voluntariado": {"items": resultVolunteering},
                "hechos-egresado-estudiosuc": {"items": resultRelationshipGraduateStudiosUc},
                "hechos-egresado-certificacion": {"items": resultRelationshipGraduateCertification},
                "hechos-egresado-cursos": {"items": resultRelationshipGraduateCourse},
                "hechos-egresado-educacion": {"items": resultRelationshipGraduateEducation},
                "hechos-egresado-patentes": {"items": resultRelationshipGraduatePatents},
                "hechos-egresado-trabajos": {"items": resultRelationshipGraduateJobs},
                "hechos-egresado-voluntariado": {"items": resultRelationshipGraduateVolunteering}
            }  
        except DatabaseError as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(response), 200, { 'Access-Control-Allow-Origin': '*' }

class GraduateUpdate(BD, Resource):
    representations = {'application/json': make_response}
    parser = reqparse.RequestParser()

    def get(self, date_update):

        try:
            date_update = datetime.strptime(date_update, '%Y-%m-%d %H:%M:%S')
            print(date_update)

            # consultar egresado
            resultGraduate = self.queryAll(dedent("""\
            SELECT "nombreUsuario", "primerNombre", "segundoNombre", "primerApellido", "segundoApellido", descripcion, intereses, email, telefono, identificacion
            FROM eguc_egresado
            WHERE fecha_actualizacion > %s"""), [date_update])

            resultStudiosUc = self.queryAll(dedent("""\
            SELECT eu.id AS codigo, eu.facultad, eu.carrera, eu."anhoGrado", eu.titulo, eu."urlCertificacion"
            FROM eguc_estudiosuc AS eu
            WHERE fecha_actualizacion > %s"""), [date_update])

            studiosUcList = []
            for row in resultStudiosUc:
                row['anhogrado'] = row['anhogrado'].strftime('%Y-%m-%d')
                studiosUcList.append(row)
            resultStudiosUc = studiosUcList

            graduate = self.queryAll(dedent("""\
                SELECT id, "nombreUsuario", "primerNombre", "segundoNombre", "primerApellido", 
                "segundoApellido", descripcion, intereses email, telefono, identificacion
                FROM public.eguc_egresado"""))

            resultRelationshipGraduateStudiosUc = []
            for r in graduate:
                #print(r)
                resultRelationship = self.queryAll(dedent("""\
                    SELECT eu.id AS codigo, eu.facultad, eu.carrera
                    FROM eguc_estudiosuc AS eu
                    WHERE eu.egresado_id = %s"""),[r['id']])

                item = {"egresado": r['nombreusuario'], "estudiosuc": resultRelationship}
                resultRelationshipGraduateStudiosUc.append(item)
            
            resultCertification = self.queryAll(dedent("""\
                SELECT id AS codigo, "nombreCertificacion", descripcion, "urlCertificacion"
                FROM public.eguc_certificacion
                WHERE fecha_actualizacion > %s"""), [date_update])

            resultRelationshipGraduateCertification = []
            resultRelationship = []
            for r in graduate:
                #print(r)
                resultRelationship = self.queryAll(dedent("""\
                    SELECT id AS codigo
                    FROM public.eguc_certificacion 
                    WHERE egresado_id = %s"""),[r['id']])

                item = {"egresado": r['nombreusuario'], "certificacion": resultRelationship}
                resultRelationshipGraduateCertification.append(item)

            resultCourse = self.queryAll(dedent("""\
                SELECT id AS codigo, nombre, url
                FROM public.eguc_cursos
                WHERE fecha_actualizacion > %s"""), [date_update])

            resultRelationshipGraduateCourse = []
            resultRelationship = []
            for r in graduate:
                #print(r)
                resultRelationship = self.queryAll(dedent("""\
                    SELECT id AS codigo
                    FROM public.eguc_cursos
                    WHERE egresado_id = %s"""),[r['id']])

                item = {"egresado": r['nombreusuario'], "cursos": resultRelationship}
                resultRelationshipGraduateCourse.append(item)
            
            resultEducation = self.queryAll(dedent("""\
                SELECT id AS codigo, instituto, "campoEstudio", "tituloObtenido", "urlCertificacion"
                FROM public.eguc_educacion
                WHERE fecha_actualizacion > %s"""), [date_update])

            resultRelationshipGraduateEducation = []
            resultRelationship = []
            for r in graduate:
                #print(r)
                resultRelationship = self.queryAll(dedent("""\
                    SELECT id AS codigo
                    FROM public.eguc_educacion
                    WHERE egresado_id = %s"""),[r['id']])

                item = {"egresado": r['nombreusuario'], "educacion": resultRelationship}
                resultRelationshipGraduateEducation.append(item)

            resultPatents = self.queryAll(dedent("""\
                SELECT id AS codigo, titulo, descripcion, numero, inventores, fecha, url
                FROM public.eguc_patentes
                WHERE fecha_actualizacion > %s"""), [date_update])

            patentsList = []
            for row in resultPatents:
                row['fecha'] = row['fecha'].strftime('%Y-%m-%d')
                patentsList.append(row)
            resultPatents = patentsList

            resultRelationshipGraduatePatents = []
            resultRelationship = []
            for r in graduate:
                #print(r)
                resultRelationship = self.queryAll(dedent("""\
                    SELECT id AS codigo
                    FROM public.eguc_patentes
                    WHERE egresado_id = %s"""),[r['id']])

                item = {"egresado": r['nombreusuario'], "patentes": resultRelationship}
                resultRelationshipGraduatePatents.append(item)

            resultJobs = self.queryAll(dedent("""\
                SELECT id AS codigo, "nombreEmpresa", cargo, descripcion
                FROM public.eguc_trabajos
                WHERE fecha_actualizacion > %s"""), [date_update])
            
            resultRelationshipGraduateJobs = []
            resultRelationship = []
            for r in graduate:
                #print(r)
                resultRelationship = self.queryAll(dedent("""\
                    SELECT id AS codigo
                    FROM public.eguc_trabajos
                    WHERE egresado_id = %s"""),[r['id']])

                item = {"egresado": r['nombreusuario'], "trabajos": resultRelationship}
                resultRelationshipGraduateJobs.append(item)

            resultVolunteering = self.queryAll(dedent("""\
                SELECT id AS codigo, organizacion, descripcion, causa
                FROM public.eguc_voluntariado
                WHERE fecha_actualizacion > %s"""), [date_update])

            resultRelationshipGraduateVolunteering = []
            resultRelationship = []
            for r in graduate:
                #print(r)
                resultRelationship = self.queryAll(dedent("""\
                    SELECT id AS codigo
                    FROM public.eguc_voluntariado
                    WHERE egresado_id = %s"""),[r['id']])

                item = {"egresado": r['nombreusuario'], "voluntariado": resultRelationship}
                resultRelationshipGraduateVolunteering.append(item)


            response = {
                "dim-egresado": {"items": resultGraduate},
                "dim-estudiosuc": {"items": resultStudiosUc},
                "dim-certificacion": {"items": resultCertification},
                "dim-cursos": {"items": resultCourse},
                "dim-educacion": {"items": resultEducation},
                "dim-patentes": {"items": resultPatents},
                "dim-trabajos": {"items": resultJobs},
                "dim-voluntariado": {"items": resultVolunteering},
                "hechos-egresado-estudiosuc": {"items": resultRelationshipGraduateStudiosUc},
                "hechos-egresado-certificacion": {"items": resultRelationshipGraduateCertification},
                "hechos-egresado-cursos": {"items": resultRelationshipGraduateCourse},
                "hechos-egresado-educacion": {"items": resultRelationshipGraduateEducation},
                "hechos-egresado-patentes": {"items": resultRelationshipGraduatePatents},
                "hechos-egresado-trabajos": {"items": resultRelationshipGraduateJobs},
                "hechos-egresado-voluntariado": {"items": resultRelationshipGraduateVolunteering}
            }  
           
        except DatabaseError as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return jsonify(response), 200, { 'Access-Control-Allow-Origin': '*' }