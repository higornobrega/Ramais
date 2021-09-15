# Generated by Django 3.2.7 on 2021-09-15 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('polo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Colaborador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(max_length=50, verbose_name='Matricula')),
                ('tipo', models.IntegerField(choices=[(1, 'Professor(a)'), (2, 'Gerente'), (3, 'Secretaria(o)')], verbose_name='Tipo')),
                ('nomeColaborador', models.CharField(max_length=254, verbose_name='Nome')),
                ('emailInstitucional', models.EmailField(max_length=254, verbose_name='Email Intitucional')),
                ('numero', models.CharField(max_length=21, verbose_name='Nome')),
                ('numeroWhatsapp', models.CharField(blank=True, max_length=21, null=True, verbose_name='Nome')),
                ('sexo', models.IntegerField(choices=[(1, 'Masculino'), (2, 'Feminino'), (3, 'Outro')], verbose_name='Sexo')),
                ('instagram', models.CharField(max_length=254, verbose_name='Instagram')),
                ('linkedin', models.CharField(max_length=254, verbose_name='Linkedin')),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='foto/%d/%m/%y/', verbose_name='Imagem')),
                ('natVinc', models.IntegerField(choices=[(1, 'Naturalidade vinculo 1'), (2, 'Naturalidade vinculo 2'), (3, 'Naturalidade vinculo 3')], verbose_name='Sexo')),
                ('cargaHoraria', models.IntegerField(verbose_name='CH')),
                ('polo', models.ManyToManyField(to='polo.Polo')),
            ],
        ),
    ]