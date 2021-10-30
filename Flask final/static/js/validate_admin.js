function validar_registrousuario() {
    let documento = document.getElementById("identificacion").value
    let nombres = document.getElementById("name").value
    let apellidos = document.getElementById("lastName").value
    let telefono = document.getElementById("phone").value
    let correo = document.getElementById("email").value
    let contrasena = document.getElementById("passw").value
    let sw = true

    if (documento.length <1) {
        alert("El documento esta vacio")
        sw = false
    }else if (documento.length < 7 ) {
        alert("El documento debe tener como minimo 7 numeros")
        sw = false}

        if (/^\d+$/i.test(documento)){
        }else{
            alert("El documento debe tener solo numeros")
            sw=false
        }

    if (nombres.length < 1) {
        alert("El nombre esta vacio")
        sw = false
    } else if (nombres.length < 3 ) {
        alert("El nombre debe tener como minimo 3 caracteres")
        sw = false
    }
    if (/^[a-zA-ZÀ-ÿ\u00f1\u00d1]+(\s*[a-zA-ZÀ-ÿ\u00f1\u00d1]*)*[a-zA-ZÀ-ÿ\u00f1\u00d1]+$/i.test(nombres)){
    }else{
        alert("El Nombre debe tener solo letras")
        sw=false
    }
    
    if (apellidos.length < 1) {
        alert("Apellidos esta vacio")
        sw = false
    } else if (apellidos.length < 3 ) {
        alert("El apellido debe tener como minimo 3 caracteres")
        sw = false
    }
        if (/^[a-zA-ZÀ-ÿ\u00f1\u00d1]+(\s*[a-zA-ZÀ-ÿ\u00f1\u00d1]*)*[a-zA-ZÀ-ÿ\u00f1\u00d1]+$/i.test(apellidos)){
        }else{
            alert("Los apellidos deben tener solo letras")
            sw=false
        }
    if (telefono.length < 1) {
        alert("El telefono esta vacio")
        sw = false
    }else if (telefono.length < 7 ) {
        alert("El telefono debe tener como minimo 7 numeros")
        sw = false
    } 
        if (/^\d+$/i.test(telefono)){
        }else{
            alert("El telefono debe tener solo numeros")
            sw=false
        }

    if (correo.length < 1) {
        alert("El Usuario esta vacio")
        sw = false
    } else {
        if (correo.includes("@")) {
            let separador = correo.split("@")
            let usuario = separador[0]
            if (usuario.length < 1) {
                alert("El correo no tiene el usuario")
                sw = false
            } else {
                let nombreDominio = separador[1]
                if (nombreDominio.includes(".")) {
                    separador = nombreDominio.split(".")
                    let dominio = separador[0]
                    let extension = separador[1]
                    if (dominio.length < 1) {
                        alert("El correo no tiene dominio")
                        sw = false
                    }

                    if (extension.length < 1) {
                        alert("El correo no tiene extension")
                        sw = false
                    }
                } else {
                    alert("El correo no tiene el .")
                    sw = false
                }
            }
        } else {
            alert("El correo no tiene el @")
            sw = false
        }
    }

    if (contrasena.length < 1) {
        alert("El campo contraseña esta vacio")
        sw = false
    } else if (contrasena.length < 8 ) {
        alert("La contraseña debe tener como minimo 8 caracteres")
        sw = false
    }


    return sw
}
/* function mensaje(){
    
    window.alert("Registro exitoso")
} */

function validar_registropiloto() {
    let documento = document.getElementById("idpiloto").value
    let nombres = document.getElementById("namepiloto").value
    let telefono = document.getElementById("phonepiloto").value
    let correo = document.getElementById("emailpiloto").value
    let contrasena = document.getElementById("passwpiloto").value
    let edad = document.getElementById("edadpiloto").value
    let sw = true

    if (documento.length <1) {
        alert("El documento esta vacio")
        sw = false
    }else if (documento.length < 7 ) {
        alert("El documento debe tener como minimo 7 numeros")
        sw = false}

        if (/^\d+$/i.test(documento)){
        }else{
            alert("El documento debe tener solo numeros")
            sw=false
        }

    if (nombres.length < 1) {
        alert("El nombre esta vacio")
        sw = false
    } else if (nombres.length < 3 ) {
        alert("El nombre debe tener como minimo 3 caracteres")
        sw = false
    }
    if (/^[a-zA-ZÀ-ÿ\u00f1\u00d1]+(\s*[a-zA-ZÀ-ÿ\u00f1\u00d1]*)*[a-zA-ZÀ-ÿ\u00f1\u00d1]+$/i.test(nombres)){
    }else{
        alert("El Nombre debe tener solo letras")
        sw=false
    }

    if (edad.length <1) {
        alert("Edad esta vacio")
        sw = false
    }else if (edad.length > 3 ) {
        alert("La edad debe tener como maximo 3 numeros")
        sw = false}

        if (/^\d+$/i.test(edad)){
        }else{
            alert("Edad debe tener solo numeros")
            sw=false
        }

    
    
    if (telefono.length < 1) {
        alert("El telefono esta vacio")
        sw = false
    }else if (telefono.length < 7 ) {
        alert("El telefono debe tener como minimo 7 numeros")
        sw = false
    } 
        if (/^\d+$/i.test(telefono)){
        }else{
            alert("El telefono debe tener solo numeros")
            sw=false
        }

    if (correo.length < 1) {
        alert("El Usuario esta vacio")
        sw = false
    } else {
        if (correo.includes("@")) {
            let separador = correo.split("@")
            let usuario = separador[0]
            if (usuario.length < 1) {
                alert("El correo no tiene el usuario")
                sw = false
            } else {
                let nombreDominio = separador[1]
                if (nombreDominio.includes(".")) {
                    separador = nombreDominio.split(".")
                    let dominio = separador[0]
                    let extension = separador[1]
                    if (dominio.length < 1) {
                        alert("El correo no tiene dominio")
                        sw = false
                    }

                    if (extension.length < 1) {
                        alert("El correo no tiene extension")
                        sw = false
                    }
                } else {
                    alert("El correo no tiene el .")
                    sw = false
                }
            }
        } else {
            alert("El correo no tiene el @")
            sw = false
        }
    }

    if (contrasena.length < 1) {
        alert("El campo contraseña esta vacio")
        sw = false
    } else if (contrasena.length < 8 ) {
        alert("La contraseña debe tener como minimo 8 caracteres")
        sw = false
    }


    return sw
}

function validar_registrovuelo() {
    let vuelo = document.getElementById("idvuelo").value
    let origen = document.getElementById("origen").value
    let destino = document.getElementById("destino").value
    let fecha = document.getElementById("fecha").value
    let hora = document.getElementById("hora").value
    let avion = document.getElementById("avion").value
    let costo = document.getElementById("costo").value
    let idpiloto =document.getElementById("idpilotovuelo").value
    let estado=document.getElementById("estado").value

    let sw = true

    if (vuelo.length <1) {
        alert("El vuelo esta vacio")
        sw = false
    }else if (vuelo.length < 3 ) {
        alert("El vuelo debe tener como minimo 3 numeros")
        sw = false}

        if (/^\d+$/i.test(vuelo)){
        }else{
            alert("El vuelo debe tener solo numeros")
            sw=false
        }

    if (idpiloto == "No seleccionado") {
        alert("Seleccione un Piloto")
        sw = false
    }

    if (origen.length <1) {
        alert("Origen esta vacio")
        sw = false
    }else if (origen.length < 3 ) {
        alert("Origen debe tener como minimo 3 letras")
        sw = false}

        if (/^[a-zA-ZÀ-ÿ\u00f1\u00d1]+(\s*[a-zA-ZÀ-ÿ\u00f1\u00d1]*)*[a-zA-ZÀ-ÿ\u00f1\u00d1]+$/i.test(origen)){
        }else{
            alert("Origen debe tener solo letras")
            sw=false
        }

    if (destino.length < 1) {
        alert("El destino esta vacio")
        sw = false
    } else if (destino.length < 3 ) {
        alert("El destino debe tener como minimo 3 caracteres")
        sw = false
    }
        if (/^[a-zA-ZÀ-ÿ\u00f1\u00d1]+(\s*[a-zA-ZÀ-ÿ\u00f1\u00d1]*)*[a-zA-ZÀ-ÿ\u00f1\u00d1]+$/i.test(destino)){
        }else{
            alert("El destino debe tener solo letras")
            sw=false
        }
    

    if (hora.length < 1) {
        alert("La hora esta vacio")
        sw = false
    }
        if (/^([0-9]{1,2}):([0-5][0-9])\s?([aApP][mM])?$/i.test(hora)){
        }else{
            alert("La hora debe tener solo numeros")
            sw=false
        }
    if (avion.length < 1) {
        alert("El campo avion esta vacio")
        sw = false
    } else if (avion.length < 4 ) {
        alert("Avion debe tener como minimo 4 caracteres")
        sw = false
    }

    if (costo.length <1) {
        alert("El costo esta vacio")
        sw = false
    }else if (costo.length < 5 ) {
        alert("El costo debe tener como minimo 5 numeros")
        sw = false}

        if (/^((\d+)|((\d{1,3}(,\d{3})*)))(\.\d+)?$/i.test(costo)){
        }else{
            alert("El costo debe tener solo numeros")
            sw=false
        }

    if(fecha == "dd/mm/aaaa"){
        alert("Ingrese una fecha")
        sw =false
    }
    

    if ( estado == "No seleccionado") {
        alert("Seleccione un Estado")
        sw = false
    }    
         
    return sw
}

function ConfirmDelete(){
    var respuesta = confirm("Esta seguro que desea Eliminar el registro?");
    if (respuesta ==true){
        return true
    }else{
        return false
    }
}

function ValidarAdminNew(){
    let correo = document.getElementById("emailactual").value
    let identificacion = document.getElementById("IdNuevo").value
    let correonuevo = document.getElementById("emailnuevo").value
    let contrasena = document.getElementById("newpassword").value
    

    let sw = true

    if (correo.length < 1) {
        alert("El Correo actual esta vacio")
        sw = false
    } else {
        if (correo.includes("@")) {
            let separador = correo.split("@")
            let usuario = separador[0]
            if (usuario.length < 1) {
                alert("El correo actual no tiene el usuario")
                sw = false
            } else {
                let nombreDominio = separador[1]
                if (nombreDominio.includes(".")) {
                    separador = nombreDominio.split(".")
                    let dominio = separador[0]
                    let extension = separador[1]
                    if (dominio.length < 1) {
                        alert("El correo actual no tiene dominio")
                        sw = false
                    }

                    if (extension.length < 1) {
                        alert("El correo  actual no tiene extension")
                        sw = false
                    }
                } else {
                    alert("El correo actual no tiene el .")
                    sw = false
                }
            }
        } else {
            alert("El correo actual no tiene el @")
            sw = false
        }
    }

    if (identificacion.length < 1) {
        alert("El documento esta vacio")
        sw = false
    }else if (identificacion.length < 7 ) {
        alert("El documento debe tener como minimo 7 números")
        sw = false}

        if (/^\d+$/i.test(identificacion)){
        }else{
            alert("El documento debe tener solo números")
            sw=false
        }

    if (correonuevo.length < 1) {
            alert("El Correo nuevo esta vacio")
            sw = false
        } else {
            if (correonuevo.includes("@")) {
                let separador = correonuevo.split("@")
                let usuario = separador[0]
                if (usuario.length < 1) {
                    alert("El correo nuevo no tiene el usuario")
                    sw = false
                } else {
                    let nombreDominio = separador[1]
                    if (nombreDominio.includes(".")) {
                        separador = nombreDominio.split(".")
                        let dominio = separador[0]
                        let extension = separador[1]
                        if (dominio.length < 1) {
                            alert("El correo nuevo no tiene dominio")
                            sw = false
                        }

                        if (extension.length < 1) {
                            alert("El correo nuevo no tiene extension")
                            sw = false
                        }
                    } else {
                        alert("El correo nuevo no tiene el .")
                        sw = false
                    }
                }
            } else {
                alert("El correo nuevo no tiene el @")
                sw = false
            }
        }

    if (contrasena.length < 1) {
        alert("La contraseña esta vacio")
        sw = false
    } else if (contrasena.length < 8 ) {
        alert("La contraseña debe tener como minimo 8 caracteres")
        sw = false
    }
}