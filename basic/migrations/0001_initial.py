# Generated by Django 2.1 on 2018-12-06 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AVItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(default=None, max_length=15, unique=True)),
                ('original_id', models.CharField(default='', max_length=15)),
                ('collection_id', models.CharField(default='', max_length=15)),
                ('item_title', models.CharField(default='', max_length=100)),
                ('series_title', models.CharField(default='', max_length=100)),
                ('episode_title', models.CharField(default='', max_length=100)),
                ('can_number', models.CharField(default='', max_length=100)),
                ('original_can_number', models.CharField(default='', max_length=100)),
                ('call_number', models.CharField(default='', max_length=100)),
                ('date_created', models.CharField(default='', max_length=100)),
                ('credits', models.CharField(default='', max_length=100)),
                ('description', models.CharField(default='', max_length=100)),
                ('location', models.CharField(default='', max_length=100)),
            ],
            options={
                'ordering': ('item_title', 'uid', 'original_id', 'collection_id'),
            },
        ),
    ]
