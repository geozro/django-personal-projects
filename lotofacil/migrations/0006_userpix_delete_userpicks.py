# Generated by Django 5.0.4 on 2024-05-31 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotofacil', '0005_remove_userpicks_id_alter_userpicks_pick_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPix',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bet_number', models.IntegerField()),
                ('concurso', models.IntegerField()),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='UserPicks',
        ),
    ]
