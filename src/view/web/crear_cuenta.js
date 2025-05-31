function crearCuenta(){
    const nombre = document.getElementById('nombre').value;
    const tipoDocumento = document.getElementById('tipo_documento').value;
    const numeroDocumento = document.getElementById('numero_documento').value;
    const contrasena = document.getElementById('contrasena').value;
    const correo = document.getElementById('correo').value;
    const fechaNacimiento = document.getElementById('fecha_nacimiento').value;


    fetch('http://127.0.0.1:8000/api/v1/crear_cuenta',
        {
            method: 'POST',
            headers:{
                'Content-Type': "application/json"
            },
            body: JSON.stringify({
                nombre: nombre,
                tipo_documento: tipoDocumento,
                numero_documento: numeroDocumento,
                contrasena: contrasena,
                correo: correo,
                fecha_nacimiento: fechaNacimiento
            })
        })
        .then(response => response.status)
        .then(status =>{
            if (status === 200){
                alert("Cuenta creada con exito");
            }else{
                alert("No se pudo crear la cuenta");
            }
            window.location.href = 'index.html'
        })
        .catch(error =>{
            console.error("Error en la petición: ", error);
        })
}


document.addEventListener("DOMContentLoaded", function() {
    const crearCuentaBotton = document.getElementById('crear_cuenta');
    crearCuentaBotton.addEventListener('click', crearCuenta);
});