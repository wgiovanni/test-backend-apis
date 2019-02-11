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
            '''
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
            '''
            response = {
                "dim-egresado": {
                    "status":"Ok",
                    "items": [
                        {
                            "primernombre": "Genessis",
                            "primerapellido": "Jimenez",
                            "email": "gjimenez@gmail,com",
                            "telefono": "04127658802",
                            "identificacion": "2464987",
                            "codigo": 1,
                            "confianza": 10, 
                            "validado": True
                        },
                        {
                            "primernombre": "Luis",
                            "primerapellido": "Gomez",
                            "email": "luisgomez@gmail,com",
                            "telefono": "04127658802",
                            "identificacion": "756438457",
                            "codigo": 2,
                            "confianza": 30, 
                            "validado": True
                        },
                        {
                            "primernombre": "Winder",
                            "primerapellido": "Morillo",
                            "email": "wmorillo@gmail,com",
                            "telefono": "746574323",
                            "identificacion": "146498766",
                            "codigo": 3,
                            "confianza": 40, 
                            "validado": True
                        },
                        {
                            "primernombre": "Wilkel",
                            "primerapellido": "Giovanni",
                            "email": "wgiovanni@gmail,com",
                            "telefono": "746574323",
                            "identificacion": "22422883",
                            "codigo": 4,
                            "confianza": 50, 
                            "validado": False
                        },
                        {
                            "primernombre": "fgdf",
                            "primerapellido": "Giovanni",
                            "email": "wgiovanni@gmail,com",
                            "telefono": "746574323",
                            "identificacion": "324234",
                            "codigo": 5,
                            "confianza": 60, 
                            "validado": True
                        },
                        {
                            "primernombre": "Freddy ",
                            "primerapellido": "Duran",
                            "email": "fduran@gmail,com",
                            "telefono": "04127658802",
                            "identificacion": "65348",
                            "codigo": 7,
                            "confianza": 90, 
                            "validado": True
                        },
                        {
                            "primernombre": "Geraldine ",
                            "primerapellido": "Herrera",
                            "email": "gherrera@gmail,com",
                            "telefono": "04127658802",
                            "identificacion": "098644",
                            "codigo": 8,
                            "confianza": 60, 
                            "validado": True
                        },
                        {
                            "primernombre": "Jordan ",
                            "primerapellido": "Herrera",
                            "email": "jherrera@gmail,com",
                            "telefono": "04127658802",
                            "identificacion": "827262",
                            "codigo": 9,
                            "confianza": 10, 
                            "validado": True
                        },
                        {
                            "primernombre": "Andrea ",
                            "primerapellido": "Da Silva",
                            "email": "adasilva@gmail,com",
                            "telefono": "04127658802",
                            "identificacion": "123432384",
                            "codigo": 10,
                            "confianza": 35, 
                            "validado": True
                        }
                    ]
                },
                "dim-estudiosuc": {
                    "status":"Ok",
                    "items": [
                        {
                            "egresado": 1,
                            "codigo": 1,
                            "facultad": "FACYT",
                            "anhogrado": "2018-07-24",
                            "titulo": "Licenciado en Computación",
                            "urlcertificacion": "url..."
                        },
                        {
                            "egresado": 2,
                            "codigo": 2,
                            "facultad": "FACYT",
                            "anhogrado": "2018-07-26",
                            "titulo": "Licenciado en Física",
                            "urlcertificacion": "url..."
                        },
                        {
                            "egresado": 3,
                            "codigo": 3,
                            "facultad": "FACYT",
                            "anhogrado": "2018-07-24",
                            "titulo": "Licenciado en Computación",
                            "urlcertificacion": "url..."
                        },
                        {
                            "egresado": 4,
                            "codigo": 4,
                            "facultad": "FACYT",
                            "anhogrado": "2010-07-24",
                            "titulo": "Licenciado en Química",
                            "urlcertificacion": "url..."
                        },
                        {
                            "egresado": 4,
                            "codigo": 5,
                            "facultad": "FACES",
                            "anhogrado": "2010-07-24",
                            "titulo": "Licenciado en Química",
                            "urlcertificacion": "url..."
                        },
                        {
                            "egresado": 5,
                            "codigo": 6,
                            "facultad": "FCJP",
                            "anhogrado": "2013-07-24",
                            "titulo": "Derecho",
                            "urlcertificacion": "url..."
                        },
                        {
                            "egresado": 6,
                            "codigo": 7,
                            "facultad": "FACY",
                            "anhogrado": "2018-07-24",
                            "titulo": "Licenciado en Computación",
                            "urlcertificacion": "url..."
                        },
                        {
                            "egresado": 7,
                            "codigo": 8,
                            "facultad": "ODONTOLOGIA",
                            "anhogrado": "2018-07-24",
                            "titulo": "ODONTOLOGIA",
                            "urlcertificacion": "url..."
                        },
                        {
                            "egresado": 8,
                            "codigo": 9,
                            "facultad": "ODONTOLOGIA",
                            "anhogrado": "2019-07-24",
                            "titulo": "ODONTOLOGIA",
                            "urlcertificacion": "url..."
                        },
                        {
                            "egresado": 9,
                            "codigo": 10,
                            "facultad": "INGENIERIA",
                            "anhogrado": "2019-07-24",
                            "titulo": "INGENIERIA",
                            "urlcertificacion": "url..."
                        }
                    ]
                },
                "dim-trabajos": {
                    "items": [
                        {
                            "egresado": 1,
                            "codigo": 1,
                            "nombreempresa": "Intelix",
                            "cargo": "Programador web",
                            "descripcion": "descripcion",
                            "url": "url",
                            "fecha": "2018-09-22",
                            "laborando": False
                        },
                        {
                            "egresado": 1,
                            "codigo": 2,
                            "nombreempresa": "Promotora Tantalo",
                            "cargo": "Programador web",
                            "descripcion": "descripcion",
                            "url": "url",
                            "fecha": "2018-09-22",
                            "laborando": True
                        },
                        {
                            "egresado": 2,
                            "codigo": 3,
                            "nombreempresa": "Sofos",
                            "cargo": "Programador web",
                            "descripcion": "descripcion",
                            "url": "url",
                            "fecha": "2018-09-22",
                            "laborando": True
                        },
                        {
                            "egresado": 3,
                            "codigo": 4,
                            "nombreempresa": "Intelix",
                            "cargo": "Programador web",
                            "descripcion": "descripcion",
                            "url": "url",
                            "fecha": "2018-09-22",
                            "laborando": False
                        },
                        {
                            "egresado": 3,
                            "codigo": 5,
                            "nombreempresa": "Promotora Tantalo",
                            "cargo": "Programador web",
                            "descripcion": "descripcion",
                            "url": "url",
                            "fecha": "2018-09-22",
                            "laborando": True
                        },
                        {
                            "egresado": 3,
                            "codigo": 6,
                            "nombreempresa": "Sofos",
                            "cargo": "Programador web",
                            "descripcion": "descripcion",
                            "url": "url",
                            "fecha": "2018-09-22",
                            "laborando": False
                        },
                        {
                            "egresado": 4,
                            "codigo": 7,
                            "nombreempresa": "Sofos",
                            "cargo": "Programador web",
                            "descripcion": "descripcion",
                            "url": "url",
                            "fecha": "2018-09-22",
                            "laborando": True
                        },
                        {
                            "egresado": 5,
                            "codigo": 8,
                            "nombreempresa": "Promotora Tantalo",
                            "cargo": "Programador web",
                            "descripcion": "descripcion",
                            "url": "url",
                            "fecha": "2018-09-22",
                            "laborando": True
                        },
                        {
                            "egresado": 6,
                            "codigo": 8,
                            "nombreempresa": "Promotora Tantalo",
                            "cargo": "Programador web",
                            "descripcion": "descripcion",
                            "url": "url",
                            "fecha": "2018-09-22",
                            "laborando": True
                        },
                        {
                            "egresado": 7,
                            "codigo": 9,
                            "nombreempresa": "CLX SAMSUNG",
                            "cargo": "Programador web",
                            "descripcion": "descripcion",
                            "url": "url",
                            "fecha": "2018-09-22",
                            "laborando": True
                        },
                        {
                            "egresado": 8,
                            "codigo": 11,
                            "nombreempresa": "INNOVA",
                            "cargo": "Programador web",
                            "descripcion": "descripcion",
                            "url": "url",
                            "fecha": "2018-09-22",
                            "laborando": False
                        },
                        {
                            "egresado": 8,
                            "codigo": 12,
                            "nombreempresa": "NAVICU",
                            "cargo": "Programador web",
                            "descripcion": "descripcion",
                            "url": "url",
                            "fecha": "2018-09-22",
                            "laborando": True
                        },
                        {
                            "egresado": 9,
                            "codigo": 13,
                            "nombreempresa": "INNOVA",
                            "cargo": "Programador web",
                            "descripcion": "descripcion",
                            "url": "url",
                            "fecha": "2018-09-22",
                            "laborando": True
                        },
                        {
                            "egresado": 10,
                            "codigo": 14,
                            "nombreempresa": "NAVICU",
                            "cargo": "Programador web",
                            "descripcion": "descripcion",
                            "url": "url",
                            "fecha": "2018-09-22",
                            "laborando": True
                        }
                    ]
                }
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