// Получаем элементы по их id
const inputElementPass1 = document.getElementById('id_password1');
const inputElementPass2 = document.getElementById('id_password2');
const btn = document.querySelector('.login_btn');
btn.disabled = true;
btn.style.opacity = 0.5;
btn.style.pointerEvents = 'none';

function updateButtonState() {
    const pass1Value = inputElementPass1.value;
    const pass2Value = inputElementPass2.value;
    const lenpass = pass1Value.length;
    if (pass1Value && pass2Value && lenpass > 7 && pass1Value === pass2Value) {
        // Делаем кнопку активной
        btn.disabled = false;
        btn.style.opacity = 1;
        btn.style.pointerEvents = 'auto';
    } else {
        // Делаем кнопку полупрозрачной и неактивной к нажатию
        btn.disabled = true;
        btn.style.opacity = 0.5;
        btn.style.pointerEvents = 'none';
    }
}

// Вызываем функцию при изменении значений полей ввода
inputElementPass1.addEventListener('input', updateButtonState);
inputElementPass2.addEventListener('input', updateButtonState);

// Получаем элемент по его id
const inputElementUsername = document.getElementById('id_username');

inputElementUsername.addEventListener('input', function() {
    // Приводим значение к нижнему регистру и устанавливаем его обратно в поле
    inputElementUsername.value = inputElementUsername.value.toLowerCase().replace(/\s/g, '');
});

// Получаем элемент по его id
const inputElementGroupNumber = document.getElementById('id_group_number');

inputElementGroupNumber.addEventListener('input', function() {
    // Оставляем только цифры
    inputElementGroupNumber.value = inputElementGroupNumber.value.replace(/\D/g, '');
});
