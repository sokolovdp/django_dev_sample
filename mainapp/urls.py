from django.conf.urls import url
import mainapp.views

app_name = 'mainapp'

urlpatterns = [
    url(r'^register/', mainapp.views.register, name='register'),
    url(r'^login/', mainapp.views.user_login, name='user_login'),
    url(r'^logout/', mainapp.views.user_logout, name='user_logout'),
]
