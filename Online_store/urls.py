"""Online_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from products.views import main, product_view, product_detail_view, create_product_view
from Online_store.settings import MEDIA_ROOT, MEDIA_URL
from users.views import auth_view, logout_view, reg_view
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',main),
    path('products/', product_view),
    path('products/<int:id>/', product_detail_view),
    path('products/create/', create_product_view),

    #users
    path('users/auth/', auth_view),
    path('users/logout/', logout_view),
    path('users/register/', reg_view)
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
