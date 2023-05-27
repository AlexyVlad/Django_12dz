from django.urls import reverse_lazy
from core.forms import CourseCreateForm
from core.models import Course
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from core import models, filters


def index(request):
    count = Course.objects.count()

    return render(request, 'index.html', {"count": count})


def list_courses(request):
    сourses = models.Course.objects.all()
    return render(request, 'сourses.html', {"object_list": сourses})


def course(request, pk):
    сourse = models.Course.objects.get(id=pk)
    return render(request, 'сourse.html', {"object": сourse})


class CourseListView(ListView):
    model = Course
    template_name = "сourses.html"

    def get_filters(self):
        return filters.CourseFilter(self.request.GET)

    def get_queryset(self):
        return self.get_filters().qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.get_filters()
        return context


class CourseDetailView(DetailView):
    model = Course
    template_name = "сourse.html"


class CourseAddView(CreateView):
    model = Course
    template_name = 'add_course.html'
    context_object_name = 'add_course'
    form_class = CourseCreateForm
    success_url = reverse_lazy('courses')
    title = "add"


class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'delete_course.html'
    context_object_name = 'delete_course'
    success_url = reverse_lazy('courses')
    title = "Удаление книги"


class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'update_course.html'
    context_object_name = 'update_course'
    form_class = CourseCreateForm
    success_url = reverse_lazy('courses')
    title = "update_course"
