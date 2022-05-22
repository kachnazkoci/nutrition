from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import UserForm
from .models import User
from food.BMI_counter import bmi


class UserListView(ListView):
    model = User
    template_name = 'users.html'
    extra_context = {'page_name': 'Users'}


class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
    extra_context = {'page_name': User.name}

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        context.update({'page_name':self.object.name})
        context['bmi'] = bmi(self.object.weight, self.object.height)
        return context


class CreateUserView(CreateView):
    template_name = 'user_create.html'
    form_class = UserForm
    model = User
    extra_context = {'page_name': 'Add USER'}


class UpdateUserView(UpdateView):
    template_name = 'user_update.html'
    form_class = UserForm
    model = User
    extra_context = {'page_name': User}


class DeleteUserView(DeleteView):
    template_name = 'user_delete.html'
    model = User
    success_url = reverse_lazy('users')
    extra_context = {'page_name': User}

# def search_location(request):
#     context = {
#         'page_name': 'Search',
#     }
#     if request.method == "post":
#         searched = request.post['searched']
#         location = User.objects.filter(name__contains=searched)
#         return render(request,
#                       '/search/search_users.html',
#                       {'searched': searched,
#                        'location': location})
#     else:
#         return render(request,
#                       'search_users.html',
#                       {})
