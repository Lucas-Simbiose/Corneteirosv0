# Generated by Django 2.0.1 on 2018-01-13 00:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=100, null=True)),
                ('birth_date', models.DateTimeField(blank=True, null=True)),
                ('cpf', models.CharField(blank=True, max_length=11, null=True)),
                ('gender', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'MALE'), (2, 'FEMALE')], null=True)),
                ('sign_up_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('subscription', models.CharField(blank=True, max_length=10, null=True)),
                ('subscription_date', models.DateTimeField(blank=True, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=8, null=True)),
                ('street', models.CharField(blank=True, max_length=300, null=True)),
                ('number', models.CharField(blank=True, max_length=5, null=True)),
                ('complement', models.CharField(blank=True, max_length=300, null=True)),
                ('neighborhood', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=20, null=True)),
                ('pro', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TeamCrest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crest_type', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Grande'), (2, 'Pequeno'), (3, 'Médio')], null=True, verbose_name='Brasão')),
                ('stamp', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Grande'), (2, 'Pequeno'), (3, 'Médio')], null=True, verbose_name='Estampa')),
                ('adornment', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Grande'), (2, 'Pequeno'), (3, 'Médio')], null=True, verbose_name='Adorno')),
                ('collor1', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Verde'), (2, 'Vermelho'), (3, 'Azul'), (4, 'Amarelo'), (5, 'Preto')], null=True, verbose_name='Cor Brasão 1')),
                ('collor2', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Verde'), (2, 'Vermelho'), (3, 'Azul'), (4, 'Amarelo'), (5, 'Preto')], null=True, verbose_name='Cor Brasão 2')),
                ('collor3', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Verde'), (2, 'Vermelho'), (3, 'Azul'), (4, 'Amarelo'), (5, 'Preto')], null=True, verbose_name='Cor Brasão 3')),
            ],
        ),
        migrations.CreateModel(
            name='TeamData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nome do Time')),
                ('real_team', models.PositiveIntegerField(blank=True, choices=[(1, 'Corinthians'), (2, 'Vasco'), (3, 'Atletico_pr'), (4, 'Atletico_mg'), (5, 'Palmeiras')], null=True, verbose_name='Time do Coração')),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='teamcrest',
            name='teamdata',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.TeamData'),
        ),
    ]
