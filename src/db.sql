--mr arreglado : https://app.diagrams.net/#G13mmksXYQGwj2blyQzbI6Tl3__95Qi5JU
--Drop:
--equipo,mundo,select atack
--referencias de entrenador a monstruo por query (nos dimos cuenta que la tabla equipo solo relacionaba las 2 y enredaba la implementacion)
--lo mismo pasaba con select atack
--tabla mundo no tenia razon de existir
--modificacion de las cardinalidades en especies y tipos y de entrenador a monstruos con relacion a las querys buscar el ...
--monstruos correspondiente a un equipo de un usuario es solamente ver que monstruo tiene su id 
--cambio de foreign key de estadisticas entendimiento erroneo ya que estaba referenciada en entrenador pero mientras no 
--juegue no tiene estadisticas 

CREATE DATABASE taller3;
--\c taller3 user postgres

--create table entrenador 
CREATE TABLE entrenador (
    id serial primary key not null,
    nombre varchar(50) ,
    password varchar(50) , 
    nombre_usuario varchar(50),
    fecha_nac date,
    edad int
);
--insert elements in to entrenador table 
INSERT INTO entrenador (nombre,password,nombre_usuario,fecha_nac,edad) VALUES ('felipe','root','user1','12-02-1998',23);

INSERT INTO entrenador (nombre,password,nombre_usuario,fecha_nac,edad) VALUES ('Mario','root1','user2','12-03-1998',23);

INSERT INTO entrenador (nombre,password,nombre_usuario,fecha_nac,edad) VALUES ('martin','root2','user3','12-04-1998',23);

--create table ataque
CREATE TABLE ataque(
    id serial not null primary key,
    tipo_at varchar(50) not null,
    daño_base int not null
);
--insert elements into ataque
insert into ataque (tipo_at,daño_base) values ('psiquico',50);
insert into ataque (tipo_at,daño_base) values ('lucha',40);
insert into ataque (tipo_at,daño_base) values ('acero',60);
insert into ataque (tipo_at,daño_base) values ('electrico',25);
insert into ataque (tipo_at,daño_base) values ('tierra',89);
insert into ataque (tipo_at,daño_base) values ('fantasma',70);

CREATE TABLE tipos(
    id int primary key not null,
    nombre varchar(50) not null,
    fortaleza varchar(50) ,
    debilidad varchar(50)
);
--insert elements into Tipos tables
insert into tipos (id,nombre,fortaleza,debilidad) values (1,'psiquico','lucha','lucha');
insert into tipos (id,nombre,fortaleza,debilidad) values (2,'lucha','fantasma','psiquico');
insert into tipos (id,nombre,fortaleza,debilidad) values (3,'acero','electrico','fantasma');
insert into tipos (id,nombre,fortaleza,debilidad) values (4,'tierra','lucha','psiquico');
insert into tipos (id,nombre,fortaleza,debilidad) values (5,'electrico','lucha','tierra');
insert into tipos (id,nombre,fortaleza,debilidad) values (6,'fantasma','acero','lucha');
insert into tipos (id,nombre,fortaleza,debilidad) values (7,'fuego','tierra','agua');
insert into tipos (id,nombre,fortaleza,debilidad) values (8,'agua','acero','fuego');


--crear tabla de especies 
CREATE TABLE especie(
    id int not null primary key,
    nombre varchar(50) not null,
    id_tipo int ,
    id_tipo2 int,
    FOREIGN key (id_tipo) references tipos(id),
    foreign key (id_tipo2) references tipos(id)
);
--insert elements into especie tables 
insert into especie (id,nombre,id_tipo) values (1,'pikachu',5);
insert into especie (id,nombre,id_tipo,id_tipo2) values (2,'charmander',7,6);
insert into especie (id,nombre,id_tipo,id_tipo2) values (3,'Bulbasaur',4,3);
insert into especie (id,nombre,id_tipo) values (4,'Wartortle',6);
insert into especie (id,nombre,id_tipo) values (5,'Venusaur',2);
insert into especie (id,nombre,id_tipo,id_tipo2) values (6,'Raichu',5,6);

--create table selec_atack
CREATE TABLE monstruos(
    id int not null primary key,
    nombre varchar(50) not null,
    velocidad int not null,
    salud int not null,
    id_user int not null,
    id_ataque int not null,
    id_especie int not null,
    foreign key (id_user) references entrenador(id),
    foreign key (id_ataque) references ataque(id),
    foreign key (id_especie) references especie(id)
);
--los monstruos solo se crean cuando se captura una especie 

CREATE TABLE estadisticas (
    id int primary key not null,
    nombre_combate varchar(50),
    ganado boolean,
    perdido boolean,
    id_user int ,
    foreign key (id_user) references entrenador(id)
);
--TO_DO:insert elements in the stadistics
