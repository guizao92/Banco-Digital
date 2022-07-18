# Generated by Django 4.0.6 on 2022-07-16 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11)),
                ('email', models.CharField(max_length=60)),
                ('telefone', models.CharField(max_length=14)),
                ('endereço', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id_conta', models.AutoField(primary_key=True, serialize=False)),
                ('saldo', models.FloatField(default=0.0)),
                ('cliente_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banco_digital.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Transferencia',
            fields=[
                ('id_transferencia', models.AutoField(primary_key=True, serialize=False)),
                ('valor_transferencia', models.FloatField()),
                ('data_transferencia', models.DateField(auto_now_add=True)),
                ('conta_entrada', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='conta_entrada', to='banco_digital.conta')),
                ('conta_saida', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='conta_saida', to='banco_digital.conta')),
            ],
        ),
    ]