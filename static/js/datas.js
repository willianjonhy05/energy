function mascaraData(data) {
    data = data.replace(/\D/g, '');
    if (data.length > 2) {
        data = data.replace(/^(\d{2})(\d)/g, '$1/$2');
        if (data.length > 5) {
            data = data.replace(/^(\d{2})\/(\d{2})(\d{1,4})$/, '$1/$2/$3');
        }
    }
    return data;
}


var campoData = document.getElementById('id_data_nasc');

campoData.addEventListener('input', function () {
    this.value = mascaraData(this.value);
});
