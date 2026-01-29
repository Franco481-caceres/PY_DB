drop database if exists seguros;
create database seguros;
use seguros;

create table polizas(
poliza_id int auto_increment,
cliente_id int,
)