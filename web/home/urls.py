from django.contrib import admin
from django.urls import path,include
from home import views
from django.conf import settings
from  django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('apply',views.kaizen,name='kaizen'),
    path('contactus',views.contact,name='contact'),
]
