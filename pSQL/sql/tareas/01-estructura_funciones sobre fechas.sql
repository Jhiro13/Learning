CREATE TABLE regions (
	region_id INT PRIMARY KEY,
	region_name VARCHAR (25) DEFAULT NULL
);

CREATE TABLE countries (
	country_id CHAR (2) PRIMARY KEY,
	country_name VARCHAR (40) DEFAULT NULL,
	region_id INT NOT NULL,
	FOREIGN KEY (region_id) REFERENCES regions (region_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE locations (
	location_id INT PRIMARY KEY,
	street_address VARCHAR (40) DEFAULT NULL,
	postal_code VARCHAR (12) DEFAULT NULL,
	city VARCHAR (30) NOT NULL,
	state_province VARCHAR (25) DEFAULT NULL,
	country_id CHAR (2) NOT NULL,
	FOREIGN KEY (country_id) REFERENCES countries (country_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE jobs (
	job_id INT PRIMARY KEY,
	job_title VARCHAR (35) NOT NULL,
	min_salary DECIMAL (8, 2) DEFAULT NULL,
	max_salary DECIMAL (8, 2) DEFAULT NULL
);

CREATE TABLE departments (
	department_id INT PRIMARY KEY,
	department_name VARCHAR (30) NOT NULL,
	location_id INT DEFAULT NULL,
	FOREIGN KEY (location_id) REFERENCES locations (location_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE employees (
	employee_id INT PRIMARY KEY,
	first_name VARCHAR (20) DEFAULT NULL,
	last_name VARCHAR (25) NOT NULL,
	email VARCHAR (100) NOT NULL,
	phone_number VARCHAR (20) DEFAULT NULL,
	hire_date DATE NOT NULL,
	job_id INT NOT NULL,
	salary DECIMAL (8, 2) NOT NULL,
	manager_id INT DEFAULT NULL,
	department_id INT DEFAULT NULL,
	FOREIGN KEY (job_id) REFERENCES jobs (job_id) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (department_id) REFERENCES departments (department_id) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (manager_id) REFERENCES employees (employee_id)
);

CREATE TABLE dependents (
	dependent_id INT PRIMARY KEY,
	first_name VARCHAR (50) NOT NULL,
	last_name VARCHAR (50) NOT NULL,
	relationship VARCHAR (25) NOT NULL,
	employee_id INT NOT NULL,
	FOREIGN KEY (employee_id) REFERENCES employees (employee_id) ON DELETE CASCADE ON UPDATE CASCADE
);
------------------------------
select now(); -> da información de hoy
select now(), current_date, current_time; -> fecha actual y hora actual
select date_part('minutes', now());

select 
	max(hire_date),
	max(hire_date) + interval '1 day' as days,
	max(hire_date) + interval '1 month' as months,
	max(hire_date) + interval '1 year' as years,
	max(hire_date) + interval '1 day' + interval '1 year' as mmguevo,
	max(hire_date) + make_interval(years:=23),
	make_interval(years:=date_part('year', now()::integer))
from employees;

SELECT user_id, EXTRACT(DAY FROM (max(post_date)-min(post_date))) as days_between
from posts
where date_part('year', post_date::date)=2021
group by user_id
having not EXTRACT(DAY FROM (max(post_date)-min(post_date)))=0;

SELECT 
  sender_id,
  COUNT(message_id) AS count_messages
FROM messages
WHERE EXTRACT(MONTH FROM sent_date) = '8'
  AND EXTRACT(YEAR FROM sent_date) = '2022'
GROUP BY sender_id
ORDER BY count_messages DESC
LIMIT 2;

(select employee_count as unique_queries, count(employee_count)
from (select a.employee_id, count(a.employee_id) as employee_count
from queries a
inner join employees b on a.employee_id=b.employee_id
where (EXTRACT(month from a.query_starttime) BETWEEN 7 and 9) and (EXTRACT(year from a.query_starttime)=2023)
group by a.employee_id) as fck
group by employee_count);

select hire_date, extract(year from now())-extract(year from hire_date) as diferencia
from employees;

-------clausula case-then

select first_name, last_name, hire_date, 
	case 
		when hire_date > current_date - interval '1 year' then 'Rango A'
		when hire_date > current_date - interval '3 year' then 'Rango B'
		when hire_date > current_date - interval '6 year' then 'Rango C'
		else 'Rango D'
	end as rango_antiguedad
from employees
order by hire_date desc;