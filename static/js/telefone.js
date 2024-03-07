document.getElementById('id_telefone').addEventListener('input', function (event) {
    let inputValue = event.target.value;
    inputValue = inputValue.replace(/\D/g, '');
    if (inputValue.length === 11) {
        inputValue = inputValue.replace(/^(\d{2})(\d{5})(\d{4})$/, '($1) $2-$3');
    } else {
        inputValue = inputValue.replace(/^(\d{2})(\d{4})(\d{4})$/, '($1) $2-$3');
    }

    event.target.value = inputValue;
});
