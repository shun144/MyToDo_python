from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model # ユーザーモデルを取得するため
# from django.contrib.auth.models import User
from .models import CustomUser



# ユーザーモデル取得
User = get_user_model()

class LoginForm(AuthenticationForm):
    """ログインフォーム"""

    # class Meta:
    #     model = CustomUser
        # fields = ['email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
    
        # for field in self.fields.values():
        #     print(field.label)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'your@email.com'
        self.fields['username'].label = 'メールアドレス'

        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
        self.fields['password'].label = 'パスワード'
        
        # self.fields['username'].widget.attrs['class'] = 'form-control'
        # self.fields['username'].widget.attrs['placeholder'] = 'your@email.com'
        # self.fields['username'].label = 'Email'

        # self.fields['password'].widget.attrs['class'] = 'form-control'
        # self.fields['password'].widget.attrs['placeholder'] = 'Password'
        # self.fields['password'].label = 'password'



class SignUpForm(UserCreationForm):
    """アカウント新規作成フォーム"""

    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label

        self.fields['email'].widget.attrs['placeholder'] = 'your@email.com'
        self.fields['email'].label = 'メールアドレス'
        # self.fields['email'].required = True

