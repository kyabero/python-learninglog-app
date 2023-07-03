from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import EntryModel
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied

def hello_world2(request):
    return HttpResponse('<h3>hello world2! from entryapp!!!</h3>')

# 「LoginRequiredMixin」はユーザーがログインしていなかったら処理を実行しない。
# 一覧を表示するページ
class ListEntryView(LoginRequiredMixin, ListView):
    template_name = 'entry/entry_model_list.html'
    model = EntryModel

# 各レコードの詳細を表示するページ
class DetailEntryView(LoginRequiredMixin, DetailView):
    template_name = 'entry/entry_detail.html'
    model = EntryModel

# 投稿フォームを作成する
class CreateEntryView(LoginRequiredMixin, CreateView):
    template_name = 'entry/entry_create.html'
    model = EntryModel
    fields = ['title', 'entry_text'] # ユーザーに入力させる項目
    success_url = reverse_lazy('list_entry')

    def form_valid(self, form): # フォームに入力したユーザー情報を元にテーブルに書き込み
        entry = form.save(commit=False)
        entry.user = self.request.user # 現在ログインしているユーザーを取り出す
        entry.save()
        return super().form_valid(form)

# ユーザーごとの投稿一覧ページを作成
class UserView(LoginRequiredMixin, ListView):
    template_name = 'entry/entry_model_list.html'
    paginate_by = 9

    def get_queryset(self):
        user_id = self.kwargs['user'] # ユーザー情報取得
        user_list = EntryModel.objects.filter(
            user=user_id # ユーザーIDと一致するもののみ取得
        )
        return user_list # 取得した情報を返す

# 投稿を修正するフォーム作成
class UpdateEntryView(LoginRequiredMixin, UpdateView):
    template_name = 'entry/entry_update.html'
    model = EntryModel
    fields = ['title', 'entry_text']
    success_url = reverse_lazy('list_entry')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset) # 編集しようとしているユーザーを取得

        if obj.user != self.request.user: # ログインユーザーと修正するユーザーが一致するか
            raise PermissionDenied # 合致していなかったらPermissionエラーを返す

        return obj # 合致していたらそのまま返す

# 投稿を削除するフォームを作成
class DeleteEntryView(LoginRequiredMixin, DeleteView):
    template_name = 'entry/entry_delete.html'
    model = EntryModel
    # fields = ['title', 'entry_text']
    success_url = reverse_lazy('list_entry')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user:
            raise PermissionDenied

        return obj