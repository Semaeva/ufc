# Generated by Django 4.1.6 on 2023-02-09 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0014_shopcategory_alter_achieveevents_options_shopthing'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopthing',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
