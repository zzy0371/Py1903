# Generated by Django 2.2.2 on 2019-06-10 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('relationtest', '0005_temp_age'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='temp',
            options={'ordering': ['title', '-addr', 'age'], 'verbose_name': '临时表'},
        ),
    ]
