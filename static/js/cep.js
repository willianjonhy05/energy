
var inputCEP = document.getElementById('id_cep');
inputCEP.addEventListener('input', function() {    
    var cep = this.value.replace(/\D/g, '');   
    if (cep.length === 8) {        
        cep = cep.substring(0, 5) + '-' + cep.substring(5);
    }
    this.value = cep;
});
