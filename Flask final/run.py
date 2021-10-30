
from flask import Flask, render_template, redirect, request, session, jsonify
import sqlite3, db, controlador
from functools import wraps
from flask.helpers import stream_with_context, url_for
from flask import flash
from sqlite3 import Error
from werkzeug.security import generate_password_hash, check_password_hash


app=Flask(__name__)
app.secret_key = "14151612"

@app.route('/')
def pInicio():
    return render_template('index.html')

def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'Administrador' in session:
            return test(*args, **kwargs)
        else:
            flash('you need to login first.')
            return redirect('/login/')
    return wrap

@app.route('/login/')
def pLogin():
    return render_template('login.html')

@app.route('/register/')
def pRegistro():
    return render_template('registro.html')

@app.route("/hacer_registro", methods=["POST"])
def hacer_registro():
    resul = ""
    if(request.method == "POST"):
        identificacion = request.form["identificacion"]
        name = request.form["name"]
        lastName = request.form["lastName"]
        phone = request.form["phone"]
        email = request.form["email"]
        passw = request.form["passw"]

        conn = sqlite3.connect("db/base_de_datos.db")
        user= conn.cursor()
        user.execute("SELECT * FROM Usuario WHERE IdUsuario = '"+identificacion+"' " )
        resul = user.fetchone()

        if (resul == None):
            password = generate_password_hash(request.form["passw"], method="sha256")
            controlador.registrar_usuario(identificacion,name,lastName,phone,email,password)      
            flash("Usuario registrado exitosamente")
            return redirect('/login')
        else:
            iduser = (resul[0])
            id_user = str(iduser)

            if ( id_user == identificacion):
                flash("El usuario ya se encuentra registrado, por favor verifique los datos ingresados e intente nuevamente")
                return redirect('/register/')
            
            

@app.route("/hacer_registrousuario", methods=["POST"])
@login_required
def hacer_registrousuario():
    identificacion = request.form["identificacion"]
    name = request.form["name"]
    lastName = request.form["lastName"]
    phone = request.form["phone"]
    email = request.form["email"]
    passw = request.form["passw"]
    conn = sqlite3.connect("db/base_de_datos.db")
    user= conn.cursor()
    user.execute("SELECT * FROM Usuario WHERE IdUsuario = '"+identificacion+"' " )
    resul = user.fetchone()
    
    if (resul == None):
        password = generate_password_hash(request.form["passw"], method="sha256")
        controlador.registrar_usuarioadmin(identificacion,name,lastName,phone,email,password)
        flash("El usuario fue registrado exitosamente")
        return redirect('/administrator')
    else:
        
        iduser = (resul[0])
        id_user = str(iduser)
        if ( id_user == identificacion):
            flash("El usuario ya se encuentra registrado, por favor verifique los datos ingresados e intente nuevamente")
            return redirect('/administrator/')
    
        
@app.route("/hacer_registropiloto", methods=["POST"])
@login_required
def hacer_registropiloto():
    identificacion = request.form["idpiloto"]
    name = request.form["namepiloto"]
    edad = request.form["edadpiloto"]
    phone = request.form["phonepiloto"]
    email = request.form["emailpiloto"]
    passw = request.form["passwpiloto"]

    conn = sqlite3.connect("db/base_de_datos.db")
    piloto= conn.cursor()
    piloto.execute("SELECT * FROM Piloto WHERE IdPiloto = '"+identificacion+"' " )
    resul = piloto.fetchone()
    
    if (resul == None):
        password = generate_password_hash(request.form["passwpiloto"], method="sha256")      
        controlador.registrar_pilotoadmin(identificacion,name,email,edad, phone,password)
        flash("El Piloto fue registrado exitosamente")
        return redirect('/administrator')
    else:
          
        pilotoadmin = (resul[0])
        id_piloto = str(pilotoadmin)
        if ( id_piloto == identificacion):
            flash("El piloto ya se encuentra registrado, por favor verifique los datos ingresados e intente nuevamente")   
            return redirect('/administrator/')
   


@app.route("/hacer_registrovuelo", methods=["POST"])
@login_required
def hacer_registrovuelo():
    idvuelo = request.form["idvuelo"]
    idpiloto = request.form["idpilotovuelo"]
    origen = request.form["origen"]
    destino = request.form["destino"]
    fecha = request.form["fecha"]
    hora = request.form["hora"]
    avion = request.form["avion"]
    costo = request.form["costo"]
    estado = request.form["estado"]
    conn = sqlite3.connect("db/base_de_datos.db")
    vuelo= conn.cursor()
    vuelo.execute("SELECT * FROM Vuelo WHERE IdVuelo = '"+idvuelo+"' " )
    resul = vuelo.fetchone()
    
    if (resul == None):
        controlador.registrar_vuelo(idvuelo,idpiloto,origen,destino, fecha,hora,avion,costo,estado)
        flash("El Vuelo fue registrado exitosamente")
        return redirect('/administrator/')
    else:
        idvuel= (resul[0])
        id_vuelo = str(idvuel)
        if ( id_vuelo == idvuelo):
            flash("El Vuelo ya se encuentra registrado, por favor verifique los datos ingresados e intente nuevamente")   
            return redirect('/administrator/#modal3')
    
@app.route("/hacer_registroreserva", methods=["POST"])
@login_required
def hacer_registroreserva():
    idreserva = request.form["idreserva"]
    idvuelo = request.form["idvuelo"]
    idusuario = request.form["idusuario"]
    asiento = request.form["asiento"]
    calificacion = request.form["calificacion"]
    comentario = request.form["comentario"] 

    conn = sqlite3.connect("db/base_de_datos.db")
    reserva= conn.cursor()
    reserva.execute("SELECT * FROM Reserva WHERE IdReserva = '"+idreserva+"' " )
    resul = reserva.fetchone()
    
    if (resul == None):
        controlador.registrar_reservaadmin(idreserva,idusuario,idvuelo,asiento, calificacion,comentario)
        flash("La reserva fue registrado exitosamente")
        return redirect('/administrator/')
    else:
        idrese= (resul[0])
        id_reser = str(idrese)
        if ( id_reser == idreserva):
            flash("Esta reserva ya se encuentra registrada, por favor verifique los datos ingresados e intente nuevamente")   
            return redirect('/administrator/')


@app.route('/reservar/<string:VueloId>/<string:UsuarioId>')
def Reservar(VueloId, UsuarioId):
    reservas = controlador.buscarasiento(VueloId)
    if (len(reservas)<100):
        asiento= str(len(reservas)+1)
        idReserva= VueloId+asiento
        controlador.reservar(idReserva, UsuarioId, VueloId, asiento,0,0) 
        
        return "Reserva Exitosa, su codigo de reserva es: "+ idReserva +" su vuelo es : "+VueloId
    else:
        return "El vuelo está lleno"



@app.route('/vuelo_user/')
def vuelo_user():
    return render_template("vuelo_user.html")

@app.route("/buscar_reservas", methods=["POST", "GET"])
def buscar_reservas():
    id = request.form["vuelouser"]    
    conn = sqlite3.connect("db/base_de_datos.db")
    reserva= conn.cursor()
    reserva.execute("SELECT * FROM Vuelo WHERE IdVuelo = '"+id+"' " )
    resul = reserva.fetchall()
    conn.close
    reserv = request.form["reserva"]
    conne = sqlite3.connect("db/base_de_datos.db")
    Vreserva= conne.cursor()
    Vreserva.execute("SELECT * FROM Reserva WHERE IdReserva = '"+reserv+"' " )
    resultado = Vreserva.fetchall()

    return render_template('vuelo_user.html', vuelouser = resul, Dreserva = resultado)

@app.route("/enviar_calificacion/<string:ReservaId>", methods=["POST", "GET"])
def enviar_calificacion(ReservaId):
    calif = request.form.get('Calificacion') 
    comentario = request.form["comentario"]
    conn = sqlite3.connect("db/base_de_datos.db")
    reserva= conn.cursor()
    reserva.execute("UPDATE Reserva SET Calificacion = '"+calif+"', Comentario = '"+comentario+"' WHERE IdReserva = "+ReservaId+" " )
    conn.commit()
    conn.close
    return redirect('/vuelo_user')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')


@app.route("/hacer_login", methods=["POST", "GET"])

def hacer_login():
    r = ""
    if(request.method == "POST"):
        email = request.form["email"]
        passw = request.form["passw"]
        Rol = request.form["Rol"]
        conn = sqlite3.connect("db/base_de_datos.db")
        admin= conn.cursor()
        admin.execute("SELECT * FROM Administrador WHERE Email = '"+email+"'" )
        r = admin.fetchall()
        for i in r:
            passwor=  (i[2])
            contrasena =check_password_hash(passwor,passw)
            if (email == i [1] and contrasena):
                session["loged"] = True
                session["email"]= email
                session["Rol"] = Rol
                session["Administrador"]=True
                return redirect('/administrator/')       

    if(request.method == "POST"):
        email = request.form["email"]
        passw = request.form["passw"]
        Rol = request.form["Rol"]
        conn = sqlite3.connect("db/base_de_datos.db")
        user= conn.cursor()
        user.execute("SELECT * FROM Usuario WHERE Email = '"+email+"' " )
        r = user.fetchall()
        for i in r:
            id = (i[0])
            name = (i[1])
            passwo=  (i[5])
            contrasena =check_password_hash(passwo,passw)
                
            if (email == i [4] and contrasena):
                session["loged"] = True
                session["email"]= email
                session["nombre"]= name
                session["Rol"] = Rol
                session["id"] = id
                return redirect('/user/')
        
    if(request.method == "POST"):
        email = request.form["email"]
        passw = request.form["passw"]
        Rol = request.form["Rol"]
        conn = sqlite3.connect("db/base_de_datos.db")
        piloto= conn.cursor()
        piloto.execute("SELECT * FROM Piloto WHERE Email = '"+email+"' " )
        r = piloto.fetchall()
        
        for i in r:
            id= (i[0])
            name = (i[1])
            passwo=  (i[5])
            contrasena =check_password_hash(passwo,passw)
            id_pilot = str(id)
            connexion = sqlite3.connect("db/base_de_datos.db")
            conn= connexion.cursor()
            conn.execute("SELECT * FROM Vuelo WHERE Piloto_id = '"+id_pilot+"'" )
            resultado = conn.fetchall()
            if (email == i [2] and contrasena):
                session["loged"] = True
                session["email"]= email
                session["id"] =id
                session["nombre"]= name
                session["Rol"] = Rol

                if 'email' in session and session["Rol"]=="Piloto":
        
                    return render_template('piloto.html', pilot = r[0], vuelos = resultado)
                else:
                    flash("No tiene permisos para ingresar a esta zona ingrese su rol correspondiente")
                    return redirect('/login') 
                    
    flash('La contraseña o el usuario son incorrectos')            
    return redirect('/login') 

 

@app.route('/administrator/')
def pSadmin():
    if 'email' in session and session["Rol"]=="Administrador":
        pilot = controlador.leerpiloto()
        user = controlador.leerusuario()
        vuel = controlador.leervuelo()
        rese = controlador.leerreservas()
        return render_template('administrador.html', pilotos = pilot , users = user, vuelos = vuel , reservas = rese)
    else:
        flash("No tiene permisos para ingresar a esta zona ingrese su rol correspondiente")
        return redirect('/login') 
    
@app.route('/user/')
def Usuario():
    if 'email' in session and session["Rol"]=="Usuario":
        result = controlador.leervuelo()
        return render_template('usuario.html',Vuelo= result)
    else:
        flash("No tiene permisos para ingresar a esta zona ingrese su rol correspondiente")
        return redirect('/login') 


@app.route('/delete/<string:id>')
@login_required
def delete_user(id):
    conn = sqlite3.connect("db/base_de_datos.db")
    delete= conn.cursor()
    delete.execute("DELETE FROM Usuario WHERE IdUsuario = {0}".format(id))
    conn.commit()
    conn.close
    flash("Registro del usuario eliminado")
    return redirect('/administrator/') 


@app.route('/deletePiloto/<string:id>')
@login_required
def delete_piloto(id):
    conn = sqlite3.connect("db/base_de_datos.db")
    delete= conn.cursor()
    delete.execute("DELETE FROM Piloto WHERE IdPiloto = {0}".format(id))
    conn.commit()
    conn.close
    flash("Registro del Piloto eliminado")
    return redirect('/administrator/')


@app.route('/deleteVuelo/<string:id>')
@login_required
def delete_vuelo(id):
    conn = sqlite3.connect("db/base_de_datos.db")
    delete= conn.cursor()
    delete.execute("DELETE FROM Vuelo WHERE IdVuelo = {0}".format(id))
    conn.commit()
    conn.close
    flash("Registro del vuelo eliminado")
    return redirect('/administrator/')

@app.route('/deleteReserva/<string:id>')
@login_required
def delete_Reserva(id):
    conn = sqlite3.connect("db/base_de_datos.db")
    delete= conn.cursor()
    delete.execute("DELETE FROM Reserva WHERE IdReserva = {0}".format(id))
    conn.commit()
    conn.close
    flash("Registro de Reserva eliminado")
    return redirect('/administrator/')


@app.route('/edit/<id>')
@login_required
def get_user(id):
    conn = sqlite3.connect("db/base_de_datos.db")
    edit= conn.cursor()
    edit.execute("SELECT * FROM Usuario WHERE IdUsuario = '"+id+"'")
    data = edit.fetchall()
    return render_template('edit_user.html',user = data[0])

@app.route('/update_user/<id>',  methods=["POST"])
@login_required
def update_user(id):
    if (request.method == 'POST'):
        identificacion = request.form["iduser"]
        name = request.form["nameuser"]
        lastName = request.form["lastNameuser"]
        phone = request.form["phoneuser"]
        email = request.form["emailuser"]
        passw = request.form["passwuser"]
        password = generate_password_hash(request.form["passwuser"], method="sha256")
        conexion = sqlite3.connect("db/base_de_datos.db")
        upda= conexion.cursor()
        upda.execute(f"""UPDATE Usuario 
                        SET IdUsuario ='{identificacion}',
                        Name ='{name}',
                        Apellido ='{lastName}',
                        Telefono = '{phone}',
                        Email ='{email}',
                        Password ='{password}'
                        WHERE IdUsuario = '{id}';""")
        conexion.commit()
        conexion.close
        flash("Datos del Usuario actualizados correctamente")
        return redirect('/administrator/')

@app.route('/editpiloto/<id>')
@login_required
def get_piloto(id):
    conn = sqlite3.connect("db/base_de_datos.db")
    edit= conn.cursor()
    edit.execute("SELECT * FROM Piloto WHERE IdPiloto = '"+id+"'")
    data = edit.fetchall()
    return render_template('edit_piloto.html',piloto = data[0])

@app.route('/update_piloto/<id>',  methods=["POST"])
@login_required
def update_piloto(id):
    if (request.method == 'POST'):
        identificacion = request.form["idpiloto"]
        name = request.form["namepiloto"]
        edad = request.form["edadpiloto"]
        phone = request.form["phonepiloto"]
        email = request.form["emailpiloto"]
        passw = request.form["passwpiloto"]
        password = generate_password_hash(request.form["passwpiloto"], method="sha256")
        conexion = sqlite3.connect("db/base_de_datos.db")
        update= conexion.cursor()
        update.execute(f"""UPDATE Piloto 
                        SET IdPiloto ='{identificacion}',
                        Name ='{name}',
                        Email ='{email}',
                        Edad ='{edad}',
                        Phone = '{phone}',
                        Password ='{password}'
                        WHERE IdPiloto = '{id}';""")
        conexion.commit()
        conexion.close
        flash("Datos del piloto actualizados correctamente")
        return redirect('/administrator/')

@app.route('/editVuelo/<id>')
@login_required
def get_vuelo(id):
    conn = sqlite3.connect("db/base_de_datos.db")
    edit= conn.cursor()
    edit.execute("SELECT * FROM Vuelo WHERE IdVuelo = '"+id+"'")
    data = edit.fetchall()
    pilot = controlador.leerpiloto()
    return render_template('edit_vuelo.html',vuelo = data[0], pilotos = pilot)

@app.route('/update_vuelo/<id>',  methods=["POST"])
@login_required
def update_vuelo(id):
    if (request.method == 'POST'):
        idvuelo = request.form["idvueloedit"]
        idpiloto = request.form["idpiloto"]
        origen = request.form["origenedit"]
        destino = request.form["destinoedit"]
        fecha = request.form["fechaedit"]
        hora = request.form["horaedit"]
        avion = request.form["avionedit"]
        costo = request.form["costoedit"]
        estado = request.form["estadoedit"]   
        conexion = sqlite3.connect("db/base_de_datos.db")
        update= conexion.cursor()
        update.execute(f"""UPDATE Vuelo 
                        SET IdVuelo ='{idvuelo}',
                        Piloto_id ='{idpiloto}',
                        Origen ='{origen}',
                        Destino ='{destino}',
                        Fecha = '{fecha}',
                        Hora ='{hora}',
                        Avion ='{avion}',
                        Costo = '{costo}',
                        Estado ='{estado}'
                        WHERE IdVuelo = '{id}';""")
        conexion.commit()
        conexion.close
        flash("Datos del Vuelo actualizados correctamente")
        return redirect('/administrator/')


@app.route('/editReserva/<id>')
@login_required
def get_reserva(id):
    conn = sqlite3.connect("db/base_de_datos.db")
    edit= conn.cursor()
    edit.execute("SELECT * FROM Reserva WHERE IdReserva = '"+id+"'")
    data = edit.fetchall()
    return render_template('edit_reserva.html',reserva = data[0])

@app.route('/update_reserva/<id>',  methods=["POST"])
@login_required
def update_reserva(id):
    if (request.method == 'POST'):
        idreserva = request.form["idreserva"]
        idvuelo = request.form["idvuelo"]
        idusuario = request.form["idusuario"]
        asiento = request.form["asiento"]
        calificacion = request.form["calificacion"]
        comentario = request.form["comentario"]
        conexion = sqlite3.connect("db/base_de_datos.db")
        update= conexion.cursor()
        update.execute(f"""UPDATE Reserva 
                        SET IdReserva ='{idreserva}',
                        Usuario_id ='{idusuario}',
                        Vuelo_id ='{idvuelo}',
                        Asiento ='{asiento}',
                        Calificacion = '{calificacion}',
                        Comentario ='{comentario}'
                        WHERE IdReserva = '{id}';""")
        conexion.commit()
        conexion.close
        flash("Datos de la reserva actualizados correctamente")
        return redirect('/administrator/')

@app.route('/change/')
@login_required
def get_admin():    
    return render_template('change_admin.html')

@app.route('/updateadmin/',  methods=["POST", "GET"])
@login_required
def update_admin():      
    if (request.method == 'POST'):
        emailactual =request.form["emailactual"]
        IdNuevo = request.form["IdNuevo"]
        emailnuevo = request.form["emailnuevo"]
        newpassword = request.form["newpassword"]
        confirmcontrasena = request.form["confirmcontrasena"]
        conexion = sqlite3.connect("db/base_de_datos.db")
        query = "SELECT * FROM Administrador"
        cursor = conexion.cursor()
        cursor.execute(query)
        resul = cursor.fetchall()
        for r in resul:
            emaildata = (r[1])
            if(emailactual != emaildata):
                flash("El correo actual no coincide con el ingresado")
                return redirect('/change/')
            else:
                if (newpassword == confirmcontrasena):
                    password = generate_password_hash(request.form["newpassword"], method="sha256")
                    conexion = sqlite3.connect("db/base_de_datos.db")
                    change= conexion.cursor()
                    change.execute(f"""UPDATE Administrador 
                                    SET Id_Admin ='{IdNuevo}',
                                    Email ='{emailnuevo}',
                                    Password ='{password}'
                                    WHERE Email = '{emailactual}';""")
                    conexion.commit()
                    conexion.close
                    session.clear()
                    flash("Datos actualizados correctamente inicie sesión")
                    return redirect('/login')
                else:
                    flash("Las contraseñas no coinciden")
                    return redirect('/change/')



@app.route('/buscarusuario/')
@login_required
def buscarusuario():
    return render_template("buscar.html")

@app.route('/buscar/',  methods=["POST", "GET"])
@login_required
def buscar():
        
        searchUser=request.form["searchUser"]
        conn = sqlite3.connect("db/base_de_datos.db")
        users= conn.cursor()
        users.execute("SELECT * FROM Usuario WHERE IdUsuario = '"+searchUser+"'")
        data = users.fetchall()
        
        
        return render_template('buscar.html', busca=data)

@app.route('/buscarpiloto/')
@login_required
def buscar_piloto():
    return render_template("buscarpiloto.html")

@app.route('/buscarPiloto/',  methods=["POST", "GET"])
@login_required
def buscarPiloto():
    
        searchPiloto=request.form["searchPiloto"]
        conn = sqlite3.connect("db/base_de_datos.db")
        piloto= conn.cursor()
        piloto.execute("SELECT * FROM Piloto WHERE IdPiloto = '"+searchPiloto+"'")
        datapiloto = piloto.fetchall()

        return render_template('buscarpiloto.html', buscapiloto = datapiloto)    

@app.route('/buscarvuelo/')
@login_required
def buscar_vuelo():
    return render_template("buscarvuelo.html")

@app.route('/buscarVuelo/',  methods=["POST", "GET"])
@login_required
def buscarVuelo():
    
        searchvuelo=request.form["searchvuelo"]
        conn = sqlite3.connect("db/base_de_datos.db")
        vuelo= conn.cursor()
        vuelo.execute("SELECT * FROM Vuelo WHERE IdVuelo = '"+searchvuelo+"'")
        datavuelo = vuelo.fetchall()

        return render_template('buscarvuelo.html', buscavuelo = datavuelo)    

@app.route('/buscarReserva/')
@login_required
def buscar_reservadmin():
    return render_template("buscarReserva.html")

@app.route('/buscarReservaadmin/',  methods=["POST", "GET"])
@login_required
def buscarReservaadmin():
    
        searchreserva=request.form["searchreserva"]
        conn = sqlite3.connect("db/base_de_datos.db")
        reserva= conn.cursor()
        reserva.execute("SELECT * FROM Reserva WHERE IdReserva = '"+searchreserva+"'")
        datareserva = reserva.fetchall()

        return render_template('buscarReserva.html', buscareserva = datareserva)    