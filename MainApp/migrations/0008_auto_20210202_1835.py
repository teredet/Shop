# Generated by Django 2.2 on 2021-02-02 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0007_auto_20210202_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MainApp.Customer', verbose_name='Owner'),
        ),
    ]
