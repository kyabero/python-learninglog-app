from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

# formでユーザーを作成するためのクラス
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2') # formで使用するための設定
