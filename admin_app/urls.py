"""admin_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.contrib.auth.models import User,Group
from django.urls import path, include

import graph

admin.site.site_title = "マイページ"
admin.site.site_header = "管理ツール"
admin.site.index_title = "HOME"
admin.site.site_url = None
admin.site.unregister(Group)     # 非表示設定



urlpatterns = [
    path('staff-admin/', admin.site.urls),
    path("graph/", include("graph.urls")),
]
