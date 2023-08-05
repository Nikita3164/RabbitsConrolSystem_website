$(document).ready(function() {
    // Получаем ссылку на кнопку по ее id
    let button = document.getElementById("get_test_data");

    // Назначаем обработчик события "click" для кнопки
    button.addEventListener("click", function() {
        // Отправляем AJAX-запрос на сервер Django
        $.ajax({
            url: "post_test_data",  // Замените на URL вашей Django-функции
            type: "GET",
            success: this.nonce
        });
    });
});

function updateTable() {
    $.ajax({
        url: '/get_rabbits_data/',
        type: 'GET',
        dataType: 'json',
        success: function(data) {
            // Обновляем содержимое строк таблицы
            let tableBody = document.querySelector('#rabbits-table tbody');
            tableBody.innerHTML = ''; // Очищаем содержимое строк
            for (let i = 0; i < data.length; i++) {
                let row = tableBody.insertRow(); // Вставляем новую строку в конец тела таблицы
                if (Math.abs(data[i].rabbit_temp_med - data[i].rabbit_temp) > 1.5 || Math.abs(data[i].rabbit_pulse_med - data[i].rabbit_pulse) > 20) {
                    row.classList.add("risk");
                }
                row.insertCell(0).innerHTML = data[i].rabbit_id;
                row.insertCell(1).innerHTML = data[i].rabbit_name;
                row.insertCell(2).innerHTML = data[i].rabbit_temp.toFixed(1);
                row.insertCell(3).innerHTML = data[i].rabbit_temp_med.toFixed(1);
                row.insertCell(4).innerHTML = data[i].rabbit_pulse.toFixed(1);
                row.insertCell(5).innerHTML = data[i].rabbit_pulse_med.toFixed(1);
            }
        }
    });
}

// Обновляем таблицу каждые 5 секунд
setInterval(updateTable, 5000);