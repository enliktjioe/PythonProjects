--create schema
DROP SCHEMA test_gis CASCADE;
CREATE SCHEMA test_gis;

--create iso_a2 list table
DROP TABLE IF EXISTS test_gis.iso_a2_list;
CREATE TABLE test_gis.iso_a2_list (id serial primary key, iso_a2 varchar(2), country_name_eng varchar(50), geom_id int);

--create geometries table
DROP TABLE IF EXISTS test_gis.geom;
CREATE TABLE test_gis.geom (geom_id serial primary key, geom geometry (MULTIPOLYGON, 4326));

--populate iso_a2 list (250 country codes)
COPY test_gis.iso_a2_list (iso_a2, country_name_eng) FROM '/Users/enlik/Documents/Workspaces/PythonProjects/Positium/test_task_02042019/iso_a2_list.csv' WITH CSV HEADER DELIMITER ';' ENCODING 'UTF-8';
