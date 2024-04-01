from django.urls import path
from .views import user_creation
from .views import stream_updates
urlpatterns = [
    path('create/', user_creation, name='create_user'),
    path('stream/', stream_updates, name='stream_updates'),

]
