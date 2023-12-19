create table users( id integer AUTOINCREMENT PRIMARY key, name text not null, password text not null, admin boolean not null DEFAULT '0');

create table emp (empid integer AUTOINCREMENT PRIMARY key, name text not null, email text, phone integer, address text, joining_date timestamp DEFAULT CURRENT_TIMESTAMP, total_projects integer DEFAULT 1, total_test_case integer DEFAULT 1, total_defects_found integer DEFAULT 1, total_defects_pending integer DEFAULT 1);

