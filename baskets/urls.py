from django.urls import path

from baskets.views import basket_add, basket_edit, basket_remove

app_name = 'baskets'

urlpatterns = [
    path('add/<int:product_id>/', basket_add, name='basket_add'),
    path('edit/<int:id>/<int:quantity>/', basket_edit, name='basket_edit'),
    path('remove/<int:id>/', basket_remove, name='basket_remove'),
]
