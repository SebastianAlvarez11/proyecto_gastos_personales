function cambiarContrasena(){
    const nuevaContrasena = document.getElementById('nueva_contrasena').value;

    fetch('http://127.0.0.1:8000/api/v1/cambiar_contrasena',
        {
            method: 'POST',
            headers:{
                'Content-Type': "application/json"
            },
            body: JSON.stringify({
                nueva_contrasena: nuevaContrasena
            })
        })
        .then(response => response.status)
        .then(status =>{
            if (status === 200){
                alert("Contraseña cambiada con exito");
            }else{
                alert("No se pudo cambiar la contraseña");
            }
            window.location.href = 'menu_2.html'
        })
        .catch(error =>{
            console.error("Error en la petición: ", error);
        })
}

document.addEventListener("DOMContentLoaded", function() {
    const cambiarContrasenaBotton = document.getElementById('cambiar_contrasena');
    cambiarContrasenaBotton.addEventListener('click', cambiarContrasena);
});
