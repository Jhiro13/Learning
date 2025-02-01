select *
from continent where name like '%America%'
union -- no hace otra cosa que unir
select *
from continent where code in (1,3,5);
-- JOIN
select a.name as country, b.name as continent 
from country a
inner join continent b on a.continent=b.code
order by a.name asc;
-- ESTO ES PARA REINICIAR SECUENCIA POR CODIGO NMS
alter SEQUENCE continent_code_seq RESTART with 9;
-- full outer join
select a.name, a.continent as continentCode, b.name as continentName
from country a
full outer join continent b on a.continent=b.code
order by a.name desc;
--left and right
select a.name, a.continent, b.name
from country a
right outer join continent b on a.continent=b.code
where a.continent is null;
-- aggregations con joins
select count(*), b.name
from country a
inner join continent b on a.continent=b.code
group by b.name
order by count(*) desc;
--moreeeeeeeeeeee
(select count(*) as Total, b.name as Continent
from country a
inner join continent b on a.continent=b.code
where b.name not like '%America%'
group by b.name)
union
(select count(*) as Total, 'America'
from country a
inner join continent b on a.continent=b.code
where b.name like '%America%')
order by Total asc;
--el segundo país con más ciudades
select count(*), b.name
from city a
inner join country b on a.countrycode=b.code
group by b.name
order by count(*) desc
limit 1
offset 1;
--- multiples joins
select distinct a.language, c.name
from countrylanguage a
inner join country b on a.countrycode=b.code
inner join continent c on b.continent=c.code
where a.isofficial is true
order by c.name asc;
--- mas de esa nota
select count(*), continent
from (select distinct a.language, c.name as continent
	from countrylanguage a
	inner join country b on a.countrycode=b.code
	inner join continent c on b.continent=c.code
	where a.isofficial is true
	order by c.name asc)
as totti ---recuerda: cuando haces subqueries debes ponerle un alias al query principal
group by continent
order by count(*) desc;