create database coaching;
use coaching;

create table course(
    ID int primary key AUTO_INCREMENT,
    name varchar(20),
    duration varchar(20)
);

insert into course(name, duration)
values
('AIML', '11 Months'),
('PGP', '1 year'),
('BE', '4 years');

create table users(
	ID int auto_increment primary key,
    firstname varchar(50) not null,
    lastname varchar(50) not null,
    password varchar(100) not null,
    email varchar(50) not null,
    isStudent boolean default true
);