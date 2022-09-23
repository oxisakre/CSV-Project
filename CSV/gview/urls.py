from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainView.as_view(template_name='templates/main.html'), name='main'),
    path('table', views.idListView.as_view(), name='Table'),
    path('alphabetical', views.Alphabetically.as_view(), name='alphabetical'),
    path('gender', views.GenderType.as_view(), name='gender'),
    path('results', views.UploadFile.as_view(), name='results'),
    path('older', views.Older.as_view(), name='older'),
    path('younger', views.Younger.as_view(), name='younger'),

]