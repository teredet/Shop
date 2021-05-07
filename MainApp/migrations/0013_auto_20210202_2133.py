# Generated by Django 2.2 on 2021-02-02 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0012_auto_20210202_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(related_name='related_cart', to='MainApp.CartProduct'),
        ),
        migrations.AlterField(
            model_name='cartproduct',
            name='user',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='MainApp.Customer', verbose_name='Buyer'),
            preserve_default=False,
        ),
    ]
