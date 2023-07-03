from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy

# Create your views here.
# ユーザー登録ページの作成
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "signup.html"
    success_url = reverse_lazy('addounts:signup_success')

    def form_valid(self, form): # userが登録ボタンを押下時の処理
        user = form.save()
        self.object = user
        return super().form_valid(form)

# ユーザー登録完了ページの作成
class SignUpSuccessView(TemplateView):
    template_name = "signup_success.html"
