from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import UserForm
from .models import User
from food.BMI_counter import bmi
from user.check import gender_check, calcul_age
from food.cal_counter_user import ideal_calories_intake, basal_metabolic_rate, activity_calorie_input
from food.nutrients_ratio import protein_calculation, carbs_calculation, fats_calculation


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
        context['age'] = calcul_age(self.object.birth_date)
        context['gender'] = gender_check(self.object.title)
        context['basal_metabolic_rate'] = basal_metabolic_rate(self.object.gender, self.object.weight,
                                                               self.object.height, context['age'])
        context['activity_calorie_input'] = activity_calorie_input(context['basal_metabolic_rate'],
                                                                   self.object.activity)
        context['ideal_calories_intake'] = ideal_calories_intake(context['activity_calorie_input'], self.object.target)
        context['protein_calculation'] = protein_calculation(context['ideal_calories_intake'], self.object.target)
        context['carbs_calculation'] = carbs_calculation(context['ideal_calories_intake'], self.object.target)
        context['fats_calculation'] = fats_calculation(context['ideal_calories_intake'], self.object.target)
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
