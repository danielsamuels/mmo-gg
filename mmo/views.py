from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView


class ProtectedTemplateView(TemplateView):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProtectedTemplateView, self).dispatch(*args, **kwargs)


class ProtectedCreateView(CreateView):

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ProtectedCreateView, self).dispatch(request, *args, **kwargs)
