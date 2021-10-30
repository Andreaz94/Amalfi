function validar_usuario() {
    let textocodigo = document.getElementById("textocodigo").value
    let sw = true

    if (textocodigo.length <1) {
        alert("El codigo esta vacio")
        sw = false
    }else if (textocodigo.length < 3 ) {
        alert("El Codigo debe tener como minimo 3 numeros")
        sw = false}

        if (/^\d+$/i.test(textocodigo)){
        }else{
            alert("El codigo debe tener solo numeros")
            sw=false
        }
    return sw
        
}

