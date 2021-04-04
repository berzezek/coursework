from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserOurregistration, UserUpdateForm
from django.views.generic import (
    ListView,
    # DetailView,
    # CreateView,
    # UpdateView,
    # DeleteView
)
from .models import Profile


def register(request):
    if request.method == "POST":
        form = UserOurregistration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт {username} был создан, введите имя пользователя и пароль')
            return redirect('user')
    else:
        form = UserOurregistration()
    return render(request, 'users/registration.html', {'form': form, 'title': 'Регистрация пользователя'})


@login_required
def profile(request):
    if request.method == "POST":
        update_user = UserUpdateForm(request.POST, instance=request.user)
        # linkcut_user = UserUpdateForm(request.POST, instance=request.user.slug)

        if update_user.is_valid():
            update_user.save()
            # linkcut_user.save()

            messages.success(request, f'Ваш аккаунт был успешно обновлен')
            return redirect('user')
    else:
        update_user = UserUpdateForm(instance=request.user)
        # linkcut_user = UserUpdateForm(instance=request.user.slug)

    data = {
        'update_user': update_user,
        # 'linkcut_user': linkcut_user,
    }
    return render(request, 'users/profile.html', data)

def about(request):
    return render(request, 'linkcut/about.html')

# class CutLinkView(ListView):
#     model = Profile
#     template_name = 'users/user.html'
#     context_object_name = 'link'
#     # ordering = ['id']
#
#     def get_context_data(self, **kwards):
#         ctx = super(CutLinkView, self).get_context_data(**kwards)
#         ctx['title_name'] = 'Короткие ссылки'
#         return ctx