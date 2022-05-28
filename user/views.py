from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import UserForm
from .models import User
from food.BMI_counter import bmi
from food.cal_counter_user import ideal_calories_intake, basal_metabolic_rate, activity_calorie_input


# def user_list_view(request):
#     users = User.objects.all()
#     context = {
#         'users': users
#     }
#     return render(request, 'users.html', context)


# def user_search_view(request):
#     context = {}
#     return render(request, 'search/search_user.html',
#                   context=context)


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
        context.update({'page_name': self.object.name})
        context['bmi'] = bmi(self.object.weight, self.object.height)
        context['basal_metabolic_rate'] = basal_metabolic_rate(self.object.gender, self.object.weight, self.object.height, self.object.age)
        context['activity_calorie_input'] = activity_calorie_input(context['basal_metabolic_rate'], self.object.activity)
        context['ideal_calories_intake'] = ideal_calories_intake(context['activity_calorie_input'], self.object.target)
        return context


# class BMIcounterView(TemplateView):
#     template_name = 'counter_BMI.html'
#     success_url = reverse_lazy('user')
#     # extra_context = {'page_name': User}


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
