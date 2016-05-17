drop database if exists blogger;
create database blogger;
use blogger;
drop table if exists blogs;
create table blogs (
  id int not null AUTO_INCREMENT primary key,
  title text not null,
  text text not null,
  publisher_name varchar(100) not null,
  created_date datetime not null,
  updated_date datetime not null
);