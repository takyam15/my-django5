from django.contrib.auth import logout
from django.contrib.auth.models import AnonymousUser
#from django.contrib.sessions.middleware import SessionMiddleware
from django.test import RequestFactory
from django.urls import reverse

from ..views import (
    IndexView,
    UserLoginView, UserHomeView, UserLogoutView,
    ContactFormView, PrivacyPolicyView
)


class TestIndexView:

    def test_get(self, rf):
        request = rf.get(reverse('account:index'))
        response = IndexView.as_view()(request)
        assert response.status_code == 200
        assert 'account/index.html' in response.template_name


class TestUserLoginView:

    def test_get(self, rf):
        request = rf.get(reverse('account:login'))
        response = UserLoginView.as_view()(request)
        assert response.status_code == 200
        assert 'account/login.html' in response.template_name


class TestUserHomeView:

    def test_get(self, rf, user):
        request = rf.get(reverse('account:home'))
        request.user = user
        response = UserHomeView.as_view()(request)
        assert response.status_code == 200
        assert 'account/home.html' in response.template_name

    def test_get_by_anonymous_user(self, rf):
        request = rf.get(reverse('account:home'))
        request.user = AnonymousUser()
        response = UserHomeView.as_view()(request)
        url_home = reverse('account:home')
        url_login = reverse('account:login')
        assert response.status_code == 302
        assert response.url == f'{url_login}?next={url_home}'


class TestUserLogoutView:

    def test_post(self, user):
        rf = RequestFactory()
        request = rf.post(reverse('account:logout'))
        request.user = user
        response = logout(request)
        assert not request.user.is_authenticated
        assert response.status_code == 302
        assert response.url == reverse('account:login')

    """def test_get(self, user):
        rf = RequestFactory()
        request = rf.get(reverse('account:logout'))
        request.user = user
        middleware = SessionMiddleware(lambda request: None)
        middleware.process_request(request)
        request.session.save()
        response = UserLogoutView.as_view()(request)
        assert response.status_code == 405
        # assert response.url == reverse('account:login')"""


class TestContactFormView:

    def test_get(self, rf):
        request = rf.get(reverse('account:contact'))
        response = ContactFormView.as_view()(request)
        assert response.status_code == 200
        assert 'account/contact.html' in response.template_name


class TestPrivacyPolicyView:

    def test_get(self, rf):
        request = rf.get(reverse('account:privacy_policy'))
        response = PrivacyPolicyView.as_view()(request)
        assert response.status_code == 200
        assert 'account/privacy_policy.html' in response.template_name
