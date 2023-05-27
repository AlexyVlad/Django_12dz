from django.urls import path, include
from . import views
from .views import CourseDetailView, CourseListView, CourseUpdateView, CourseAddView, CourseDeleteView

urlpatterns = [
    path('', views.index),
    path('courses_f', views.list_courses, name='courses'),
    path('courses', CourseListView.as_view(), name='courses'),
    path('course_f/<int:pk>', views.course, name="course"),
    path('course/<int:pk>', CourseDetailView.as_view(), name="course"),

    path('course/add_course/', CourseAddView.as_view(), name="add_course"),
    path('course/delete_course/<int:pk>/', CourseDeleteView.as_view(), name="delete_course"),
    path('course/update/<int:pk>', CourseUpdateView.as_view(), name="update"),
]