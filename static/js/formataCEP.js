function formatarCEP(cep) {
    if (cep.length === 8) {
        return cep.substring(0, 5) + '-' + cep.substring(5);
    } else {
        return cep;
    }
}


var cepElement = document.getElementById('cep');
var cep = cepValue;
var cepFormatado = formatarCEP(cep);
cepElement.textContent = cepFormatado;
