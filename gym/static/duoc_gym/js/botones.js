
//Planes
function selSub() {
    let $input = document.getElementById('sub')
    $input.addEventListener('click', function () {
        var texto = document.getElementById('sub');
        texto.style.color="white";
        this.value = "Seleccionado";
        this.style.backgroundColor = "green";
     
    })
}

//Habilitador
function habilitarBoton(){
    document.getElementById('sub').addEventListener('input', function(event) {
        document.getElementById('sig').disabled = !this.value;
    }, false);
}
