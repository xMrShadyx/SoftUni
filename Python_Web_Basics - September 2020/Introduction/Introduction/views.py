from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import ListView


def index(request):
    title = 'Softuni Django 101'
    users = User.objects.all()
    context = {
        'title': title,
        'users': users,
    }
    return render(request, 'index.html', context)


class UserListView(ListView):
    model = User
    template_name = 'index2.html'
    queryset = User.objects.all().order_by('-username')

    def get_context_object_name(self, object_list):
        return 'users'

    def get_context_data(self, *, objects_list=None, **kwargs):
       context = super().get_context_data()
       context['title'] = 'From class View'
       return context