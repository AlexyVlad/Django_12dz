from django.forms import forms

from core.models import Course
from django.forms import ModelForm

from django import forms


class CourseCreateForm(ModelForm):
    class Meta:
        model = Course
        fields = "__all__"

