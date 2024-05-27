import sqlite3

def import_films():
    conn=sqlite3.connect("./instance/filmfan.db")
    c=conn.cursor()
    c.execute()
    conn.commit()

import_films()

def import_regisseurs():
    conn=sqlite3.connect("./instance/filmfan.db")
    c=conn.cursor()
    c.execute()
    conn.commit()

import_regisseurs()

def import_acteurs():
    conn=sqlite3.connect("./instance/filmfan.db")
    c=conn.cursor()
    c.execute()
    conn.commit()

import_acteurs()