-- creando una vista
create or replace view comments_per_week as (
select date_trunc('week', a.created_at) as weeks, sum(b.counter) as total_claps, count(distinct a.post_id) as number_of_posts, count(*) as number_of_claps
from posts a
inner join claps b on a.post_id=b.post_id
group by weeks
order by weeks desc);

select *
from comments_per_week;
DROP VIEW comments_per_week;

-- creando una vista materializada (ojo esto guarda la tabla en memoria)
create or replace materialized view comments_per_week_mat as (
select date_trunc('week', a.created_at) as weeks, sum(b.counter) as total_claps, count(distinct a.post_id) as number_of_posts, count(*) as number_of_claps
from posts a
inner join claps b on a.post_id=b.post_id
group by weeks
order by weeks desc);

select *
from comments_per_week_mat;
DROP VIEW comments_per_week_mat;
REFRESH MATERIALIZED view comments_per_week_mat;---esto es para actualizar la vista materializada
ALTER VIEW comments_per_week RENAME TO callamrd;
----CTE----
with recursive countup (val) as (
	select 1 as val
	union
	select val+1 from countup where val<10
)
select *
from countup;
---tabla de multiplicar
with recursive multiplication_table(base, numbers, resultado) as (
	select 5 as base, 1 as numbers, 5 * 1 as resultado
	union
	select 5 as base, numbers+1, numbers * base from multiplication_table where numbers<10
)
select *
from multiplication_table;

with RECURSIVE bosses as(
    select id, name, rerport_to
    from employees
    union
    select a.id, a.name, a.report_to
    from employees a
    inner join bosses b on b.id=a.report_to
)
select *
from bosses;

with RECURSIVE bosses  as(
    select id, name, rerport_to
    from employees
    union
    select a.id, a.name, a.report_to
    from employees a
    inner join bosses b on b.id=a.report_to
)
select *
from bosses;