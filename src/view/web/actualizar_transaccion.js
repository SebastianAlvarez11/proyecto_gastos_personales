function actualizarTransaccion() {
    const id = document.getElementById('transaccion_id').value;
    const campo = document.getElementById('campo').value;
    const nuevoValor = document.getElementById('nuevo_valor').value;

        fetch('http://127.0.0.1:8000/api/v1/actualizar_transaccion',
        {
            method: 'POST',
            headers:{
                'Content-Type': "application/json"
            },
            body: JSON.stringify({
                id: id,
                campo: campo,
                nuevo_valor: nuevoValor
            })
        })
        .then(response => response.status)
        .then(status =>{
            if (status === 200){
                alert("Actualización con exito");
            }else{
                alert("No se pudo actualizar la transacción");
            }
            window.location.href = 'menu_2.html'
        })
        .catch(error =>{
            console.error("Error en la petición: ", error);
        })
}

document.addEventListener("DOMContentLoaded", function() {
    const actualizarTransaccionBotton = document.getElementById('actualizar_transaccion');
    actualizarTransaccionBotton.addEventListener('click', actualizarTransaccion);
});
