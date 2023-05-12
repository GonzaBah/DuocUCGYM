//Load
document.addEventListener("DOMContentLoaded", function(event) {
    // Todo lo que vaya aqui se ejecutará cuando cargue la página
    habilitarBoton(true)
});

let $input = document.getElementById('sub')
$input.addEventListener('click', function () {
    if(this.value == "Suscribirme"){
        // var texto = document.getElementById('sub');
        this.style.color="white";
        this.value = "Seleccionado";
        this.style.backgroundColor = "green";
        habilitarBoton(false)
    }else{
        // var texto = document.getElementById('sub');
        this.style.color="";
        this.value = "Suscribirme";
        this.style.backgroundColor = "";
        habilitarBoton(true)
    }
})

//Habilitador
function habilitarBoton(valor){
    'use strict';
    document.getElementById('sig').disabled = valor;
}


