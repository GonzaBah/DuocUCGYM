//Load
document.addEventListener("DOMContentLoaded", function(event) {
    // Todo lo que vaya aqui se ejecutará cuando cargue la página
    document.getElementById('sig').disabled = true;
});

let $input = document.getElementById('sub')
    $input.addEventListener('click', function () {
        var texto = document.getElementById('sub');
 
        texto.style.color="white";
        this.value = "Seleccionado";
        this.style.backgroundColor = "green";
        habilitarBoton()
    })



//Habilitador
function habilitarBoton(){
    'use strict';
    document.getElementById('sig').disabled = false;
}

function Enviar()
{
    window.location.href="{% url 'd_plan' %};"
}