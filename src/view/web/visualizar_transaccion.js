function visualizarTransaccion(){
    const fechaInicial = document.getElementById('fecha_inicial').value;
    const fechaFinal = document.getElementById('fecha_final').value;

    fetch('http://127.0.0.1:8000/api/v1/visualizar_transaccion',
        {
            method: 'POST',
            headers:{
                'Content-Type': "application/json"
            },
            body: JSON.stringify({
                fecha_inicial: fechaInicial,
                fecha_final: fechaFinal
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
    const visualizarTransaccionBotton = document.getElementById('visualizar_transaccion');
    visualizarTransaccionBotton.addEventListener('click', visualizarTransaccion);
});