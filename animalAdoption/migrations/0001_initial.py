# Generated by Django 4.2.1 on 2023-06-05 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('statut_vaccinal', models.BooleanField(default=False)),
                ('sterilisation', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='chien',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('statut_vaccinal', models.BooleanField(default=False)),
                ('sterilisation', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='oiseau',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('statut_vaccinal', models.BooleanField(default=False)),
                ('sterilisation', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
