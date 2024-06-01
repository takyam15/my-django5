from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView, FormView

from .forms import UserLoginForm, ContactForm


class IndexView(TemplateView):

    template_name = 'account/index.html'


class UserLoginView(LoginView):

    form_class = UserLoginForm
    template_name = 'account/login.html'


class UserHomeView(LoginRequiredMixin, TemplateView):

    template_name = 'account/home.html'


class UserLogoutView(LogoutView):

    template_name = 'account/login.html'


class ContactFormView(FormView):

    form_class = ContactForm
    template_name = 'account/contact.html'
    success_url = 'account:contact'

    def form_valid(self, form):
        form.send_email()
        super().form_valid(form)


class PrivacyPolicyView(TemplateView):

    template_name = 'account/privacy_policy.html'
