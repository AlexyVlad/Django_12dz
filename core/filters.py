import django_filters as filters
from core.models import Course


class CourseFilter(filters.FilterSet):
    name = filters.CharFilter(label="Название курса", field_name='name', lookup_expr="icontains")

    class Meta:
        model = Course
        fields = ['name', ]
