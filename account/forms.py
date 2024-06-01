from django import forms
from django.conf import settings
from django.core.mail import BadHeaderError, EmailMessage
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse


class UserLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label
            field.label = ''


class ContactForm(forms.Form):

    name = forms.CharField(
        label='',
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'お名前'
        })
    )
    email = forms.EmailField(
        label='',
        max_length=254,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'メールアドレス'
        })
    )
    title = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '件名'
        })
    )
    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': '本文'
        })
    )
    # captha = ReCaptchaField(widget=ReCaptchaWidget())

    def send_email(self):
        subject = 'お問い合わせ：' + self.cleaned_data['title']
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        from_email = f'{name} <{email}>'
        message = self.cleaned_data['body']
        recipient_list = [settings.EMAIL_HOST_USER]
        email_message = EmailMessage(
            subject, message, from_email, recipient_list, reply_to=[email]
        )
        try:
            email_message.send()
        except BadHeaderError:
            return HttpResponse('無効なヘッダが検出されました。')
