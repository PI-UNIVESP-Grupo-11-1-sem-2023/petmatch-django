# Generated by Django 4.2.1 on 2023-05-28 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ongs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.TextField()),
                ('CPF', models.TextField()),
                ('Telefone', models.TextField()),
                ('Email', models.TextField()),
                ('Cep', models.TextField()),
                ('Rua', models.TextField()),
                ('Cidade', models.TextField()),
                ('Estado', models.TextField()),
            ],
        ),
    ]