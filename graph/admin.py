from django import forms
from django.contrib import admin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.admin import AdminSite
from django.db import models
from register.models import *
from .models import *


# class SaleForm(forms.ModelForm):

#     extra_field = forms.CharField()

#     def save(self, commit=True):
#         extra_fields = self.cleaned_data.get('extra_field', None)
#         # ...do something with extra_field here...
#         return super(SaleForm, self).save(commit=commit)

#     class Meta:
#         model = Sale

# class GraphAdmin(admin.ModelAdmin):
#     list_display = ("products_name", "products_date", )
    
# admin.site.register(Sale, GraphAdmin)
# admin.site.app_index = ()
