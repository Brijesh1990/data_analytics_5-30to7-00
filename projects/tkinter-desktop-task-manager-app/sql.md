CREATE TABLE `tkinterapp_taskapp`.`tasks`
(

id int primary key auto_increment,
title varchar(255),
description text,
priority varchar(255),
status varchar(200),
start_date date,
due_date date,
create_at timestamp default current_timestamp

);