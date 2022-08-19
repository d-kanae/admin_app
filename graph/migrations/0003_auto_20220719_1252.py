# Generated by Django 3.0.4 on 2022-07-19 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0002_auto_20220719_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='production',
            name='products_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='graph.Products', verbose_name='商品名'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='best_before_duration',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='賞味期間', to='graph.Products', verbose_name='賞味期間'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='customer_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='販売先', to='graph.Customer', verbose_name='販売先'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='production_date',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='製造日', to='graph.Production', verbose_name='製造日'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='products_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='商品名', to='graph.Products', verbose_name='商品名'),
        ),
    ]