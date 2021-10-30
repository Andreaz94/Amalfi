function validar_formulario() {
    let correo= document.getElementById("email").value
    let pass = document.getElementById("passw").value
    let Rol = document.getElementById("Rol").value

    let sw = true

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

    if (pass.length < 1) {
        alert("El campo contraseña esta vacio")
        sw = false
    } else if (pass.length < 8 ) {
        alert("La contraseña debe tener como minimo 8 caracteres")
        sw = false
    }
    if (Rol == "Seleccione un Rol") {
        alert("Seleccione un rol")
        sw = false
    }
    return sw
}