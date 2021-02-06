# Generated by Django 2.2 on 2021-02-02 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0005_auto_20210201_1618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartproduct',
            name='final_prize',
        ),
        migrations.AddField(
            model_name='cartproduct',
            name='final_price',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=9, verbose_name='Final Price'),
            preserve_default=False,
        ),
    ]