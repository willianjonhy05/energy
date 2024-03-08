document.getElementById('id_cpf').addEventListener('input', function (event) {
    let value = event.target.value.replace(/\D/g, '');

    if (value.length === 11) {

        event.target.value = value.replace(/(\d{3})(\d{3})(\d{3})(\d{2})/, '$1.$2.$3-$4');
    } else if (value.length === 14) {

        event.target.value = value.replace(/(\d{2})(\d{3})(\d{3})(\d{4})(\d{2})/, '$1.$2.$3/$4-$5');
    }
});