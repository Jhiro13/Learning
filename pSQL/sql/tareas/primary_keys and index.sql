alter table country
	add primary key (code); -- agregas pk de forma manual

alter table country
	add check (surfacearea >=0); -- agrega un check que restringe

alter table country
	add check ((continent='Asia') or
	(continent='South America') or 
	(continent='North America') or
	(continent='Oceania') or
	(continent='Antarctica') or
	(continent='Africa') or 
	(continent='Europe') or
	(continent='Central America'));

alter table country
	drop constraint "country_continent_check"; --primero tienes que hacer esto antes de modificar el constraint

create unique index "unique_country_name" on country (name); --esta nota es para optimizar queries
create index "country_continent" on country (
	continent
);