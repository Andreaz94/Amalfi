function validar_registro() {
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
        alert("El correo esta vacio")
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

