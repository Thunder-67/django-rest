# Generated by Django 3.2.9 on 2021-11-03 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='meals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strmeal', models.CharField(max_length=100)),
                ('strmealthumb', models.URLField(max_length=100)),
                ('idmeal', models.IntegerField()),
            ],
        ),
    ]
