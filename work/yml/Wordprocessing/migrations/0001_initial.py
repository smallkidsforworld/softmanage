# Generated by Django 3.0.6 on 2020-05-10 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SelfIndo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('occupation', models.CharField(max_length=50)),
                ('salary', models.IntegerField()),
            ],
        ),
    ]
