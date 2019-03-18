# Generated by Django 2.1.7 on 2019-03-16 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('quantidade', models.IntegerField()),
                ('categoria', models.CharField(max_length=20)),
            ],
        ),
    ]
