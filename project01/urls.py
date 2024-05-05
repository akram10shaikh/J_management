"""project01 URL Configuration

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
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('base/',views.base,name='base'),
    path('second/',views.second,name='second'),
    path('add/',views.add,name='add'),
    path('login_page/',views.login_page,name='login_page'),
    path('log1/',views.log1,name='log1'),
    path('log_out/',views.log_out,name='log_out'),
    path('add_data/',views.add_data,name='add_data'),
    path('employee/',views.employee,name='employee'),
    path('display/',views.display,name='display'),
    path('add_user/',views.add_user,name='add_user'),       
    path('display_one/',views.display_one,name='display_one'),
    path('edit/',views.edit,name='edit'),
    path('edit_record/<int:id>/', views.edit_record, name='edit_record'),
    path('edit_apply/',views.edit_apply,name='edit_apply'),
    path('search/',views.search,name='search'),
    path('search_data/',views.search_data,name='search_data'),
    path('search_page/',views.search_page,name='search_page'),
    # path('delete_record/<int:id>/', views.delete_record, name='delete_record'),
    path('delete/<int:id>/', views.delete_record, name='delete_record'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
