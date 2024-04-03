from django.urls import path
from .views import index, customer_detail
urlpatterns = [
    path("", index , name="index"),
    path("<int:customer_id>",customer_detail, name="customer_detail" )
]