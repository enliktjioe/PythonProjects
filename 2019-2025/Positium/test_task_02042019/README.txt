
--General objective: Create a Python script that downloads, inserts to PostrgreSQL/PostGIS and validates the geometries of ISO 3166-1 alpha-2 (iso_a2) country list. 

--Guidelines:
--For each (or at least for as many as possible) country codes of iso_a2 list, there should be a geometry (multipolygon) in WGS84 (srs=4326), which is valid
--Locate the open-source geospatial database that geometries of countries could be downloaded from. Preferably single location for all countries.
--Create a Python script (script and config.py should be separate files) that
a) downloads the geometries from the source;
b) imports the geometries to PostGIS (preferably use shp2psql, use intermediate import table, or directly to geom table), checks for the validity of the geometries (PostGIS - ST_IsValid, ST_NDims, ST_GeometryType), corrects if necessary (ST_MakeValid);
c) links each iso_a2 code to a specific geometry (via geom_id).

--The iso_a2 list is provided, the source data for geometries is to be found from the web.
--If some geometries are not imported (don't exist, can't be found), then leave geom_id as NULL
--If some geometries are not valid and can't be fixed, then Python has to report that for this country, the geometry is not valid and leave geom_id as NULL
--The structure of the tables can be altered slightly - the main logic is that there should be two tables (iso_a2_list and geom) which are linked by geom_id. Intermediate temp tables for importing and processing can be created, but deleted after the import. You can add additional attributes to iso_a2_list and geom tables, if you feel necessary, but this requires an explanation why they are needed.
--Geometries should not be too large, the range of the total size of downloadable geometries: 1MB ... 1GB. 

--RESULT should be two Python files (config file and script itself), and SQL for DB structure, if different from what is below.

-- 2 related input files:
--- iso_a2_list.csv    (reference data about countries)
--- gis.sql   (commands for database schema etc)
