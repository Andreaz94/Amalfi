from flask import render_template
from db import conexion_bd

def registrar_usuario(IdUsuario, Name, Apellido, Telefono, Email, Password):
    conexion = conexion_bd()
    strsql = "INSERT into Usuario (IdUsuario, Name, Apellido, Telefono ,Email, Password) values ({},'{}','{}',{},'{}','{}')".format(IdUsuario, Name, Apellido, Telefono,Email, Password)

    cursor = conexion.cursor()
    cursor.execute(strsql)
    conexion.commit()
    conexion.close 


def registrar_usuarioadmin(IdUsuario, Name, Apellido, Telefono, Email, Password):
    conexion = conexion_bd()
    sqluser = "INSERT into Usuario (IdUsuario, Name, Apellido, Telefono ,Email, Password) values ('{}','{}','{}','{}','{}','{}')".format(IdUsuario, Name, Apellido, Telefono,Email, Password)

    cursor = conexion.cursor()
    cursor.execute(sqluser)
    conexion.commit()
    conexion.close

def registrar_pilotoadmin(IdPiloto, Name, Email, Edad, Phone, Password):
    conexion = conexion_bd()
    sqlpiloto = "insert into Piloto (IdPiloto, Name, Email, Edad, Phone, Password) values ('{}','{}','{}','{}','{}','{}')".format(IdPiloto, Name, Email, Edad, Phone, Password)

    cursor = conexion.cursor()
    cursor.execute(sqlpiloto)
    conexion.commit()
    conexion.close

def registrar_vuelo(IdVuelo, Piloto_id, Origen, Destino, Fecha, Hora, Avion, Costo, Estado):
    conexion = conexion_bd()
    sqlvuelo = "insert into Vuelo (IdVuelo, Piloto_id, Origen, Destino, Fecha, Hora, Avion, Costo, Estado) values('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(IdVuelo, Piloto_id, Origen, Destino, Fecha, Hora, Avion, Costo, Estado)

    cursor = conexion.cursor()
    cursor.execute(sqlvuelo)
    conexion.commit()
    conexion.close

def registrar_reservaadmin(IdReserva, Usuario_id, Vuelo_id, Asiento, Calificacion, Comentario):
    conexion = conexion_bd()
    sqlreserva = "insert into Reserva (IdReserva, Usuario_id, Vuelo_id, Asiento, Calificacion, Comentario) values ('{}','{}','{}','{}','{}','{}')".format(IdReserva, Usuario_id, Vuelo_id, Asiento, Calificacion, Comentario)

    cursor = conexion.cursor()
    cursor.execute(sqlreserva)
    conexion.commit()
    conexion.close
        
def leervuelo():
    conexion = conexion_bd()
    query = "SELECT * FROM Vuelo"
    cursor = conexion.cursor()
    cursor.execute(query)
    resul = cursor.fetchall()
    return resul

def leerusuario():
    conexion = conexion_bd()
    query = "SELECT * FROM Usuario"
    cursor = conexion.cursor()
    cursor.execute(query)
    resul = cursor.fetchall()
    return resul

def leerpiloto():
    conexion = conexion_bd()
    query = "SELECT * FROM Piloto"
    cursor = conexion.cursor()
    cursor.execute(query)
    resul = cursor.fetchall()
    return resul

def leerreservas():
    conexion = conexion_bd()
    query = "SELECT * FROM Reserva"
    cursor = conexion.cursor()
    cursor.execute(query)
    resul = cursor.fetchall()
    return resul

def reservar(IdReserva, UsuarioId, VueloId, Asiento, Calificacion, Comentario):
    conexion = conexion_bd()
    strsql = "insert into Reserva (IdReserva, Usuario_id, Vuelo_id, Asiento, Calificacion, Comentario ) values ('{}','{}','{}','{}','{}','{}')".format(IdReserva,UsuarioId,VueloId,Asiento,Calificacion,Comentario)

    cursor = conexion.cursor()
    cursor.execute(strsql)
    conexion.commit()
    conexion.close 

def comentarios(Calificacion,Comentario):
    conexion = conexion_bd()
    strsql = "insert into Reserva (Calificacion, Comentario ) values ('{}','{}')".format(Calificacion,Comentario)

    cursor = conexion.cursor()
    cursor.execute(strsql)
    conexion.commit()
    conexion.close 



def buscarasiento(VueloId):
    conexion = conexion_bd()
    strsql = "SELECT * FROM Reserva WHERE Vuelo_id = '"+VueloId+"' "

    cursor = conexion.cursor()
    cursor.execute(strsql)
    resul = cursor.fetchall()
    print(resul)
    return resul 


""" def obtener_registros(tabla, condicion):
    conexion = conexion_bd()
    cursor = conexion.cursor()

    if condicion == None:
        strsql = 'SELECT * FROM {}'.format(tabla)
    else:
        strsql = 'SELECT * FROM {} WHERE {}'.format(tabla, condicion)

    cursor.execute(strsql)

    datos = cursor.fetchall()
    conexion.close()

    return datos """