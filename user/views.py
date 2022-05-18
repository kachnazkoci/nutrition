from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, FormView, CreateView, UpdateView, DeleteView
from .models import User


class UserListView(ListView):
    model = User
    template_name = 'users.html'
    extra_context = {'page_name': 'Users'}

    def user_list_view(request):
        users = User.objects.all()
        context = {
            'users': users
        }
        return render(request, 'user_list.html', context)

    def user_search_view(request):
        context = {}
        return render(request, 'nutrition/user/templates/search/search.html',
                      context=context)


class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
    extra_context = {'page_name': User}
    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        context.update({'page_name': self.object.name})
        return context



# def create_user_view(request):
#     if request.method == 'POST':
#         form = CreatePersonForm(request.POST)
#         persons = User.objects.all()
#         context = {
#             'persons': persons
#         }
#         if form.is_valid():
#             instance = form.save(commit=False)
#             instance.save()
#             return render(request, 'persons_list.html', context)
#     else:
#         form = CreatePersonForm()
#     context = {'form': form}
#     return render(request, 'create_person.html', context)

