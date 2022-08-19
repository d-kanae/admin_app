from pyexpat import model
import re
from statistics import mode
from turtle import color
from urllib import response
from django.shortcuts import render

from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from . import models, graph
from .models import Products, Customer, Production, Sale

import base64
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import io


class Index(TemplateView):
    
    # テンプレートファイル連携
    template_name = "graph/Index.html"
    
    # 変数としてグラフイメージをテンプレートに渡す
    def get_context_data(self, **kwargs):
        
        # グラフオブジェクト
        qs = models.Sale.objects.all()      # モデルクラス(Saleテーブル)読込
        x = [x.sale_date for x in qs]       # x軸データ
        y = [y.sale_volume for y in qs]     # y軸データ
        chart = graph.plot_Graph(x,y)       # グラフ作成
        
        # 変数を渡す
        context = super().get_context_data(**kwargs)
        context["chart"] = chart
        return context
    
    # GET処理
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

