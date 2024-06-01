import pytest
from django.urls import reverse, resolve, Resolver404

from ..views import (
    IndexView,
    UserLoginView, UserHomeView, UserLogoutView,
    ContactFormView, PrivacyPolicyView
)


def test_index():
    found = resolve(reverse('account:index'))
    assert found.func.view_class == IndexView


def test_login():
    found = resolve(reverse('account:login'))
    assert found.func.view_class == UserLoginView


def test_home():
    found = resolve(reverse('account:home'))
    assert found.func.view_class == UserHomeView


def test_logout():
    found = resolve(reverse('account:logout'))
    assert found.func.view_class == UserLogoutView


def test_contact():
    found = resolve(reverse('account:contact'))
    assert found.func.view_class == ContactFormView


def test_privacy_policy():
    found = resolve(reverse('account:privacy_policy'))
    assert found.func.view_class == PrivacyPolicyView


def test_not_exist():
    with pytest.raises(Resolver404):
        resolve('/not-exist/')
