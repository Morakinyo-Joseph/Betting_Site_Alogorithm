# Generated by Django 4.0.6 on 2022-08-08 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workbench', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='selected_game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workbench.game'),
        ),
    ]