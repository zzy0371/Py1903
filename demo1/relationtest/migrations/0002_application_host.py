# Generated by Django 2.2.2 on 2019-06-10 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relationtest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('h', models.ManyToManyField(to='relationtest.Host')),
            ],
        ),
    ]
