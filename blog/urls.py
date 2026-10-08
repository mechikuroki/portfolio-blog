from django.urls import path
from . import views

urlpatterns = [
    #path('home/', views.home, name='home'),
    path('blog/', views.product_list, name='product_list'),
    path('blog/<int:pk>/', views.product_detail, name='product_detail'),
    path('blog/search/', views.search, name='search'),
    path('blog/<int:pk>/delete/', views.delete, name='delete'),
    path('blog/<int:pk>/deletecomment/', views.delete_comment, name='delete_comment'),
    path('blog/signup/', views.signup_view, name='signup'),
    path('blog/login/', views.login_view, name='login'),
    #path('<int:pk>/edit/', views.edit_product, name='edit_product'),
]
