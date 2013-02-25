from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from mmo import settings


class HomepageView(TemplateView):
    template_name = 'site/homepage.html'


class LoginView(TemplateView):
    template_name = 'site/login.html'


class RegisterView(FormView):
    template_name = 'site/register.html'
    form_class = UserCreationForm
    success_url = settings.LOGIN_REDIRECT_URL

    def form_valid(self, form):
        form.save()

        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1']
        )
        if user is not None:
            if user.is_active:
                login(self.request, user)

        return super(RegisterView, self).form_valid(form)
