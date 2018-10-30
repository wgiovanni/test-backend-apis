/*CREATE DATABASE estudiante;

\c estudiante
*/

CREATE TABLE IF NOT EXISTS facultad(
  Id Serial,
  Nombre nchar(100) NOT NULL,	
	
  PRIMARY KEY (Id)
);

CREATE TABLE IF NOT EXISTS estatusEstudiante(
  Id Serial,
  Estatus bit NOT NULL,
  CedulaEstudiante int NOT NULL,	
	
  PRIMARY KEY (Id)
);

CREATE TABLE IF NOT EXISTS estudiante(
  Cedula int,
  PrimerNombre nchar(100) NOT NULL,
  SegundoNombre nchar(100) DEFAULT NULL,
  PrimerApellido nchar(100) NOT NULL,
  SegundoApellido nchar(100) DEFAULT NULL,
  Sexo int NOT NULL,
  Discapacidad nchar(100) NOT NULL,
  Direccion nchar(200) DEFAULT NULL,
  Telefono1 nchar(15) NOT NULL,
  Telefono2 nchar(15) DEFAULT NULL,
  Etnia nchar(100) NOT NULL,
  Email nchar(50) NOT NULL,
  EdoProcedencia nchar(50) NOT NULL,
  FechaNacimiento date NOT NULL,
  IdEstatusEstudiante int NOT NULL,
  IdFacultad int NOT NULL,
   
  PRIMARY KEY (Cedula),
  FOREIGN KEY (IdEstatusEstudiante) REFERENCES estatusestudiante(Id) ON UPDATE CASCADE,	
  FOREIGN KEY (IdFacultad) REFERENCES facultad(Id) ON UPDATE CASCADE	

);

ALTER TABLE estatusEstudiante
ADD FOREIGN KEY (CedulaEstudiante) REFERENCES estudiante(Cedula) ON UPDATE CASCADE;


CREATE TABLE IF NOT EXISTS carrera(
  Id Serial,
  Nombre nchar(100) NOT NULL,	
  Tipo bit NOT NULL,
  IdFacultad int NOT NULL,

  PRIMARY KEY (Id),
  FOREIGN KEY (IdFacultad) REFERENCES facultad(Id) ON UPDATE CASCADE	
);

CREATE TABLE IF NOT EXISTS estudioadicional(
  Id Serial,
  Diplomado nchar(100) DEFAULT NULL,
  Curso nchar(100) DEFAULT NULL,
  Taller nchar(100) DEFAULT NULL,
  CedulaEstudiante int NOT NULL,	
	
  PRIMARY KEY (Id),
  FOREIGN KEY (CedulaEstudiante) REFERENCES estudiante(Cedula) ON UPDATE CASCADE	
);

CREATE TABLE IF NOT EXISTS asignaturainscrita(
  Id Serial,
  Nombre nchar(100) NOT NULL,	
  IdEstatusEstudiante int NOT NULL,

  PRIMARY KEY (Id),
  FOREIGN KEY (IdEstatusEstudiante) REFERENCES estatusestudiante(Id) ON UPDATE CASCADE	
);


CREATE TABLE IF NOT EXISTS asignaturaaprobada(
  Id Serial,
  Nombre nchar(100) NOT NULL,
  Calificacion int NOT NULL,
  Periodo 	nchar(20) NOT NULL,
  IdEstatusEstudiante int NOT NULL,

  PRIMARY KEY (Id),
  FOREIGN KEY (IdEstatusEstudiante) REFERENCES estatusestudiante(Id) ON UPDATE CASCADE	
);

/*
insert into admint(admint,password,email,imagen) values('hola','0000','juanhernandezluis0@gmail.com','../image/User_icon_BLACK-01.PNG');
*/

-- 1 es activo
-- 2 es desactivo

INSERT INTO public.estatusestudiante(
            status)
    VALUES (1);


INSERT INTO public.estatusestudiante(
            status)
    VALUES (2);