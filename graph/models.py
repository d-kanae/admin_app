from django.db import models
from register.models import *

# 顧客クラス
class Customer(models.Model):
    customer_name = models.CharField("顧客名", max_length=100)
    customer_app_date = models.DateField("登録日", auto_now_add=True)
    
    class Meta:
        verbose_name = "顧客"
        verbose_name_plural = "顧客"
    
    def __str__(self):
        return self.customer_name

# 商品クラス
class Products(models.Model):
    products_name = models.CharField("商品名",max_length=50)
    best_before_duration = models.IntegerField("賞味期間(日)")
    product_app_date = models.DateField("登録日", auto_now_add=True)

    class Meta:
        verbose_name = "商品"
        verbose_name_plural = "商品"
        
    def __str__(self):
        return self.products_name
        

# 製造クラス
class Production(models.Model):
    products_name = models.ForeignKey(Products, on_delete=models.DO_NOTHING, verbose_name = "商品名")
    production_date = models.DateField("製造日")
    production_volume = models.IntegerField("製造量(CS)")
    
    class Meta:
        verbose_name = "製造履歴"
        verbose_name_plural = "製造履歴"
    
    def __str__(self):
        return f"{self.products_name}:{self.production_date}"
    

# 販売クラス
class Sale(models.Model):
    products_name = models.ForeignKey(Products, on_delete=models.DO_NOTHING, verbose_name = "商品名", related_name= "商品名")
    production_date = models.ForeignKey(Production, on_delete=models.DO_NOTHING, verbose_name = "製造日", related_name="製造日")
    best_before_duration = models.ForeignKey(Products, on_delete=models.DO_NOTHING, verbose_name = "賞味期間", related_name="賞味期間")
    customer_name = models.OneToOneField(Customer, on_delete=models.DO_NOTHING, verbose_name = "販売先", related_name="販売先")
    sale_date = models.DateField("販売日")
    sale_volume = models.IntegerField("販売量(CS)")
    sale_price = models.IntegerField("販売額(円/CS)")

    class Meta:
        verbose_name = "販売履歴"
        verbose_name_plural = "販売履歴"
        ordering = ("-sale_date",)
