-- Aula 1 gustavo modelo físico teste

-- 1 Criar o banco de dados
create schema if not exists Ex_SQL1;

-- 2 abrir a base de dados
use Ex_SQL1;

-- 3 criar tabelas
create table if not exists medico  (
id_medico int (11) primary key,
crm int not null,
nome varchar(100) not null,
cpf varchar(20) not null,
especialidade varchar(50) not null,
data_nascimento date not null,
endereco varchar(200) not null,
telefone varchar(20)
);

create table if not exists tipo_exame (
id_tipo_exame int(11) primary key,
tipo varchar(50) not null
);

create table if not exists resultado_exame (
id_tipo_resultado_exame int (11) primary key,
tipo varchar(30) not null
);

create table if not exists riscos_ocupacionais (
id_riscos int(11) primary key,
nome varchar(45) not null
);

create table if not exists cargo (
id_cargo int(11) primary key,
nome varchar(45)
);

create table if not exists funcionario (
id_funcionario int(11) primary key,
nome varchar(100) not null,
cpf varchar(20) not null,
data_nascimento date not null,
endereco varchar(200) not null,
telefone varchar(20) not null,

);
