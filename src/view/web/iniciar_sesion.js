function iniciarSesion(){
    const nombre = document.getElementById('nombre').value;
    const contrasena = document.getElementById('contrasena').value;

    fetch('http://127.0.0.1:8000/api/v1/iniciar_sesion',
        {
            method: 'POST',
            headers:{
                'Content-Type': "application/json"
            },
            body: JSON.stringify({
                nombre: nombre,
                contrasena: contrasena
            })
        })
        .then(response => response.status)
        .then(status =>{
            if (status === 200){
                alert("Inicio de sesión exitoso")
                window.location.href='menu_2.html';
            }else{
                alert("Nombre o contraseña incorrecta");
            }
            
        })
        .catch(error =>{
            console.error("Error en la petición: ", error);
        })
}

document.addEventListener("DOMContentLoaded", function(){
    const iniciarSesionBotton = document.getElementById('iniciar_sesion');
    iniciarSesionBotton.addEventListener('click', iniciarSesion);
});