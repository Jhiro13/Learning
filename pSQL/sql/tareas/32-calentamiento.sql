-- Nombre, apellido e IP, donde la última conexión se dió de 221.XXX.XXX.XXX

select first_name, last_name, last_connection
from users
where last_connection like '221%';

-- Nombre, apellido y seguidores(followers) de todos a los que lo siguen más de 4600 personas

select first_name,last_name,followers
from users
where following>=4600;
#aggregate FUNCTIONs
select 
count(*) as total_users, 
min(followers), max(followers), 
avg(followers), sum(followers)/count(*),
round(avg(followers))
from users;
#between
select count(*), followers -- una función agregada no junto con columna, se tiene que agregar group by
from users
where followers between 4700 and 4999
group by followers
order by count(*) desc;

--terminología
DDL -> DATA DEFINITION LANGUAGE (create, alter, drop, truncate)
DML -> DATA MANIPULATION LANGUAGE (insert, delete, update)
TCL -> TRANSACTION CONTROL LANGUAGE (commit, rollback)
DQL -> DATA QUERY LANGUAGE (select)
--- la estructura es
select ...
where ...
join ...
group by ...
having ... --es como el where solo que es para las aggregate functions como el count(*)
order by ...
limit ...
offset ...
#having
select count(*),country
from users
group by country
having count(*) between 6 and 9
order by count(*) desc;
#distinct
select DISTINCT country from users; --solo un pais te selecciona, no repite (se basa en lo escrito)