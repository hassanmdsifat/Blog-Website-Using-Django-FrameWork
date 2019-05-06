from django.conf.urls import url
from first_app import views
app_name="first_app"

urlpatterns = [

    url(r'^aboutme/',views.about_me,name="aboutme"),
    url(r'^catagory/',views.catagory,name="catagory"),
    url(r'^seedetails/',views.details,name="details"),
    url(r'^get_comments/',views.get_comments,name="get_comments"),

    
]