from ..forms import UserLoginForm, ContactForm


class TestUserLoginForm:

    def test_has_fields(self):
        assert set(UserLoginForm().fields) == {'username', 'password'}


class TestContactForm:

    def test_has_fields(self):
        assert set(ContactForm().fields) == {'name', 'email', 'title', 'body'}
