const garbage = document.querySelector('.garbage select');
const type_text = document.getElementById('id_type_text');
const categoryDiv = document.querySelector('.category');
const tonalitiDiv = document.querySelector('.tonaliti');
const garbagevalue = garbage.value;
    const type_textvalue = type_text.value;
    if (garbagevalue == "True") {
        categoryDiv.style.display = "none";
        if (type_textvalue === "Пост") {
            tonalitiDiv.style.display = "none";
        }
    } else {
        categoryDiv.style.display = "block"; // Вернуть элемент
        tonalitiDiv.style.display = "block"; // Вернуть элемент
    }

function udateVisibleBlocks() {
    const garbagevalue = garbage.value;
    const type_textvalue = type_text.value;
    if (garbagevalue == "True") {
        categoryDiv.style.display = "none";
        if (type_textvalue === "Пост") {
            tonalitiDiv.style.display = "none";
        }
    } else {
        categoryDiv.style.display = "block"; // Вернуть элемент
        tonalitiDiv.style.display = "block"; // Вернуть элемент
    }
}
// Вызываем функцию при изменении значений полей ввода
garbage.addEventListener('change', udateVisibleBlocks)