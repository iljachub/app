// Коли html документ готовий (промальований)
$(document).ready(function () {
    // Беремо із размітки элемент по id - сповіщення від django
    var notification = $('#notification');
    // І через 7 сек. прибираємо
    if (notification.length > 0) {
        setTimeout(function () {
            notification.alert('close');
        }, 7000);
    }

    // Коли клік по значку корини відкриваємо(модальне) вікно
    $('#modalButton').click(function () {
        $('#exampleModal').appendTo('body');

        $('#exampleModal').modal('show');
    });

    // Колі клік по кнопці закрити корзину
    $('#exampleModal .btn-close').click(function () {
        $('#exampleModal').modal('hide');
    });

    // Обробка події радіокнопки вибору доставки
    $("input[name='requires_delivery']").change(function() {
        var selectedValue = $(this).val();
        // Ховаємо або показуємо- вибір доставки
        if (selectedValue === "1") {
            $("#deliveryAddressField").show();
        } else {
            $("#deliveryAddressField").hide();
        }
    });

});