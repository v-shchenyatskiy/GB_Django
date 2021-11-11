'use strict';

$(() => {
    $('.btn').on('click', ({ target }) => {
        const { id } = target.dataset
        $.get(`/baskets/add/${id}/`).done(() => {
            $(target).html('&#10003; товар добавлен');
            setTimeout(()=> $(target).html('Отправить в корзину'), 1000);
        });
    });

    $('.basket_list').on('change', '.basket_item input', ({ target }) => {
        const { name: id, value: qty } = target;
        $.ajax({
            url: `/baskets/edit/${id}/${qty}/`,
            success: ({ result }) => $('.basket_list').html(result),
        });
    });
});
