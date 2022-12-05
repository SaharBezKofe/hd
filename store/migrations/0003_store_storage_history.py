# Generated by Django 4.1.3 on 2022-12-02 15:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('good', '0003_alter_good_buy_amount'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('storage', '0001_initial'),
        ('store', '0002_alter_store_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='storage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='storage.storage', verbose_name='Склад'),
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата покупки')),
                ('good', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='good.good', verbose_name='Товар')),
                ('store', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.store', verbose_name='Магазин')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
    ]