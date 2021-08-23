create database coaching;
use coaching;

create table course(
    ID int primary key AUTO_INCREMENT,
    name varchar(20),
    duration varchar(20)
);


insert into course values('AIML', '11 Months'), ('PGP', '1 year'), ('BE', '4 years');