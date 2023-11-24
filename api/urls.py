from django.urls import path

from .views import CostumerListView, CourseApiView

urlpatterns = [
    path('customers/', CostumerListView.as_view()),
    path('courses/', CourseApiView.as_view()),
]