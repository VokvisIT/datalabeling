const garbageSelect = document.querySelector('.garbage select');
const categoryDiv = document.querySelector('.category');
const tonalitiDiv = document.querySelector('.tonaliti');

garbageSelect.addEventListener("change", function() {
    const selectedValue = garbageSelect.value;
    console.log("Выбрано: " + selectedValue);
    if (selectedValue == "True") {
        categoryDiv.style.display = "none"; // Убрать элемент
        // tonalitiDiv.style.display = "none"; // Убрать элемент
      } else {
        categoryDiv.style.display = "block"; // Вернуть элемент
        // tonalitiDiv.style.display = "block"; // Вернуть элемент
      }
  });
