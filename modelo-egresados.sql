BEGIN;
--
-- Create model certificacion
--
CREATE TABLE "EGUC_certificacion" (
	"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
	"nombreCertificacion" varchar(100) NOT NULL, 
	"descripcion" varchar(500) NOT NULL, 
	"urlCertificacion" varchar(300) NOT NULL);
--
-- Create model cursos
--
CREATE TABLE "EGUC_cursos" (
	"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
	"nombre" varchar(100) NOT NULL, 
	"url" varchar(300) NOT NULL);
--
-- Create model educacion
--
CREATE TABLE "EGUC_educacion" (
	"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
	"instituto" varchar(100) NOT NULL, 
	"campoEstudio" varchar(100) NOT NULL, 
	"tituloObtenido" varchar(100) NOT NULL, 
	"urlCertificacion" varchar(300) NOT NULL);
--
-- Create model egresado
--
CREATE TABLE "EGUC_egresado" (
	"idUser" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
	"nombreUsuario" varchar(30) NOT NULL UNIQUE, 
	"primerNombre" varchar(50) NOT NULL, 
	"segundoNombre" varchar(50) NOT NULL, 
	"primerApellido" varchar(50) NOT NULL, 
	"segundoApellido" varchar(50) NOT NULL, 
	"descripcion" varchar(500) NOT NULL, 
	"intereses" varchar(500) NOT NULL, 
	"foto" varchar(2000) NOT NULL, 
	"email" varchar(100) NOT NULL, 
	"telefono" varchar(20) NOT NULL, 
	"identificacion" varchar(30) NOT NULL);
--
-- Create model estudiosUC
--
CREATE TABLE "EGUC_estudiosuc" (
	"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
	"facultad" varchar(100) NOT NULL, 
	"carrera" varchar(100) NOT NULL, 
	"anhoGrado" date NOT NULL, 
	"titulo" varchar(100) NOT NULL, 
	"urlCertificacion" varchar(300) NOT NULL, 
	"egresado_id" integer NOT NULL 
	REFERENCES "EGUC_egresado" ("idUser") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model idiomas
--
CREATE TABLE "EGUC_idiomas" (
	"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
	"idiomas" varchar(20) NOT NULL, 
	"egresado_id" integer NOT NULL 
	REFERENCES "EGUC_egresado" ("idUser") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model patentes
--
CREATE TABLE "EGUC_patentes" (
	"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
	"titulo" varchar(100) NOT NULL, 
	"descripcion" varchar(500) NOT NULL, 
	"numero" varchar(30) NOT NULL, 
	"inventores" varchar(150) NOT NULL, 
	"fecha" date NOT NULL, 
	"url" varchar(300) NOT NULL, 
	"egresado_id" integer NOT NULL 
	REFERENCES "EGUC_egresado" ("idUser") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model publicaciones
--
CREATE TABLE "EGUC_publicaciones" (
	"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
	"titulo" varchar(100) NOT NULL, 
	"nombre" varchar(100) NOT NULL, 
	"autores" varchar(150) NOT NULL, 
	"fecha" date NOT NULL, 
	"url" varchar(300) NOT NULL, 
	"descripcion" varchar(500) NOT NULL, 
	"egresado_id" integer NOT NULL 
	REFERENCES "EGUC_egresado" ("idUser") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model trabajos
--
CREATE TABLE "EGUC_trabajos" (
	"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
	"nombreEmpresa" varchar(100) NOT NULL, 
	"cargo" varchar(100) NOT NULL, 
	"descripcion" varchar(500) NOT NULL, 
	"egresado_id" integer NOT NULL 
	REFERENCES "EGUC_egresado" ("idUser") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model voluntariado
--
CREATE TABLE "EGUC_voluntariado" (
	"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
	"organizacion" varchar(100) NOT NULL, 
	"descripcion" varchar(500) NOT NULL, 
	"causa" varchar(300) NOT NULL, 
	"egresado_id" integer NOT NULL 
	REFERENCES "EGUC_egresado" ("idUser") DEFERRABLE INITIALLY DEFERRED);
--
-- Add field egresado to educacion
--
ALTER TABLE "EGUC_educacion" RENAME TO "EGUC_educacion__old";
CREATE TABLE "EGUC_educacion" (
	"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
	"instituto" varchar(100) NOT NULL, 
	"campoEstudio" varchar(100) NOT NULL, 
	"tituloObtenido" varchar(100) NOT NULL, 
	"urlCertificacion" varchar(300) NOT NULL, 
	"egresado_id" integer NOT NULL 
	REFERENCES "EGUC_egresado" ("idUser") DEFERRABLE INITIALLY DEFERRED);

INSERT INTO "EGUC_educacion" ("id", "instituto", "campoEstudio", "tituloObtenido", "urlCertificacion", "egresado_id") SELECT "id", "instituto", "campoEstudio", "tituloObtenido", "urlCertificacion", NULL FROM "EGUC_educacion__old";
DROP TABLE "EGUC_educacion__old";
CREATE INDEX "EGUC_estudiosuc_egresado_id_ce04c2d4" ON "EGUC_estudiosuc" ("egresado_id");
CREATE INDEX "EGUC_idiomas_egresado_id_fe5aa58c" ON "EGUC_idiomas" ("egresado_id");
CREATE INDEX "EGUC_patentes_egresado_id_bc6e8d84" ON "EGUC_patentes" ("egresado_id");
CREATE INDEX "EGUC_publicaciones_egresado_id_3cae5058" ON "EGUC_publicaciones" ("egresado_id");
CREATE INDEX "EGUC_trabajos_egresado_id_9b578b94" ON "EGUC_trabajos" ("egresado_id");
CREATE INDEX "EGUC_voluntariado_egresado_id_206e4e15" ON "EGUC_voluntariado" ("egresado_id");
CREATE INDEX "EGUC_educacion_egresado_id_69416c3a" ON "EGUC_educacion" ("egresado_id");
--
-- Add field egresado to cursos
--
ALTER TABLE "EGUC_cursos" RENAME TO "EGUC_cursos__old";
CREATE TABLE "EGUC_cursos" (
	"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
	"nombre" varchar(100) NOT NULL, 
	"url" varchar(300) NOT NULL, 
	"egresado_id" integer NOT NULL 
	REFERENCES "EGUC_egresado" ("idUser") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "EGUC_cursos" ("id", "nombre", "url", "egresado_id") SELECT "id", "nombre", "url", NULL FROM "EGUC_cursos__old";
DROP TABLE "EGUC_cursos__old";
CREATE INDEX "EGUC_cursos_egresado_id_34c49a03" ON "EGUC_cursos" ("egresado_id");
--
-- Add field egresado to certificacion
--
ALTER TABLE "EGUC_certificacion" RENAME TO "EGUC_certificacion__old";
CREATE TABLE "EGUC_certificacion" (
	"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
	"nombreCertificacion" varchar(100) NOT NULL, 
	"descripcion" varchar(500) NOT NULL, 
	"urlCertificacion" varchar(300) NOT NULL, 
	"egresado_id" integer NOT NULL 
	REFERENCES "EGUC_egresado" ("idUser") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "EGUC_certificacion" ("id", "nombreCertificacion", "descripcion", "urlCertificacion", "egresado_id") SELECT "id", "nombreCertificacion", "descripcion", "urlCertificacion", NULL FROM "EGUC_certificacion__old";
DROP TABLE "EGUC_certificacion__old";
CREATE INDEX "EGUC_certificacion_egresado_id_bd25d3ee" ON "EGUC_certificacion" ("egresado_id");
COMMIT;




INSERT INTO public.eguc_egresado(
            "nombreUsuario", "primerNombre", "segundoNombre", "primerApellido", 
            "segundoApellido", descripcion, intereses, foto, email, telefono, 
            identificacion)
    VALUES ('gjimenez', 'Genessis', 'De Jesus', 'Jimenez', 
            'Zea', 'descripcion', 'futbol', '....', 'gjimenez@gmail,com', '04127658802', 
            '2464987');


INSERT INTO public.eguc_egresado(
            "nombreUsuario", "primerNombre", "segundoNombre", "primerApellido", 
            "segundoApellido", descripcion, intereses, foto, email, telefono, 
            identificacion)
    VALUES ('lgomez', 'Luis', 'Augusto', 'Gomez', 
            'No se', 'descripcion', 'metal', '....', 'luisgomez@gmail,com', '04127658802', 
            '756438457');


INSERT INTO public.eguc_egresado(
            "nombreUsuario", "primerNombre", "segundoNombre", "primerApellido", 
            "segundoApellido", descripcion, intereses, foto, email, telefono, 
            identificacion)
    VALUES ('wmorillo', 'Winder', 'Jose', 'Morillo', 
            'No se', 'descripcion', 'programar', '....', 'wmorillo@gmail,com', '746574323', 
            '146498766');

INSERT INTO public.eguc_egresado(
            "nombreUsuario", "primerNombre", "segundoNombre", "primerApellido", 
            "segundoApellido", descripcion, intereses, foto, email, telefono, 
            identificacion)
    VALUES ('wgiovanni', 'Wilkel', 'Alejandro', 'Giovanni', 
            'Perozo', 'descripcion', 'programar', '....', 'wgiovanni@gmail,com', '746574323', 
            '22422883');



INSERT INTO public.eguc_estudiosuc(
            facultad, carrera, "anhoGrado", titulo, "urlCertificacion", 
            egresado_id)
    VALUES ('Ciencias y Tecnología', 'Computación', '2018-07-24', 'Licenciado en Computación', 'url...', 
            1);

INSERT INTO public.eguc_estudiosuc(
            facultad, carrera, "anhoGrado", titulo, "urlCertificacion", 
            egresado_id)
    VALUES ('Ciencias y Tecnología', 'Física', '2018-07-24', 'Licenciado en Física', 'url...', 
            2);

INSERT INTO public.eguc_estudiosuc(
            facultad, carrera, "anhoGrado", titulo, "urlCertificacion", 
            egresado_id)
    VALUES ('Ciencias y Tecnología', 'Computación', '2018-07-24', 'Licenciado en Computación', 'url...', 
            3);

INSERT INTO public.eguc_estudiosuc(
            facultad, carrera, "anhoGrado", titulo, "urlCertificacion", 
            egresado_id)
    VALUES ('Ciencias y Tecnología', 'Química', '2010-07-24', 'Licenciado en Química', 'url...', 
            3);




INSERT INTO public.eguc_certificacion(
            "nombreCertificacion", descripcion, "urlCertificacion", egresado_id)
    VALUES ('Certificacion1', 'descripcion', 'url xxx', 3);

INSERT INTO public.eguc_certificacion(
            "nombreCertificacion", descripcion, "urlCertificacion", egresado_id)
    VALUES ('Certificacion2', 'descripcion', 'url xxx', 4);

INSERT INTO public.eguc_certificacion(
            "nombreCertificacion", descripcion, "urlCertificacion", egresado_id)
    VALUES ('Certificacion3', 'descripcion', 'url certificacion', 4);



INSERT INTO public.eguc_cursos(
            nombre, url, egresado_id)
    VALUES ('Programación basica', 'http://platzi.com/programacionbasica', 4);
INSERT INTO public.eguc_cursos(
            nombre, url, egresado_id)
    VALUES ('Curso basico PHP', 'http://platzi.com/wgiovanni/phpbasico', 4);
INSERT INTO public.eguc_cursos(
            nombre, url, egresado_id)
    VALUES ('Curso Java', 'http://platzi.com/java', 4);

INSERT INTO public.eguc_cursos(
            nombre, url, egresado_id)
    VALUES ('Curso Angular', 'http://platzi.com/angular', 1);
INSERT INTO public.eguc_cursos(
            nombre, url, egresado_id)
    VALUES ('Curso basico PHP', 'http://platzi.com/lgomez/phpbasico', 2);


INSERT INTO public.eguc_educacion(
	    instituto, "campoEstudio", "tituloObtenido", "urlCertificacion", 
            egresado_id)
    VALUES ('Instituto1', 'Campo de Estudio1', 'Titulo1', 'http://urlcertificacion.com', 2);

INSERT INTO public.eguc_educacion(
	    instituto, "campoEstudio", "tituloObtenido", "urlCertificacion", 
            egresado_id)
    VALUES ('Instituto2', 'Campo de Estudio2', 'Titulo2', 'http://urlcertificacion.com', 2);

INSERT INTO public.eguc_educacion(
	    instituto, "campoEstudio", "tituloObtenido", "urlCertificacion", 
            egresado_id)
    VALUES ('Instituto3', 'Campo de Estudio3', 'Titulo3', 'http://urlcertificacion.com', 3);



INSERT INTO public.eguc_patentes(
            titulo, descripcion, numero, inventores, fecha, url, egresado_id)
    VALUES ('Patente1', 'Descripcion Patente1', '5151', 'inventor1, inventor2, inventor3', '2018-07-10', 'url', 4);
INSERT INTO public.eguc_patentes(
            titulo, descripcion, numero, inventores, fecha, url, egresado_id)
    VALUES ('Patente2', 'Descripcion Patente1', '987874', 'inventor1, inventor2, inventor3', '2018-07-10', 'url', 1);



INSERT INTO public.eguc_trabajos(
            "nombreEmpresa", cargo, descripcion, egresado_id)
    VALUES ('Intelix', 'Programador web', 'descripcion', 4);
INSERT INTO public.eguc_trabajos(
            "nombreEmpresa", cargo, descripcion, egresado_id)
    VALUES ('Promotora Tantalo', 'Programador web', 'descripcion', 4);

INSERT INTO public.eguc_trabajos(
            "nombreEmpresa", cargo, descripcion, egresado_id)
    VALUES ('Sofos', 'Programador web', 'descripcion', 2);



INSERT INTO public.eguc_voluntariado(
            organizacion, descripcion, causa, egresado_id)
    VALUES ('Organizacion1', 'descripcion', 'una causa ahi', 3);
INSERT INTO public.eguc_voluntariado(
            organizacion, descripcion, causa, egresado_id)
    VALUES ('Organizacion2', 'descripcion', 'una causa ahi2', 1);

INSERT INTO public.eguc_voluntariado(
            organizacion, descripcion, causa, egresado_id)
    VALUES ('Organizacion3', 'descripcion', 'una causa ahi2', 1);
