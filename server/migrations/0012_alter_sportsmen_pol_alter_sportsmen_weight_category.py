# Generated by Django 4.1.6 on 2023-02-08 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0011_alter_sportsmen_weight_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sportsmen',
            name='pol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.pol'),
        ),
        migrations.AlterField(
            model_name='sportsmen',
            name='weight_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.weightcategory'),
        ),
    ]