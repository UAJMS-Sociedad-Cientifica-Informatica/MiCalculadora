function boton(dato) {
    texto = document.getElementById("texto").value;
    document.getElementById("texto").value = texto + dato;
}


function borrar() {
    texto = document.getElementById("texto").value;
    texto = texto.substring(0, texto.length-1);
    document.getElementById("texto").value = texto;
}


function limpiar() {
    document.getElementById("texto").value = "";
}


function igual() {
    request = new XMLHttpRequest();
    calcular = document.getElementById("texto").value;
    calcular = calcular.replace("/","d");
    request.open("GET", "calcular/"+calcular, true);
    request.onreadystatechange = function () {
        if(this.readyState === 4 && this.status === 200){
            json = JSON.parse(this.responseText);
            document.getElementById("texto").value = json.resultado;
        }
    };
    request.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    request.send("holamundo");
}