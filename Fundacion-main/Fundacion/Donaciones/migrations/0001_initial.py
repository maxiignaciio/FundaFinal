# Generated by Django 4.0.2 on 2022-06-29 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('nombre', models.TextField(max_length=20)),
                ('apellido_pat', models.TextField(max_length=50)),
                ('apellido_mat', models.TextField(max_length=50)),
                ('monto', models.IntegerField()),
            ],
        ),
    ]
