# Generated by Django 2.2.3 on 2019-07-15 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('ANDADOR', 'Andador'), ('MULETA', 'Muleta'), ('CADEIRA_RODAS', 'Cadeira de Rodas'), ('CADEIRA_BANHO', 'Cadeira de banho'), ('CAMA', 'Cama'), ('COLCHAO', 'Colchão'), ('TIPOIA', 'Tipoia'), ('COLAR_CERVICAL', 'Colar Cervical'), ('BOTA_ORTOPEDICA', 'Bota_ortopédica'), ('OUTROS', 'Outros')], max_length=30, verbose_name='Tipo do material:')),
                ('caracteristicas', models.CharField(max_length=60, verbose_name='Caracteristica do material:')),
                ('nr', models.CharField(blank=True, max_length=30, null=True, verbose_name='NR do material:')),
                ('observacoes', models.CharField(blank=True, max_length=60, null=True, verbose_name='Descrição do material:')),
            ],
        ),
    ]
