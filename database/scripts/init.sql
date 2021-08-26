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
    firstname varchar(50),
    lastname varchar(50),
    email varchar(50),
    isStudent boolean default true
);