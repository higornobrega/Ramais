# Generated by Django 3.2.7 on 2021-09-16 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endereco', '0001_initial'),
        ('polo', '0002_auto_20210916_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='polo',
            name='endereco',
            field=models.ManyToManyField(to='endereco.Endereco', verbose_name='Endereco'),
        ),
    ]
