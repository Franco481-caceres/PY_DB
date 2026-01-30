drop database if exists seguros;
create database seguros;
use seguros;


create table direcciones (
	direccion_id integer auto_increment,
    calle varchar(50),
	cp varchar(10),
	municipio varchar(50),
    primary key (direccion_id)
);


create TABLE clientes (
	cliente_id integer auto_increment,
	nombre varchar(20),
	apellido varchar(20),
	fecha_nacimiento date,
	nro_licencia integer,
	direccion_id integer,
    PRIMARY KEY(cliente_id),
    Foreign Key (direccion_id) REFERENCES direcciones (direccion_id)
);



create table autos (
	patente varchar(7) unique,
    chasis_id integer unique,
	motor_id integer UNIQUE,
	marca varchar(15),
	modelo VARCHAR(30),
	tipo VARCHAR(10),
	color varchar(10),
	cliente_id integer,
    primary KEY (patente),
    Foreign Key (cliente_id) REFERENCES clientes (cliente_id)
    );

create table productores( 
	matricula integer unique,
	nombre varchar(20),
	telefono varchar(11),
	direccion_id integer,
    primary key(matricula),
    Foreign Key (direccion_id) REFERENCES direcciones (direccion_id)
);

create table polizas (
	poliza_id integer auto_increment,
	prima decimal (6,2),
	premio decimal(7,2),
	suma_asegurada decimal(9,2),
	periodo_inicial date,
	periodo_final date,
	matricula integer,
    cobertura decimal,
	patente varchar(7),
    PRIMARY KEY (poliza_id),
    Foreign Key (patente) REFERENCES autos (patente),
    Foreign Key (matricula) REFERENCES productores (matricula)
);

create table siniestros (
	siniestro_id integer auto_increment,
	detalles varchar(150)
    PRIMARY KEY(siniestros_id)
);

create table planes (
	plan_id integer auto_increment,
	poliza_id integer,
	siniestro_id integer,
    PRIMARY KEY(plan_id),
    Foreign Key (poliza_id) REFERENCES polizas (poliza_id),    
    Foreign Key (siniestro_id) REFERENCES siniestros (siniestro_id)
);

create table accidentes (
	accidente_id integer auto_increment,
    patente varchar(7),
	siniestro_id integer,
    fecha date,
	direccion_id integer,
    PRIMARY KEY(accidente_id),
    Foreign Key (direccion_id) REFERENCES direcciones(direccion_id)
);
 


