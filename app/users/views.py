from django.contrib.auth import login
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import CreationForm


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('selections:random_tile')
    template_name = 'users/signup.html'

    def form_valid(self, form):
        """
        Если форма валидна, сохраняет связанную модель.
        Осуществляет логирование пользователя после его создания.
        Возвращает пользователя на страницу с результатом запроса,
        если с нее пользователь перешел на страницу регистрации.
        """
        self.object = form.save()
        login(self.request, self.object)
        if self.request.path != self.request.get_full_path().split('=')[-1]:
            query_id = self.request.get_full_path().split('/')[-2]
            return redirect('selections:query', query_id)
        return redirect(self.get_success_url())
