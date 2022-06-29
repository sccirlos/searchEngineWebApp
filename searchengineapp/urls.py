
from django.urls import path
from . import views

# tells our app what view to load based on the URL.
urlpatterns = [

   
    path('',views.index,name='index'),
   # path('unzipRead', views.unzipRead),
    path('search',views.search,name='search'),
    path('docs', views.htmlfiles, name='doc_list'),
]