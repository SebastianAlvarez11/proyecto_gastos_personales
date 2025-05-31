function realizarTransaccion(){
    const cantidadDinero = document.getElementById('cantidad_dinero').value;
    const categoria = document.getElementById('categoria').value;
    const fecha = document.getElementById('fecha').value;
    const hora = document.getElementById('hora').value;

    fetch('http://127.0.0.1:8000/api/v1/realizar_transaccion',
        {
            method: 'POST',
            headers:{
                'Content-Type': "application/json"
            },
            body: JSON.stringify({
                cantidad_dinero: cantidadDinero,
                categoria: categoria,
                fecha: fecha,
                hora: hora
            })
        })
        .then(response => response.status)
        .then(status =>{
            if (status === 200){
                alert("Transacción creada con exito");
            }else{
                alert("No se pudo crear la transacción");
            }
            window.location.href = 'menu_2.html'
        })
        .catch(error =>{
            console.error("Error en la petición: ", error);
        })
}

document.addEventListener("DOMContentLoaded", function() {
    const crearTransaccionBotton = document.getElementById('realizar_transaccion');
    crearTransaccionBotton.addEventListener('click', realizarTransaccion);
});