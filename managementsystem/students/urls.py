from django.urls import path
from .views import StudentListView, StudentDetailView, StudentCreateView

urlpatterns = [
  #get
  path('',StudentListView.as_view(), name='student_list'),
#post
  path('create/', StudentCreateView.as_view(),name='student_create'),
#
path('<int:student_id>/', StudentDetailView.as_view(), name='student_detail')
]