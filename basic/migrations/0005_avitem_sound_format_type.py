# Generated by Django 2.1 on 2018-12-17 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0004_avitem_base'),
    ]

    operations = [
        migrations.AddField(
            model_name='avitem',
            name='Sound_format_type',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]