# Generated by Django 4.1.6 on 2023-02-08 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0005_sportsmen_wins'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turnir',
            name='sportsmen',
        ),
        migrations.AddField(
            model_name='sportsmen',
            name='turnir',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='server.turnir'),
        ),
    ]
