//Load
document.addEventListener("DOMContentLoaded", function(event) {
    // Todo lo que vaya aqui se ejecutará cuando cargue la página
    habilitarBoton(true)
});

function seleccionar(id){
    console.log(id);
    document.getElementsByName("subs").disabled = true;
    let input = document.getElementById(id);
    if (input.value == "Suscribirme"){
        input.style.color="white";
        input.value = "Seleccionado";
        input.style.backgroundColor = "green";
        habilitarBoton(false)
    } else {
        input.style.color="";
        input.value = "Suscribirme";
        input.style.backgroundColor = "";
        habilitarBoton(true)
    }

}

//Habilitador
function habilitarBoton(valor){
    'use strict';
    document.getElementById('sig').disabled = valor;
}


