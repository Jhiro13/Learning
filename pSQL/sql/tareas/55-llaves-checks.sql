

-- 1. Crear una llave primaria en city (id)

alter table city
	add primary key (id);
-- 2. Crear un check en population, para que no soporte negativos
alter table city
	add check (population>=0);

-- 3. Crear una llave primaria compuesta en "countrylanguage"
-- los campos a usar como llave compuesta son countrycode y language
alter table city
	add check (population>=0);

-- 4. Crear check en percentage, 
-- Para que no permita negativos ni números superiores a 100
alter table countrylanguage
	add check (percentage between 0 and 100);

alter table city
	add foreign key (countrycode)
	references country(code);
#CASCADA UPDATE AND DELETE
-- es para que todo se ejecute en todas las tablas relacionadas