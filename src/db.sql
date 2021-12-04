create table trainer (
    id serial not null primary key,
    nombre varchar(50) not null,
    password varchar(50) not null,
    username varchar(50) not null,
    id_team int,
    fecha_nac date,
    edad int,
    partidasTotales int,
    partidasGanadas int, 
    partidasPerdidas int,

);

insert into trainer (nombre,password,username,id_team,fecha_nac,edad,partidasTotales,partidasGanadas,partidasPerdidas) values ('felipe','root1','user1',1,'12-02-1998',23,0,0,0);
insert into trainer (nombre,password,username,id_team,fecha_nac,edad,partidasTotales,partidasGanadas,partidasPerdidas) values ('marcos','root2','user2',2,'12-02-1998',23,0,0,0);
insert into trainer (nombre,password,username,id_team,fecha_nac,edad,partidasTotales,partidasGanadas,partidasPerdidas) values  ('rogelio','root3','user3',3,'12-02-1998',23,0,0,0);
insert into trainer (nombre,password,username,id_team,fecha_nac,edad,partidasTotales,partidasGanadas,partidasPerdidas)  values ('mario','root4','user4',4,'12-02-1998',23,0,0,0);
insert into trainer (nombre,password,username,id_team,fecha_nac,edad,partidasTotales,partidasGanadas,partidasPerdidas) values ('nathan','root5','user5',5,'12-02-1998',23,0,0,0);
insert into trainer (nombre,password,username,id_team,fecha_nac,edad,partidasTotales,partidasGanadas,partidasPerdidas) values ('ilonka','roo','user6',6,'12-02-1998',23,0,0,0);
insert into trainer (nombre,password,username,id_team,fecha_nac,edad,partidasTotales,partidasGanadas,partidasPerdidas) values ('winter','root7','user7',7,'12-02-1998',23,0,0,0);
insert into trainer (nombre,password,username,id_team,fecha_nac,edad,partidasTotales,partidasGanadas,partidasPerdidas) values ('temary','root8','user8',8,'12-02-1998',23,0,0,0);


CREATE TABLE tipos(
    id  int not null primary key not null,
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
insert into tipos (id,nombre,fortaleza,debilidad) values (9,'normal','veneno','fuego');
insert into tipos (id,nombre,fortaleza,debilidad) values (10,'veneno','volador','agua');
insert into tipos (id,nombre,fortaleza,debilidad) values (11,'bicho','fuego','volador');
insert into tipos (id,nombre,fortaleza,debilidad) values (12,'hada','fantasma','psiquico');

CREATE TABLE ataque(
    id serial not null primary key,
    nombre text,
    tipo_at varchar(50) not null,
    daño_base  int not null not null
);
--insert elements into ataque
insert into ataque (nombre,tipo_at,daño_base) values ('controla','psiquico',50);
insert into ataque (nombre,tipo_at,daño_base) values ('directo','lucha',40);
insert into ataque (nombre,tipo_at,daño_base) values ('carazo','acero',60);
insert into ataque (nombre,tipo_at,daño_base) values ('impaktrueno','electrico',25);
insert into ataque (nombre,tipo_at,daño_base) values ('tormenta','tierra',89);
insert into ataque (nombre,tipo_at,daño_base) values ('buuu','fantasma',70);
insert into ataque (nombre,tipo_at,daño_base) values ('fireball','fuego',40);
insert into ataque (nombre,tipo_at,daño_base) values ('Splash','agua',45);
insert into ataque (nombre,tipo_at,daño_base) values ('Infect','veneno',87);
insert into ataque (nombre,tipo_at,daño_base) values ('siuuuu','bicho',32);
insert into ataque (nombre,tipo_at,daño_base) values ('adacadabra','hada',65);
CREATE TABLE especie(
    id  int not null not null primary key,
    nombre varchar(50) not null,
    id_tipo  int ,
    id_tipo2  int ,
    FOREIGN key (id_tipo) references tipos(id),
    foreign key (id_tipo2) references tipos(id)
);
--insert elements into especie tables 
insert into especie (id,nombre,id_tipo) values (1,'pikachu',5);
insert into especie (id,nombre,id_tipo,id_tipo) values (2,'charmander',7,6);
insert into especie (id,nombre,id_tipo,id_tipo2) values (3,'Bulbasaur',4,3);
insert into especie (id,nombre,id_tipo) values (4,'Wartortle',7);
insert into especie (id,nombre,id_tipo) values (5,'Venusaur',2);
insert into especie (id,nombre,id_tipo) values (6,'Ivysaur',1);
insert into especie (id,nombre,id_tipo) values (7,'Venusaur',2);
insert into especie (id,nombre,id_tipo) values (8,'Charmeleon',3);
insert into especie (id,nombre,id_tipo) values (9,'Charizard',4);
insert into especie (id,nombre,id_tipo) values (10,'Squirtle',5);
insert into especie (id,nombre,id_tipo) values (11,'Wartortle',6);
insert into especie (id,nombre,id_tipo) values (12,'Blastoise',7);
insert into especie (id,nombre,id_tipo) values (13,'Caterpie',8);
insert into especie (id,nombre,id_tipo) values (14,'Metapod',9);
insert into especie (id,nombre,id_tipo) values (15,'Butterfree',10);
insert into especie (id,nombre,id_tipo) values (15,'Weedle',11);
insert into especie (id,nombre,id_tipo) values (16,'Kakuna',12);
insert into especie (id,nombre,id_tipo) values (17,'Beedrill',1);
insert into especie (id,nombre,id_tipo) values (18,'Pidgey',2);
insert into especie (id,nombre,id_tipo) values (19,'Pidgeotto',3);
insert into especie (id,nombre,id_tipo) values (20,'Pidgeot',4);
insert into especie (id,nombre,id_tipo) values (21,'Rattata',5);
insert into especie (id,nombre,id_tipo) values (22,'Raticate',6);
insert into especie (id,nombre,id_tipo) values (23,'Spearow',7);
insert into especie (id,nombre,id_tipo) values (24,'Fearow',8);
insert into especie (id,nombre,id_tipo) values (25,'Ekans',9);
insert into especie (id,nombre,id_tipo) values (26,'Arbok',10);
insert into especie (id,nombre,id_tipo) values (27,'Sandslash',11);
insert into especie (id,nombre,id_tipo) values (28,'Nidorina',12);
insert into especie (id,nombre,id_tipo) values (29,'Nidoqueen',1);
insert into especie (id,nombre,id_tipo) values (30,'Nidoking',2);
insert into especie (id,nombre,id_tipo) values (31,'Clefairy',3);
insert into especie (id,nombre,id_tipo) values (32,'Clefable',4);
insert into especie (id,nombre,id_tipo) values (33,'Ninetales',6);
insert into especie (id,nombre,id_tipo) values (34,'Jigglypuff',7);
insert into especie (id,nombre,id_tipo) values (35,'Wigglytuff',8);
insert into especie (id,nombre,id_tipo) values (36,'Zubat',9);
insert into especie (id,nombre,id_tipo) values (37,'Golbat',10);
insert into especie (id,nombre,id_tipo) values (38,'Oddish',11);
insert into especie (id,nombre,id_tipo) values (39,'Gloom',12);
insert into especie (id,nombre,id_tipo) values (40,'Vileplume',1);
insert into especie (id,nombre,id_tipo) values (41,'Paras',2);
insert into especie (id,nombre,id_tipo) values (42,'Parasect',3);
insert into especie (id,nombre,id_tipo) values (43,'Venonat',4);
insert into especie (id,nombre,id_tipo) values (44,'Venomoth',5);
insert into especie (id,nombre,id_tipo) values (45,'Diglett',6);
insert into especie (id,nombre,id_tipo) values (46,'Dugtrio',7);
insert into especie (id,nombre,id_tipo) values (47,'Meowth',8);
insert into especie (id,nombre,id_tipo) values (48,'Persian',9);
insert into especie (id,nombre,id_tipo) values (49,'Psyduck',10);
insert into especie (id,nombre,id_tipo) values (50,'Golduck',11);
insert into especie (id,nombre,id_tipo) values (51,'Mankey',12);
insert into especie (id,nombre,id_tipo) values (52,'Primeape',1);
insert into especie (id,nombre,id_tipo) values (53,'Growlithe',2);



create table monster (
    id serial not null primary key,
    nombre varchar(50),
    velocidad int ,
    salud int,
    id_trainer int,
    id_team int,
    id_especie int,
    id_ataque int,
    foreign key (id_trainer) references trainer(id),
    foreign key (id_especie) references especie(id),
    foreign key (id_ataque) references ataque(id)

);