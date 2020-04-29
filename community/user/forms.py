from django import forms
from django.contrib.auth.hashers import make_password, check_password
from .models import user
class LoginForm(forms.Form):
    username=forms.CharField(
        error_messages={
            'required': '아이디를 입력하세요.'},max_length=32,label='사용자 이름')
    password=forms.CharField(
        error_messages={
            'required': '비밀번호를 입력하세요.'},widget=forms.PasswordInput,label='비밀번호')

    def clean(self):
        cleaned_data=super().clean()
        username=cleaned_data.get('username')
        password=cleaned_data.get('password')

        if username and password:
            User=user.objects.get(username=username)
            if not check_password(password, User.password):
                self.add_error('password','비밀번호를 틀렸습니다')
            else:
                self.user_id=User.id
