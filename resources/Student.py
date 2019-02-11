from flask_restful import abort, Resource, reqparse
import simplejson as json
from psycopg2 import DatabaseError
from textwrap import dedent
from common.BD import BD
from flask import make_response, jsonify, request
from datetime import datetime


class StudentInsertInitial(BD, Resource):
    representations = {'application/json': make_response}
    parser = reqparse.RequestParser()

    def get(self):
        try:
            '''
            # consultar facultad
            resultfaculty = self.queryAll(dedent("""SELECT nombre FROM facultad"""))

            # consultar carrera
            resultProfession = self.queryAll(dedent("""SELECT nombre, tipo FROM carrera"""))

            # consultar estudiantes
            resultStudent = self.queryAll(dedent("""\
            SELECT e.cedula, e.nacionalidad, e.nombre, e.apellido, e.sexo, e.fecha_nacimiento, 
            e.telefono1, e.telefono2, e.correo, e.edo_procedencia, e.etnia, e.discapacidad, s.status, tipo
            FROM estudiante AS e
            INNER JOIN estatusestudiante AS s 
            ON (e.id_statusestudiante = s.id)"""))
            studentList = []
            for row in resultStudent:
                row['fecha_nacimiento'] = row['fecha_nacimiento'].strftime('%Y-%m-%d')
                studentList.append(row)
            resultStudent = studentList

            # consultar relaciones
            resultRelationship = self.queryAll(dedent("""\
            SELECT e.cedula AS estudiante, c.nombre AS carrera, f.nombre AS facultad
	        FROM estudiante AS e 
	        INNER JOIN carrera AS c ON (e.id_carrera = c.id)
	        INNER JOIN facultad AS f ON (c.id_facultad = f.id)"""))
            print(resultRelationship)     
            response = {
                "hechos-estudiante-carrera-facultad": {"items": resultRelationship},
                "dim-facultad": {"items": resultfaculty}, 
                "dim-carrera": {"items":resultProfession}, 
                "dim-estudiante": {"items": resultStudent} 
                
            }
            '''
            response = {
                "hechos-estudiante-carrera-facultad": {
                    "items": [
                        {
                            "estudiante": "26011707",
                            "carrera": "COMPUTACION",
                            "facultad": "FACYT"
                        },
                        {
                            "estudiante": "22422883",
                            "carrera": "COMPUTACION",
                            "facultad": "FACYT"
                        },
                        {
                            "estudiante": "27855129",
                            "carrera": "QUIMICA",
                            "facultad": "FACYT"
                        },
                        {
                            "estudiante": "13381615",
                            "carrera": "FISICA",
                            "facultad": "FACYT"
                        },
                        {
                            "estudiante": "22345223",
                            "carrera": "MATEMATICA",
                            "facultad": "FACYT"
                        },
                        {
                            "estudiante": "22345243",
                            "carrera": "MATEMATICA",
                            "facultad": "FACYT"
                        },
                        {
                            "estudiante": "123456789",
                            "carrera": "MEDICINA",
                            "facultad": "FCS"
                        },
                        {
                            "estudiante": "123456789",
                            "carrera": "MEDICINA",
                            "facultad": "FCS"
                        },
                        {
                            "estudiante": "0983653",
                            "carrera": "BIOANALISIS",
                            "facultad": "FCS"
                        },
                        {
                            "estudiante": "32424",
                            "carrera": "ENFERMERIA EN GERIATRIA Y GERONTOLOGIA",
                            "facultad": "FCS"
                        },
                        {
                            "estudiante": "3245959524",
                            "carrera": "ESPECIALIZACION EN DESARROLLO DE SOFTWARE",
                            "facultad": "FACYT"
                        },
                        {
                            "estudiante": "12",
                            "carrera": "ESPECIALIZACION EN DESARROLLO DE SOFTWARE",
                            "facultad": "FCJP"
                        }
                    ]
                },
                "dim-carrera": {
                    "items": [
                        {
                            "nombre": "COMPUTACION"
                        },
                        {
                            "nombre": "QUIMICA"
                        },
                        {
                            "nombre": "FISICA"
                        },
                        {
                            "nombre": "MATEMATICA"
                        },
                        {
                            "nombre": "BIOLOGIA"
                        },
                        {
                            "nombre": "BIOANALISIS"
                        },
                        {
                            "nombre": "MEDICINA"
                        },
                        {
                            "nombre": "ENFERMERIA EN GERIATRIA Y GERONTOLOGIA"
                        },
                        {
                            "nombre": "ESPECIALIZACION EN DESARROLLO DE SOFTWARE"
                        },
                        {
                            "nombre": "DERECHO"
                        }
                    ]
                },
                "dim-estudiante": {
                    "items": [
                        {
                            "cedula": "22422883",
                            "nacionalidad": "v",
                            "nombre": "Wilkel",
                            "apellido": "Apellido",
                            "sexo": "f",
                            "fecha_nacimiento": "1995-05-24",
                            "telefono1": "0412-76558802",
                            "telefono2": "0245-3351406",
                            "correo": "wilkelgiovanni@gmail.com",
                            "edo_procedencia": "Carabobo",
                            "etnia": "NO PERTENEZCO A UN PUEBLO INDIGENA",
                            "discapacidad": "NO POSEO NINGUNA DISCAPACIDAD",
                            "status": 0,
                            "tipo": 1,
                            "ano": "2014"
                        },
                        {
                            "cedula": "27855129",
                            "nacionalidad": "e",
                            "nombre": "Ana",
                            "apellido": "Sanchez",
                            "sexo": "F",
                            "fecha_nacimiento": "1999-09-22",
                            "telefono1": "0241-8481233",
                            "telefono2": "0426-3437317",
                            "correo": "anasanchez@gmail.com",
                            "edo_procedencia": "Carabobo",
                            "etnia": "NO PERTENEZCO A UN PUEBLO INDIGENA",
                            "discapacidad": "NO POSEO NINGUNA DISCAPACIDAD",
                            "status": 0,
                            "tipo": 0,
                            "ano": "2012"
                        },
                        {
                            "cedula": "26011707",
                            "nacionalidad": "E",
                            "nombre": "Alba",
                            "apellido": "Silva",
                            "sexo": "F",
                            "fecha_nacimiento": "1997-03-01",
                            "telefono1": "0241-2051334",
                            "telefono2": "0412-1308522",
                            "correo": "andreadellepere_3@hotmail.com",
                            "edo_procedencia": "Carabobo",
                            "etnia": "YANOMAMI",
                            "discapacidad": "SI POSEO DISCAPACIDAD",
                            "status": 1,
                            "tipo": 1,
                            "ano": "2015"
                        },
                        {
                            "cedula": "13381615",
                            "nacionalidad": "v",
                            "nombre": "Luis",
                            "apellido": "Servita",
                            "sexo": "f",
                            "fecha_nacimiento": "1976-07-07",
                            "telefono1": "02418140120",
                            "telefono2": "04265413615",
                            "correo": "luisservita777@gmail.com",
                            "edo_procedencia": "Carabobo",
                            "etnia": "NO PERTENEZCO A UN PUEBLO INDIGENA",
                            "discapacidad": "NO POSEO NINGUNA DISCAPACIDAD",
                            "status": 0,
                            "tipo": 1,
                            "ano": "2013"
                        },
                        {
                            "cedula": "22345243",
                            "nacionalidad": "V",
                            "nombre": "Alejandro2",
                            "apellido": "Giovanni2",
                            "sexo": "m",
                            "fecha_nacimiento": "1995-05-24",
                            "telefono1": "0215545",
                            "telefono2": "155455515",
                            "correo": "alejandro2@gmail.com",
                            "edo_procedencia": "Carabobo",
                            "etnia": "TIMOTO-CUICAS/TIMOTES",
                            "discapacidad": "NO POSEO NINGUNA DISCAPACIDAD",
                            "status": 1,
                            "tipo": 0,
                            "ano": "2010"
                        },
                        {
                            "cedula": "22345223",
                            "nacionalidad": "V",
                            "nombre": "Alejandro",
                            "apellido": "Giovanni",
                            "sexo": "M",
                            "fecha_nacimiento": "1995-05-24",
                            "telefono1": "0215545",
                            "telefono2": "155455515",
                            "correo": "alejandro@gmail.com",
                            "edo_procedencia": "Carabobo",
                            "etnia": "NO PERTENEZCO A UN PUEBLO INDIGENA",
                            "discapacidad": "SI POSEO DISCAPACIDAD",
                            "status": 1,
                            "tipo": 1,
                            "ano": "2011"
                        },
                        {
                            "cedula": "123456789",
                            "nacionalidad": "V",
                            "nombre": "Alejandro",
                            "apellido": "Giovanni",
                            "sexo": "M",
                            "fecha_nacimiento": "1995-05-24",
                            "telefono1": "0215545",
                            "telefono2": "155455515",
                            "correo": "alejandro@gmail.com",
                            "edo_procedencia": "Carabobo",
                            "etnia": "NO PERTENEZCO A UN PUEBLO INDIGENA",
                            "discapacidad": "SI POSEO DISCAPACIDAD",
                            "status": 1,
                            "tipo": 0,
                            "ano": "2010"
                        },
                        {
                            "cedula": "0983653",
                            "nacionalidad": "V",
                            "nombre": "Alejandro",
                            "apellido": "Giovanni",
                            "sexo": "M",
                            "fecha_nacimiento": "1995-05-24",
                            "telefono1": "0215545",
                            "telefono2": "155455515",
                            "correo": "alejandro@gmail.com",
                            "edo_procedencia": "Carabobo",
                            "etnia": "NO PERTENEZCO A UN PUEBLO INDIGENA",
                            "discapacidad": "SI POSEO DISCAPACIDAD",
                            "status": 0,
                            "tipo": 0,
                            "ano": "2014"
                        },
                        {
                            "cedula": "32424",
                            "nacionalidad": "V",
                            "nombre": "Alejandro",
                            "apellido": "Giovanni",
                            "sexo": "M",
                            "fecha_nacimiento": "1995-05-24",
                            "telefono1": "0215545",
                            "telefono2": "155455515",
                            "correo": "alejandro@gmail.com",
                            "edo_procedencia": "Carabobo",
                            "etnia": "OTRA cosa",
                            "discapacidad": "NO POSEO DISCAPACIDAD",
                            "status": 0,
                            "tipo": 1,
                            "ano": "2012"
                        },
                        {
                            "cedula": "3245959524",
                            "nacionalidad": "V",
                            "nombre": "Alejandro",
                            "apellido": "Giovanni",
                            "sexo": "M",
                            "fecha_nacimiento": "1995-05-24",
                            "telefono1": "0215545",
                            "telefono2": "155455515",
                            "correo": "alejandro@gmail.com",
                            "edo_procedencia": "Carabobo",
                            "etnia": "OTRA cosa",
                            "discapacidad": "otroa cosa",
                            "status": 0,
                            "tipo": 1,
                            "ano": "2013"
                        },
                        {
                            "cedula": "12",
                            "nacionalidad": "V",
                            "nombre": "jose",
                            "apellido": "dsd",
                            "sexo": "M",
                            "fecha_nacimiento": "1995-05-24",
                            "telefono1": "0215545",
                            "telefono2": "322",
                            "correo": "alejandro@gmail.com",
                            "edo_procedencia": "Carabobo",
                            "etnia": "",
                            "discapacidad": "",
                            "status": 0,
                            "tipo": 0,
                            "ano": "2013"
                        }
                    ]
                }
            }  
        except DatabaseError as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return json.dumps(response), 200, { 'Access-Control-Allow-Origin': '*' }

        
        
class StudentUpdate(BD, Resource):
    representations = {'application/json': make_response}
    parser = reqparse.RequestParser()
    
    def get(self, date_update):

        try:
            date_update = datetime.strptime(date_update, '%Y-%m-%d %H:%M:%S')
            print(date_update)
            '''
            # consultar facultad
            resultfaculty = self.queryAll(dedent("""SELECT nombre FROM facultad WHERE fecha_actualizacion >= %s"""), [date_update])
            # consultar carrera
            resultProfession = self.queryAll(dedent("""SELECT nombre, tipo FROM carrera WHERE fecha_actualizacion >= %s"""), [date_update])

            # consultar estudiantes
            resultStudent = self.queryAll(dedent("""\
            SELECT e.cedula, e.nacionalidad, e.nombre, e.apellido, e.sexo, e.fecha_nacimiento, 
            e.telefono1, e.telefono2, e.correo, e.edo_procedencia, e.etnia, e.discapacidad, s.status, tipo
            FROM estudiante AS e
            INNER JOIN estatusestudiante AS s 
            ON (e.id_statusestudiante = s.id)
            WHERE e.fecha_actualizacion >= %s"""), [date_update])
            studentList = []
            for row in resultStudent:
                row['fecha_nacimiento'] = row['fecha_nacimiento'].strftime('%Y-%m-%d')
                studentList.append(row)
            resultStudent = studentList
            print(resultStudent)
            # consultar relaciones
            resultRelationship = self.queryAll(dedent("""\
            SELECT e.cedula AS estudiante, c.nombre AS carrera, f.nombre AS facultad
	        FROM estudiante AS e 
	        INNER JOIN carrera AS c ON (e.id_carrera = c.id)
	        INNER JOIN facultad AS f ON (c.id_facultad = f.id)"""))
            response = {
                "hechos-estudiante-carrera-facultad": {"items": resultRelationship},
                "dim-facultad": {"items": resultfaculty}, 
                "dim-carrera": {"items":resultProfession}, 
                "dim-estudiante": {"items": resultStudent}
            } 
            ''' 
            response = {
                "hechos-estudiante-carrera-facultad": {
                    "items": [
                        {
                            "estudiante": "26011707",
                            "carrera": "COMPUTACION",
                            "facultad": "FACYT"
                        },
                        {
                            "estudiante": "22422883",
                            "carrera": "COMPUTACION",
                            "facultad": "FACYT"
                        },
                        {
                            "estudiante": "27855129",
                            "carrera": "QUIMICA",
                            "facultad": "FACYT"
                        },
                        {
                            "estudiante": "13381615",
                            "carrera": "FISICA",
                            "facultad": "FACYT"
                        },
                        {
                            "estudiante": "22345223",
                            "carrera": "MATEMATICA",
                            "facultad": "FACYT"
                        },
                        {
                            "estudiante": "22345243",
                            "carrera": "MATEMATICA",
                            "facultad": "FACYT"
                        },
                        {
                            "estudiante": "123456789",
                            "carrera": "MEDICINA",
                            "facultad": "FCS"
                        },
                        {
                            "estudiante": "123456789",
                            "carrera": "MEDICINA",
                            "facultad": "FCS"
                        },
                        {
                            "estudiante": "0983653",
                            "carrera": "BIOANALISIS",
                            "facultad": "FCS"
                        },
                        {
                            "estudiante": "32424",
                            "carrera": "ENFERMERIA EN GERIATRIA Y GERONTOLOGIA",
                            "facultad": "FCS"
                        },
                        {
                            "estudiante": "3245959524",
                            "carrera": "ESPECIALIZACION EN DESARROLLO DE SOFTWARE",
                            "facultad": "FACYT"
                        },
                        {
                            "estudiante": "12",
                            "carrera": "DERECHO",
                            "facultad": "FCJP"
                        },
                        {
                            "estudiante": "22",
                            "carrera": "DERECHO",
                            "facultad": "FCJP"
                        },
                        {
                            "estudiante": "24",
                            "carrera": "EDUCACION, MENCION FRANCES",
                            "facultad": "FACE"
                        },
                        {
                            "estudiante": "25",
                            "carrera": "EDUCACION, MENCION ARTES PLASTICAS",
                            "facultad": "FACE"
                        },
                        {
                            "estudiante": "26",
                            "carrera": "EDUCACION INTEGRAL",
                            "facultad": "FACE"
                        }
                    ]
                },
                "dim-carrera": {
                    "items": [
                        {
                            "nombre": "COMPUTACION"
                        },
                        {
                            "nombre": "QUIMICA"
                        },
                        {
                            "nombre": "FISICA"
                        },
                        {
                            "nombre": "MATEMATICA"
                        },
                        {
                            "nombre": "BIOLOGIA"
                        },
                        {
                            "nombre": "BIOANALISIS"
                        },
                        {
                            "nombre": "MEDICINA"
                        },
                        {
                            "nombre": "ENFERMERIA EN GERIATRIA Y GERONTOLOGIA"
                        },
                        {
                            "nombre": "ESPECIALIZACION EN DESARROLLO DE SOFTWARE"
                        },
                        {
                            "nombre": "DERECHO"
                        },
                        {
                            "nombre": "EDUCACION, MENCION ARTES PLASTICAS"
                        },
                        {
                            "nombre": "EDUCACION, MENCION FRANCES"
                        },
                        {
                            "nombre": "EDUCACION INTEGRAL"
                        }
                    ]
                },
                "dim-estudiante": {
                    "items": [
                        {
                            "cedula": "22422883",
                            "nacionalidad": "v",
                            "nombre": "Wilkel",
                            "apellido": "Apellido",
                            "sexo": "f",
                            "fecha_nacimiento": "1995-05-24",
                            "telefono1": "0412-76558802",
                            "telefono2": "0245-3351406",
                            "correo": "wilkelgiovanni@gmail.com",
                            "edo_procedencia": "Carabobo",
                            "etnia": "NO PERTENEZCO A UN PUEBLO INDIGENA",
                            "discapacidad": "NO POSEO NINGUNA DISCAPACIDAD",
                            "status": 0,
                            "tipo": 1,
                            "ano": "2014"
                        },
                        {
                            "cedula": "27855129",
                            "nacionalidad": "e",
                            "nombre": "Ana",
                            "apellido": "Sanchez",
                            "sexo": "F",
                            "fecha_nacimiento": "1999-09-22",
                            "telefono1": "0241-8481233",
                            "telefono2": "0426-3437317",
                            "correo": "anasanchez@gmail.com",
                            "edo_procedencia": "Carabobo",
                            "etnia": "NO PERTENEZCO A UN PUEBLO INDIGENA",
                            "discapacidad": "NO POSEO NINGUNA DISCAPACIDAD",
                            "status": 0,
                            "tipo": 0,
                            "ano": "2012"
                        },
                        {
                            "cedula": "26011707",
                            "nacionalidad": "E",
                            "nombre": "Alba",
                            "apellido": "Silva",
                            "sexo": "F",
                            "fecha_nacimiento": "1997-03-01",
                            "telefono1": "0241-2051334",
                            "telefono2": "0412-1308522",
                            "correo": "andreadellepere_3@hotmail.com",
                            "edo_procedencia": "Carabobo",
                            "etnia": "YANOMAMI",
                            "discapacidad": "SI POSEO DISCAPACIDAD",
                            "status": 1,
                            "tipo": 1,
                            "ano": "2015"
                        },
                        {
                            "cedula": "13381615",
                            "nacionalidad": "v",
                            "nombre": "Luis",
                            "apellido": "Servita",
                            "sexo": "f",
                            "fecha_nacimiento": "1976-07-07",
                            "telefono1": "02418140120",
                            "telefono2": "04265413615",
                            "correo": "luisservita777@gmail.com",
                            "edo_procedencia": "Carabobo",
                            "etnia": "NO PERTENEZCO A UN PUEBLO INDIGENA",
                            "discapacidad": "NO POSEO NINGUNA DISCAPACIDAD",
                            "status": 0,
                            "tipo": 1,
                            "ano": "2013"
                        },
                        {
                            "cedula": "22345243",
                            "nacionalidad": "V",
                            "nombre": "Alejandro2",
                            "apellido": "Giovanni2",
                            "sexo": "m",
                            "fecha_nacimiento": "1995-05-24",
                            "telefono1": "0215545",
                            "telefono2": "155455515",
                            "correo": "alejandro2@gmail.com",
                            "edo_procedencia": "Carabobo",
                            "etnia": "TIMOTO-CUICAS/TIMOTES",
                            "discapacidad": "NO POSEO NINGUNA DISCAPACIDAD",
                            "status": 1,
                            "tipo": 0,
                            "ano": "2010"
                        },
                        {
                            "cedula": "22345223",
                            "nacionalidad": "V",
                            "nombre": "Alejandro",
                            "apellido": "Giovanni",
                            "sexo": "M",
                            "fecha_nacimiento": "1995-05-24",
                            "telefono1": "0215545",
                            "telefono2": "155455515",
                            "correo": "alejandro@gmail.com",
                            "edo_procedencia": "Carabobo",
                            "etnia": "NO PERTENEZCO A UN PUEBLO INDIGENA",
                            "discapacidad": "SI POSEO DISCAPACIDAD",
                            "status": 1,
                            "tipo": 1,
                            "ano": "2011"
                        },
                        {
                            "cedula": "123456789",
                            "nacionalidad": "V",
                            "nombre": "Alejandro",
                            "apellido": "Giovanni",
                            "sexo": "M",
                            "fecha_nacimiento": "1995-05-24",
                            "telefono1": "0215545",
                            "telefono2": "155455515",
                            "correo": "alejandro@gmail.com",
                            "edo_procedencia": "Carabobo",
                            "etnia": "NO PERTENEZCO A UN PUEBLO INDIGENA",
                            "discapacidad": "SI POSEO DISCAPACIDAD",
                            "status": 1,
                            "tipo": 0,
                            "ano": "2010"
                        },
                        {
                            "cedula": "0983653",
                            "nacionalidad": "V",
                            "nombre": "Alejandro",
                            "apellido": "Giovanni",
                            "sexo": "M",
                            "fecha_nacimiento": "1995-05-24",
                            "telefono1": "0215545",
                            "telefono2": "155455515",
                            "correo": "alejandro@gmail.com",
                            "edo_procedencia": "Carabobo",
                            "etnia": "NO PERTENEZCO A UN PUEBLO INDIGENA",
                            "discapacidad": "SI POSEO DISCAPACIDAD",
                            "status": 0,
                            "tipo": 0,
                            "ano": "2014"
                        },
                        {
                            "cedula": "32424",
                            "nacionalidad": "V",
                            "nombre": "Alejandro",
                            "apellido": "Giovanni",
                            "sexo": "M",
                            "fecha_nacimiento": "1995-05-24",
                            "telefono1": "0215545",
                            "telefono2": "155455515",
                            "correo": "alejandro@gmail.com",
                            "edo_procedencia": "Carabobo",
                            "etnia": "OTRA cosa",
                            "discapacidad": "NO POSEO NINGUNA DISCAPACIDAD",
                            "status": 0,
                            "tipo": 1,
                            "ano": "2012"
                        },
                        {
                            "cedula": "3245959524",
                            "nacionalidad": "V",
                            "nombre": "Alejandro",
                            "apellido": "Giovanni",
                            "sexo": "M",
                            "fecha_nacimiento": "1995-05-24",
                            "telefono1": "0215545",
                            "telefono2": "155455515",
                            "correo": "alejandro@gmail.com",
                            "edo_procedencia": "Carabobo",
                            "etnia": "OTRA cosa",
                            "discapacidad": "otroa cosa",
                            "status": 0,
                            "tipo": 1,
                            "ano": "2013"
                        },
                        {
                            "cedula": "12",
                            "nacionalidad": "V",
                            "nombre": "jose",
                            "apellido": "dsd",
                            "sexo": "M",
                            "fecha_nacimiento": "1995-05-24",
                            "telefono1": "0215545",
                            "telefono2": "322",
                            "correo": "alejandro@gmail.com",
                            "edo_procedencia": "Carabobo",
                            "etnia": "",
                            "discapacidad": "",
                            "status": 0,
                            "tipo": 0,
                            "ano": "2013"
                        },
                        {
                            "cedula": "22",
                            "nacionalidad": "V",
                            "nombre": "jose",
                            "apellido": "dsd",
                            "sexo": "M",
                            "fecha_nacimiento": "1995-05-24",
                            "telefono1": "0215545",
                            "telefono2": "322",
                            "correo": "alejandro@gmail.com",
                            "edo_procedencia": "Carabobo",
                            "etnia": "",
                            "discapacidad": "",
                            "status": 0,
                            "tipo": 0,
                            "ano": "2013"
                        },
                        {
                            "cedula": "24",
                            "nacionalidad": "e",
                            "nombre": "jose",
                            "apellido": "dsd",
                            "sexo": "M",
                            "fecha_nacimiento": "1995-05-24",
                            "telefono1": "0215545",
                            "telefono2": "322",
                            "correo": "alejandro@gmail.com",
                            "edo_procedencia": "Carabobo",
                            "etnia": "",
                            "discapacidad": "NO POSEO NINGUNA DISCAPACIDAD",
                            "status": 0,
                            "tipo": 0,
                            "ano": "2016"
                        },
                        {
                            "cedula": "25",
                            "nacionalidad": "E",
                            "nombre": "jose",
                            "apellido": "dsd",
                            "sexo": "f",
                            "fecha_nacimiento": "1995-05-24",
                            "telefono1": "0215545",
                            "telefono2": "322",
                            "correo": "alejandro@gmail.com",
                            "edo_procedencia": "Carabobo",
                            "etnia": "NO PERTENEZCO A UN PUEBLO INDIGENA",
                            "discapacidad": "NO POSEO NINGUNA DISCAPACIDAD",
                            "status": 0,
                            "tipo": 0,
                            "ano": "2016"
                        },
                        {
                            "cedula": "26",
                            "nacionalidad": "E",
                            "nombre": "juan",
                            "apellido": "dsd",
                            "sexo": "m",
                            "fecha_nacimiento": "1995-05-24",
                            "telefono1": "0215545",
                            "telefono2": "322",
                            "correo": "alejandro@gmail.com",
                            "edo_procedencia": "Carabobo",
                            "etnia": "NO PERTENEZCO A UN PUEBLO INDIGENA",
                            "discapacidad": "NO POSEO NINGUNA DISCAPACIDAD",
                            "status": 1,
                            "tipo": 0,
                            "ano": "2016"
                        },
                    ]
                }
            }  
        except DatabaseError as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return jsonify(response), 200, { 'Access-Control-Allow-Origin': '*' }



    

