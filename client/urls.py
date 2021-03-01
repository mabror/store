from django.urls import path
from  .  import views


urlpatterns = [
    path('', views.page, name='page'),
    path('store/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_check, name='login'),
    path('logout/', views.logout_check, name='logout'),
    path('current_product/<int:product_id>', views.current_product, name='current_product'),
    path('current_product_ex/<int:product_id>', views.current_product_ex, name='current_product_ex'),
    path('income_create/', views.income_create, name='income_create'),
    path('expence_create/', views.expence_create, name='expence_create'),
    path('create/', views.post_create, name='create'),
]