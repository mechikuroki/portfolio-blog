from django.urls import path
from . import views

urlpatterns = [
    #path('home/', views.home, name='home'),
    path('', views.index, name='index'),
    path('blog/', views.product_list, name='product_list'),
    path('blog/<int:pk>/', views.product_detail, name='product_detail'),
    path('blog/search/', views.search, name='search'),
    #path('<int:pk>/edit/', views.edit_product, name='edit_product'),
    #path('<int:pk>/delete/', views.delete_product, name='delete_product'),
]
