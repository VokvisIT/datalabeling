// Получаем элемент по его id
const inputElementUsername = document.getElementById('id_username');

inputElementUsername.addEventListener('input', function() {
    // Приводим значение к нижнему регистру и устанавливаем его обратно в поле
    inputElementUsername.value = inputElementUsername.value.toLowerCase().replace(/\s/g, '');
});