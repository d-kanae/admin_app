from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import *

# 一覧
class IndexView(ListView):
    # 一覧するモデルを指定 -> `object_list`で取得可能
    model = Products

# 個別
class Detail(DetailView):
    # 詳細表示するモデルを指定 -> `object`で取得可能
    model = Sale
    

