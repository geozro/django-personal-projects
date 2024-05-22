# Generated by Django 5.0.4 on 2024-05-22 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LotofacilResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concurso', models.IntegerField(unique=True)),
                ('data_sorteio', models.DateField()),
                ('bola1', models.IntegerField()),
                ('bola2', models.IntegerField()),
                ('bola3', models.IntegerField()),
                ('bola4', models.IntegerField()),
                ('bola5', models.IntegerField()),
                ('bola6', models.IntegerField()),
                ('bola7', models.IntegerField()),
                ('bola8', models.IntegerField()),
                ('bola9', models.IntegerField()),
                ('bola10', models.IntegerField()),
                ('bola11', models.IntegerField()),
                ('bola12', models.IntegerField()),
                ('bola13', models.IntegerField()),
                ('bola14', models.IntegerField()),
                ('bola15', models.IntegerField()),
                ('ganhadores_15_acertos', models.IntegerField()),
                ('rateio_15_acertos', models.CharField(max_length=20)),
                ('ganhadores_14_acertos', models.IntegerField()),
                ('rateio_14_acertos', models.CharField(max_length=20)),
                ('ganhadores_13_acertos', models.IntegerField()),
                ('rateio_13_acertos', models.CharField(max_length=20)),
                ('ganhadores_12_acertos', models.IntegerField()),
                ('rateio_12_acertos', models.CharField(max_length=20)),
                ('ganhadores_11_acertos', models.IntegerField()),
                ('rateio_11_acertos', models.CharField(max_length=20)),
                ('acumulado_15_acertos', models.CharField(max_length=20)),
                ('arrecadacao_total', models.CharField(max_length=20)),
                ('estimativa_premio', models.CharField(max_length=20)),
                ('acumulado_especial_independencia', models.CharField(max_length=20)),
                ('observacao', models.TextField()),
            ],
        ),
    ]