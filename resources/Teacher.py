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
            '''
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
            ''' 
            response = {
                "dim-docente": {
                    "items": [
                        {
                            "cedula": "11356034",
                            "primernombre": "Mirella",
                            "segundonombre": "Segundo",
                            "primerapellido": "Herrera",
                            "segundoapellido": "Segundo",
                            "correo": "mirella.herrera@gmail.com",
                            "areadeinvestigacion": "investigacion",
                            "sexo": "F",
                            "nacionalidad": "V",
                            "facultad": "FACYT",
                            "tipo": "Investigador",
                            "escalafon": "Titular"
                        },
                        {
                            "cedula": "1515515",
                            "primernombre": "Dessiree",
                            "primerapellido": "Delgado",
                            "correo": "desidelgado@gmail.com",
                            "areadeinvestigacion": "investigacion",
                            "sexo": "F",
                            "nacionalidad": "V",
                            "segundonombre": "SegundoNombre",
                            "segundoapellido": "Segundoapellido",
                            "facultad": "FACYT",
                            "tipo": "Investigador",
                            "escalafon": "Titular"
                        },
                        {
                            "cedula": "545511",
                            "primernombre": "Marilyn",
                            "primerapellido": "Guigni",
                            "correo": "marilyngiugni@gmail.com",
                            "areadeinvestigacion": "investigacion",
                            "sexo": "F",
                            "nacionalidad": "V",
                            "segundonombre": "SegundoNombre",
                            "segundoapellido": "Segundoapellido",
                            "facultad": "FACYT",
                            "tipo": "Investigador",
                            "escalafon": "Asociado"
                        },
                        {
                            "cedula": "226555",
                            "primernombre": "Pedro",
                            "primerapellido": "Linares",
                            "correo": "pedro@gmail.com",
                            "areadeinvestigacion": "investigacion",
                            "sexo": "M",
                            "nacionalidad": "E",
                            "segundonombre": "SegundoNombre",
                            "segundoapellido": "Segundoapellido",
                            "facultad": "Ingeniería",
                            "tipo": "Contratado",
                            "escalafon": "Asociado"
                        },
                        {
                            "cedula": "123456788",
                            "primernombre": "Alguien ahi",
                            "primerapellido": "Alguien ahi",
                            "correo": "alguienahi@gmail.com",
                            "areadeinvestigacion": "investigacion",
                            "sexo": "f",
                            "nacionalidad": "e",
                            "segundonombre": "SegundoNombre",
                            "segundoapellido": "Segundoapellido",
                            "facultad": "ODONTOLOGIA",
                            "tipo": "Normal",
                            "escalafon": "Asistente"
                        },
                        {
                            "cedula": "65",
                            "primernombre": "Afddgd",
                            "primerapellido": "Adfgdi",
                            "correo": "alguienahi@gmail.com",
                            "areadeinvestigacion": "derecho penal",
                            "sexo": "f",
                            "nacionalidad": "e",
                            "segundonombre": "SegundoNombre",
                            "segundoapellido": "Segundoapellido",
                            "facultad": "FCJP",
                            "tipo": "Normal",
                            "escalafon": "Titular"
                        }
                    ]
                },
                "dim-otro-estudio": {
                    "items": [
                        {
                            "codigo": "valor",
                            "nomtitulo": "valor"
                        }
                    ]
                },
                "dim-publicacion": {
                    "items": [
                        {
                            "codigo": 4,
                            "titulopublicacion": "Titulo de la publicacion2",
                            "urlcitacion": "http://dhcvhzvgvgvgvz.com",
                            "urlpublicacion": "http://aquiseencuentra.com",
                            "numerocitaciones": 50
                        },
                        {
                            "codigo": 6,
                            "titulopublicacion": "Titulo de la publicacion2",
                            "urlcitacion": "http://dhcvhzvgvgvgvz.com",
                            "urlpublicacion": "http://aquiseencuentra.com",
                            "numerocitaciones": 75
                        },
                        {
                            "codigo": 7,
                            "titulopublicacion": "Titulo de la publicacion3",
                            "urlcitacion": "http://dhcvhzvgvgvgvz.com",
                            "urlpublicacion": "http://aquiseencuentra.com",
                            "numerocitaciones": 500
                        },
                        {
                            "codigo": 8,
                            "titulopublicacion": "Titulo de la publicacion4",
                            "urlcitacion": "http://dhcvhzvgvgvgvz.com",
                            "urlpublicacion": "http://aquiseencuentra.com",
                            "numerocitaciones": 22
                        },
                        {
                            "codigo": 9,
                            "titulopublicacion": "Titulo de la publicacion5",
                            "urlcitacion": "http://dhcvhzvgvgvgvz.com",
                            "urlpublicacion": "http://aquiseencuentra.com",
                            "numerocitaciones": 43
                        },
                        {
                            "codigo": 10,
                            "titulopublicacion": "Titulo de la publicacion6",
                            "urlcitacion": "http://dhcvhzvgvgvgvz.com",
                            "urlpublicacion": "http://aquiseencuentra.com",
                            "numerocitaciones": 873
                        }
                    ]
                },
                "dim-proyecto": {
                    "items": [
                        {
                            "codigo": "valor",
                            "titulo": "valor"
                        }
                    ]
                },
                "dim-titulo": {
                    "items": [
                        {
                            "codigo": 3,
                            "nomtitulo": "Licenciado en Computacion"
                        },
                        {
                            "codigo": 4,
                            "nomtitulo": "Ingeniera"
                        },
                        {
                            "codigo": 5,
                            "nomtitulo": "Licenciado en Computacion"
                        },
                        {
                            "codigo": 6,
                            "nomtitulo": "Ingeniera"
                        }
                    ]
                },
                "dim-premio": {
                    "items": [
                        {
                            "codigo": "valor",
                            "nombre": "valor"
                        }
                    ]
                },
                "hechos-docente-otroestudio": {
                    "items": [
                        {
                            "docente": "valor",
                            "otroestudio": "valor"
                        }
                    ]
                },
                "hechos-docente-publicacion": {
                    "items": [
                        {
                            "docente": "11356034",
                            "publicacion": 4,
                            "numerocitaciones": 50
                        },
                        {
                            "docente": "1515515",
                            "publicacion": 4,
                            "numerocitaciones": 50
                        },
                        {
                            "docente": "545511",
                            "publicacion": 6,
                            "numerocitaciones": 75
                        },
                        {
                            "docente": "226555",
                            "publicacion": 7,
                            "numerocitaciones": 500
                        },
                        {
                            "docente": "123456788",
                            "publicacion": 8,
                            "numerocitaciones": 22
                        },
                        {
                            "docente": "545511",
                            "publicacion": 8,
                            "numerocitaciones": 22
                        },
                        {
                            "docente": "65",
                            "publicacion": 9,
                            "numerocitaciones": 43
                        },
                        {
                            "docente": "65",
                            "publicacion": 10,
                            "numerocitaciones": 873
                        }
                    ]
                },
                "hechos-docente-proyecto": {
                    "items": [
                        {
                            "docente": "valor",
                            "proyecto": "valor"
                        }
                    ]
                },
                "hechos-docente-titulo": {
                    "items": [
                        {
                            "docente": "11356034",
                            "titulo": 3,
                            "nivel": "Doctorado"
                        },
                        {
                            "docente": "1515515",
                            "titulo": 3,
                            "nivel": "Doctorado"
                        },
                        {
                            "docente": "545511",
                            "titulo": 4,
                            "nivel": "Maestria"
                        },
                        {
                            "docente": "226555",
                            "titulo": 5,
                            "nivel": "Pregrado"
                        },
                        {
                            "docente": "123456788",
                            "titulo": 6,
                            "nivel": "Maestria"
                        },
                        {
                            "docente": "545511",
                            "titulo": 6,
                            "nivel": "Maestria"
                        },
                        {
                            "docente": "65",
                            "titulo": 5,
                            "nivel": "Maestria"
                        }
                    ]
                },
                "hechos-docente-premio": {
                    "items": [
                        {
                            "docente": "valor",
                            "premio": "valor"
                        }
                    ]
                }
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
            '''
             # consultar docente
            resultTeacher = self.queryAll(dedent("""\
                SELECT cedula, primernombre, primerapellido, correo, areadeinvestigacion, 
                sexo, nacionalidad, segundonombre, segundoapellido, facultad, tipo, escalafon
                FROM docente WHERE fecha_actualizacion >= %s"""), [date_update])
            
            #consultar publicaciones
            resultPublication = self.queryAll(dedent("""\
            SELECT id As codigo, cedulaautor, titulopublicacion, urlcitacion, urlpublicacion, numerocitaciones
            FROM public.publicacion WHERE fecha_actualizacion >=  %s"""), [date_update])

            resultOtherStudio = self.queryAll(dedent("""\
            SELECT id As codigo, cedulaautor, nomtitulo
            FROM public.otro_estudio WHERE fecha_actualizacion >=  %s"""), [date_update])

            resultPrize = self.queryAll(dedent("""\
            SELECT id As codigo, nombre, cedulaautor
            FROM public.premio WHERE fecha_actualizacion >=  %s"""), [date_update])

            resultProject = self.queryAll(dedent("""\
            SELECT id As codigo, cedulaautor, titulo
            FROM public.proyecto WHERE fecha_actualizacion >=  %s"""), [date_update])

            resultTitle = self.queryAll(dedent("""\
            SELECT id As codigo, cedulaautor, nomtitulo, nivel
            FROM public.titulo WHERE fecha_actualizacion >=  %s"""), [date_update])

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
            '''
            response = response = {
                "dim-docente": {
                    "items": [
                        {
                            "cedula": "11356034",
                            "primernombre": "Mirella",
                            "segundonombre": "Segundo",
                            "primerapellido": "Herrera",
                            "segundoapellido": "Segundo",
                            "correo": "mirella.herrera@gmail.com",
                            "areadeinvestigacion": "investigacion",
                            "sexo": "F",
                            "nacionalidad": "V",
                            "facultad": "FACYT",
                            "tipo": "Investigador",
                            "escalafon": "Titular"
                        },
                        {
                            "cedula": "1515515",
                            "primernombre": "Dessiree",
                            "primerapellido": "Delgado",
                            "correo": "desidelgado@gmail.com",
                            "areadeinvestigacion": "investigacion",
                            "sexo": "F",
                            "nacionalidad": "V",
                            "segundonombre": "SegundoNombre",
                            "segundoapellido": "Segundoapellido",
                            "facultad": "FACYT",
                            "tipo": "Investigador",
                            "escalafon": "Titular"
                        },
                        {
                            "cedula": "545511",
                            "primernombre": "Marilyn",
                            "primerapellido": "Guigni",
                            "correo": "marilyngiugni@gmail.com",
                            "areadeinvestigacion": "investigacion",
                            "sexo": "F",
                            "nacionalidad": "V",
                            "segundonombre": "SegundoNombre",
                            "segundoapellido": "Segundoapellido",
                            "facultad": "FACYT",
                            "tipo": "Investigador",
                            "escalafon": "Asociado"
                        },
                        {
                            "cedula": "226555",
                            "primernombre": "Pedro",
                            "primerapellido": "Linares",
                            "correo": "pedro@gmail.com",
                            "areadeinvestigacion": "investigacion",
                            "sexo": "M",
                            "nacionalidad": "E",
                            "segundonombre": "SegundoNombre",
                            "segundoapellido": "Segundoapellido",
                            "facultad": "Ingeniería",
                            "tipo": "Contratado",
                            "escalafon": "Asociado"
                        },
                        {
                            "cedula": "123456788",
                            "primernombre": "Alguien ahi",
                            "primerapellido": "Alguien ahi",
                            "correo": "alguienahi@gmail.com",
                            "areadeinvestigacion": "investigacion",
                            "sexo": "f",
                            "nacionalidad": "e",
                            "segundonombre": "SegundoNombre",
                            "segundoapellido": "Segundoapellido",
                            "facultad": "ODONTOLOGIA",
                            "tipo": "Normal",
                            "escalafon": "Asistente"
                        },
                        {
                            "cedula": "65",
                            "primernombre": "Afddgd",
                            "primerapellido": "Adfgdi",
                            "correo": "alguienahi@gmail.com",
                            "areadeinvestigacion": "derecho penal",
                            "sexo": "f",
                            "nacionalidad": "e",
                            "segundonombre": "SegundoNombre",
                            "segundoapellido": "Segundoapellido",
                            "facultad": "FCJP",
                            "tipo": "Normal",
                            "escalafon": "Titular"
                        }
                    ]
                },
                "dim-otro-estudio": {
                    "items": [
                        {
                            "codigo": "valor",
                            "nomtitulo": "valor"
                        }
                    ]
                },
                "dim-publicacion": {
                    "items": [
                        {
                            "codigo": 4,
                            "titulopublicacion": "Titulo de la publicacion2",
                            "urlcitacion": "http://dhcvhzvgvgvgvz.com",
                            "urlpublicacion": "http://aquiseencuentra.com",
                            "numerocitaciones": 50
                        },
                        {
                            "codigo": 6,
                            "titulopublicacion": "Titulo de la publicacion2",
                            "urlcitacion": "http://dhcvhzvgvgvgvz.com",
                            "urlpublicacion": "http://aquiseencuentra.com",
                            "numerocitaciones": 75
                        },
                        {
                            "codigo": 7,
                            "titulopublicacion": "Titulo de la publicacion3",
                            "urlcitacion": "http://dhcvhzvgvgvgvz.com",
                            "urlpublicacion": "http://aquiseencuentra.com",
                            "numerocitaciones": 500
                        },
                        {
                            "codigo": 8,
                            "titulopublicacion": "Titulo de la publicacion4",
                            "urlcitacion": "http://dhcvhzvgvgvgvz.com",
                            "urlpublicacion": "http://aquiseencuentra.com",
                            "numerocitaciones": 22
                        },
                        {
                            "codigo": 9,
                            "titulopublicacion": "Titulo de la publicacion5",
                            "urlcitacion": "http://dhcvhzvgvgvgvz.com",
                            "urlpublicacion": "http://aquiseencuentra.com",
                            "numerocitaciones": 43
                        },
                        {
                            "codigo": 10,
                            "titulopublicacion": "Titulo de la publicacion6",
                            "urlcitacion": "http://dhcvhzvgvgvgvz.com",
                            "urlpublicacion": "http://aquiseencuentra.com",
                            "numerocitaciones": 873
                        }
                    ]
                },
                "dim-proyecto": {
                    "items": [
                        {
                            "codigo": "valor",
                            "titulo": "valor"
                        }
                    ]
                },
                "dim-titulo": {
                    "items": [
                        {
                            "codigo": 3,
                            "nomtitulo": "Licenciado en Computacion"
                        },
                        {
                            "codigo": 4,
                            "nomtitulo": "Ingeniera"
                        },
                        {
                            "codigo": 5,
                            "nomtitulo": "Licenciado en Computacion"
                        },
                        {
                            "codigo": 6,
                            "nomtitulo": "Ingeniera"
                        }
                    ]
                },
                "dim-premio": {
                    "items": [
                        {
                            "codigo": "valor",
                            "nombre": "valor"
                        }
                    ]
                },
                "hechos-docente-otroestudio": {
                    "items": [
                        {
                            "docente": "valor",
                            "otroestudio": "valor"
                        }
                    ]
                },
                "hechos-docente-publicacion": {
                    "items": [
                        {
                            "docente": "11356034",
                            "publicacion": 4,
                            "numerocitaciones": 50
                        },
                        {
                            "docente": "1515515",
                            "publicacion": 4,
                            "numerocitaciones": 50
                        },
                        {
                            "docente": "545511",
                            "publicacion": 6,
                            "numerocitaciones": 75
                        },
                        {
                            "docente": "226555",
                            "publicacion": 7,
                            "numerocitaciones": 500
                        },
                        {
                            "docente": "123456788",
                            "publicacion": 8,
                            "numerocitaciones": 22
                        },
                        {
                            "docente": "545511",
                            "publicacion": 8,
                            "numerocitaciones": 22
                        },
                        {
                            "docente": "65",
                            "publicacion": 9,
                            "numerocitaciones": 43
                        },
                        {
                            "docente": "65",
                            "publicacion": 10,
                            "numerocitaciones": 873
                        }
                    ]
                },
                "hechos-docente-proyecto": {
                    "items": [
                        {
                            "docente": "valor",
                            "proyecto": "valor"
                        }
                    ]
                },
                "hechos-docente-titulo": {
                    "items": [
                        {
                            "docente": "11356034",
                            "titulo": 3,
                            "nivel": "Doctorado"
                        },
                        {
                            "docente": "1515515",
                            "titulo": 3,
                            "nivel": "Doctorado"
                        },
                        {
                            "docente": "545511",
                            "titulo": 4,
                            "nivel": "Maestria"
                        },
                        {
                            "docente": "226555",
                            "titulo": 5,
                            "nivel": "Pregrado"
                        },
                        {
                            "docente": "123456788",
                            "titulo": 6,
                            "nivel": "Maestria"
                        },
                        {
                            "docente": "545511",
                            "titulo": 6,
                            "nivel": "Maestria"
                        },
                        {
                            "docente": "65",
                            "titulo": 6,
                            "nivel": "Maestria"
                        }
                    ]
                },
                "hechos-docente-premio": {
                    "items": [
                        {
                            "docente": "valor",
                            "premio": "valor"
                        }
                    ]
                }
            }

        except DatabaseError as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))
        except Exception as e:
            abort(500, message="{0}:{1}".format(e.__class__.__name__, e.__str__()))

        return jsonify(response), 200, { 'Access-Control-Allow-Origin': '*' }