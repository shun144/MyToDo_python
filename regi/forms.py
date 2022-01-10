from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model # ユーザーモデルを取得するため

# ユーザーモデル取得
User = get_user_model()

class LoginForm(AuthenticationForm):
    """ログインフォーム"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'your@email.com'
        self.fields['username'].label = 'Email'

        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
        self.fields['password'].label = 'password'


        # for field in self.fields.values():
        #     field.widget.attrs['class'] = 'form-control'
        #     field.widget.attrs['placeholder'] = field.label
        #     field.help_text = 'test'
