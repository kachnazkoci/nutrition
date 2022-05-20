from django.shortcuts import render, resolve_url
from django.db import models
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import FoodForm
from .models import Food


# def food_list_view(request):
#     users = Food.objects.all()
#     context = {
#         'users': users
#     }
#     return render(request, 'food.html', context)


# def user_search_view(request):
#     context = {}
#     return render(request, 'search/search_user.html',
#                   context=context)


class FoodListView(ListView):
    model = Food
    template_name = 'food.html'
    extra_context = {'page_name': 'Food'}


class FoodDetailView(DetailView):
    model = Food
    template_name = 'food_detail.html'
    extra_context = {'page_name': Food.name}

    def get_context_data(self, **kwargs):
        context = super(FoodDetailView, self).get_context_data(**kwargs)
        context.update({'page_name': self.object.name})
        return context


class CreateFoodView(CreateView):
    template_name = 'food_create.html'
    form_class = FoodForm
    model = Food
    extra_context = {'page_name': 'Add FOOD'}


class UpdateFoodView(UpdateView):
    template_name = 'food_update.html'
    form_class = FoodForm
    model = Food
    extra_context = {'page_name': Food}


class DeleteFoodView(DeleteView):
    template_name = 'food_delete.html'
    model = Food
    success_url = reverse_lazy('food')
    extra_context = {'page_name': Food}