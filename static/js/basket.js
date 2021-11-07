'use strict';

$(() => {
    $('.basket_list').on('change', '.basket_item input', ({ target }) => {
        const { name: id, value: qty } = target;

        $.ajax({
            url: `/baskets/edit/${id}/${qty}/`,
            success: ({ result }) => $('.basket_list').html(result),
        });
    });
});
