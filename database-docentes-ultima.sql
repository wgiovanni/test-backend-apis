CREATE DATABASE docente;

\c docente

/*Creacion de etidades*/
CREATE TABLE Docente(
	Cedula int ,
	PirmerNombre varchar(50) ,
	SegundoNombre varchar(50) ,
	PirmerApellido varchar(50) ,
	SegundoApellido varchar(50) ,
	Sexo varchar(2),
	correo varchar(50) ,
	Nacionalidad varchar(2),
	Facultad varchar(30) ,
	Tipo varchar(50) ,
	AreaDeInvestigacion varchar(50) ,
	Escalafon varchar(50) ,
		PRIMARY KEY (Cedula));

CREATE TABLE Publicacion(
	Id  serial,
	CedulaAutor int ,
	NumeroCitaciones int ,
	UrlCitacion varchar(200) ,
	TituloPublicacion varchar(200),
	UrlPublicacion varchar(200),
		PRIMARY KEY (Id,CedulaAutor),
		FOREIGN KEY (CedulaAutor) REFERENCES Docente(Cedula) ON UPDATE CASCADE	);

CREATE TABLE Titulo(
	Id serial,
	CedulaAutor int ,
	Nomtitulo varchar(50) ,
	Nivel varchar(50) ,
		PRIMARY KEY (Id),
		FOREIGN KEY (CedulaAutor) REFERENCES Docente(Cedula) ON UPDATE CASCADE	);

CREATE TABLE OtroEstudio(
	Id serial,
	CedulaAutor int ,
	Nomtitulo varchar(50) ,
		PRIMARY KEY (Id,CedulaAutor),
		FOREIGN KEY (CedulaAutor) REFERENCES Docente(Cedula) ON UPDATE CASCADE	);

CREATE TABLE Proyecto(
	Id  serial,
	CedulaAutor int ,
	titulo  varchar(50) ,
		PRIMARY KEY (Id,CedulaAutor),
		FOREIGN KEY (CedulaAutor) REFERENCES Docente(Cedula) ON UPDATE CASCADE	);

CREATE TABLE Premio(
	Id  serial,
	CedulaAutor int ,
	Nombre varchar(50) ,
		PRIMARY KEY (Id,CedulaAutor),
		FOREIGN KEY (CedulaAutor) REFERENCES Docente(Cedula) ON UPDATE CASCADE	);	

			
/*Creacion de Relaciones
CREATE TABLE DocenteTieneTitulo(
	CedulaPersona int,
	IdTitulo int,
	PRIMARY KEY (CedulaPersona,IdTitulo),
	FOREIGN KEY (IdTitulo) REFERENCES titulo(id)  on update cascade,
	FOREIGN KEY (CedulaPersona)  REFERENCES docente(cedula)  on update cascade);

CREATE TABLE DocenteRealizaOtroEstudio(
	CedulaPersona int,
	IdOtroEstudio int,
	FOREIGN KEY (CedulaPersona) REFERENCES Docente(Cedula) ON UPDATE CASCADE,
	FOREIGN KEY (IdOtroEstudio) REFERENCES OtroEstudio(Id) ON UPDATE CASCADE);

CREATE TABLE DocenteTieneCitacion(
	CedulaPersona int,
	IdCitacion int,
	FOREIGN KEY (IdCitacion) REFERENCES Citacion(Id) ON UPDATE CASCADE,
	FOREIGN KEY (CedulaPersona) REFERENCES Docente(Cedula) ON UPDATE CASCADE);

CREATE TABLE DocenteParticipaProyecto(
	CedulaPersona int,
	IdProyecto int,
	FOREIGN KEY (IdProyecto) REFERENCES Proyecto(Id) ON UPDATE CASCADE,
	FOREIGN KEY (CedulaPersona) REFERENCES Docente(Cedula) ON UPDATE CASCADE);
*/