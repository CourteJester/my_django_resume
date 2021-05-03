from django.urls import path
from . import views
urlpatterns = [
	path('', views.home, name="home"),
	#path('about-me.html', views.about, name="about-me"),
	#path('home1.html', views.home1, name="home1"),

]
