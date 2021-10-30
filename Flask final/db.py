import sqlite3
from sqlite3 import Error

def conexion_bd():
    try:
        conexion = sqlite3.Connection('db/base_de_datos.db')
        return conexion
    except Error:
        print(Error)