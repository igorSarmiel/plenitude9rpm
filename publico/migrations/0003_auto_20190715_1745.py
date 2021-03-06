# Generated by Django 2.2.3 on 2019-07-15 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publico', '0002_auto_20190708_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dependentes',
            name='observacoes',
            field=models.TextField(blank=True, max_length=1600, verbose_name='Observações:'),
        ),
        migrations.AlterField(
            model_name='dependentes',
            name='parentesco',
            field=models.CharField(choices=[('FILHO(A)', 'Filho(a)'), ('ENTEADO(A)', 'Enteado(a)'), ('CONJUGE', 'Conjuge'), ('OUTROS', 'Outros')], max_length=10, verbose_name='Relacionamento com titular:'),
        ),
        migrations.AlterField(
            model_name='publico',
            name='matricula',
            field=models.CharField(max_length=9, verbose_name='Nr policia/Bombeiro'),
        ),
        migrations.AlterField(
            model_name='publico',
            name='observacoes',
            field=models.TextField(blank=True, max_length=1600, verbose_name='Observações:'),
        ),
    ]
