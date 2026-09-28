from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home_page'),

    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('cart/', views.cart_view, name='cart'),
    path('add/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:id>/', views.remove_item, name='remove'),

    path('checkout/', views.checkout, name='checkout'),

    # 🔥 ADD THIS LINE (MOST IMPORTANT)
    path('search/', views.search, name='search'),
]