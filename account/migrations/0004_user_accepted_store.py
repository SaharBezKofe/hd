# Generated by Django 4.1.3 on 2022-12-03 01:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_history_options'),
        ('account', '0003_user_is_user_allow_to_dashboard'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='accepted_store',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.store', verbose_name='Выбранный магазин'),
        ),
    ]
