from django.urls import path
from mgmt_app.views import StudentListView, StudentDetailView, StudentCreateView, StudentUpdateView, StudentDeleteView, StudentCertView
urlpatterns = [
    path('list/', StudentListView.as_view(), name='student-list'),
    path('detail/<str:pk>/', StudentDetailView.as_view(), name='student-detail'),
    path('create/', StudentCreateView.as_view(), name='student-create'),
    path('update/<str:pk>/', StudentUpdateView.as_view(), name='student-update'),
    path('delete/<str:pk>/', StudentDeleteView.as_view(), name='student-delete'),
    path('cert/<str:pk>/', StudentCertView.as_view(), name='student-cert'),
]
