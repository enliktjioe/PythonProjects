#!/usr/bin/python

hostname = 'localhost'
username = 'enlik'
database = 'positiumDB'

print "Using psycopg2…"
import psycopg2
conn = psycopg2.connect( host=hostname, user=username, dbname=database )
cur = conn.cursor()
print("Database opened successfully")