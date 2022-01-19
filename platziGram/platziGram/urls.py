
from django.contrib import admin
from django.urls import path
from platziGram import views as local_views
from posts import views as post_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-world/', local_views.hello_world),
    path('sorted/', local_views.sorted_func),
    path('hi/<str:name>/<int:age>/', local_views.say_hi),
    path('posts/', post_views.list_post),
]
