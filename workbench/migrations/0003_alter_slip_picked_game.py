# Generated by Django 4.0.6 on 2022-08-07 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workbench', '0002_alter_slip_picked_game'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slip',
            name='picked_game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workbench.game'),
        ),
    ]
