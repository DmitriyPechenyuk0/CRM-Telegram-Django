from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
# Create your views here.

class RenderHome(TemplateView):
    template_name='home_app/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'home'
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated == True:

            if request.method.lower() in self.http_method_names:
                handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
            else:
                handler = self.http_method_not_allowed
            return handler(request, *args, **kwargs)
        else:
            return redirect("auth")