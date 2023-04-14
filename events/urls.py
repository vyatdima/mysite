from django.urls import path

from events.views import events, peoples, procedures, PasswordCreate, LoadFromFile, ExportToFile, StripPeople

app_name = 'events'

urlpatterns = [
    path('', events, name='events'),
    path('<int:id_param>/', events, name='event'),
    path('peoples/', peoples, name='peoples'),
    path('peoples/<int:id_param>/', peoples, name='people'),
    path('procedures/', procedures, name='procedures'),
    path('password/', PasswordCreate, name='password'),
    path('load_from_file/', LoadFromFile, name='load_from_file'),
    path('export_to_file/', ExportToFile, name='export_to_file'),
    path('strip_people/', StripPeople, name='strip_people'),
]
