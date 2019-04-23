# Generated by Django 2.0.7 on 2019-04-09 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ativo', models.CharField(blank=True, choices=[('ON', 'ON'), ('OFF', 'OFF')], default='ON', max_length=4, null=True, verbose_name='Paciente Ativo ?')),
                ('nomeCompleto', models.CharField(blank=True, max_length=120, null=True, verbose_name='Nome Completo')),
                ('cpf', models.CharField(blank=True, max_length=20, null=True, verbose_name='CPF')),
                ('dataNascimento', models.CharField(blank=True, max_length=20, null=True, verbose_name='Data Nascimento')),
                ('idade', models.CharField(blank=True, max_length=3, null=True, verbose_name='Idade')),
                ('sexo', models.CharField(blank=True, choices=[('MASCULINO', 'MASCULINO'), ('FEMININO', 'FEMININO')], default='MASCULINO', max_length=10, null=True, verbose_name='Sexo')),
                ('estadoCivil', models.CharField(blank=True, choices=[('DIVORCIADO(A)', 'DIVORCIADO(A)'), ('VIUVO(A)', 'VIUVO(A)'), ('CASADO(A)', 'CASADO(A)'), ('SOLTEIRO(A)', 'VIUVO(A)')], default='SOLTEIRO(A)', max_length=25, null=True, verbose_name='Estado Civil')),
                ('profissao', models.TextField(blank=True, null=True, verbose_name='Profissões')),
                ('origem', models.TextField(blank=True, null=True, verbose_name='Origem')),
                ('observacao', models.TextField(blank=True, null=True, verbose_name='Observação')),
                ('email', models.CharField(blank=True, max_length=120, null=True, unique=True, verbose_name='Email')),
                ('telefone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefone')),
                ('celular', models.CharField(blank=True, max_length=20, null=True, verbose_name='Celular')),
                ('cep', models.CharField(blank=True, max_length=20, null=True, verbose_name='CEP')),
                ('numero', models.CharField(blank=True, max_length=240, null=True, verbose_name='Número')),
                ('rua', models.CharField(blank=True, max_length=240, null=True, verbose_name='Rua')),
                ('quadra', models.CharField(blank=True, max_length=240, null=True, verbose_name='Quadra')),
                ('bairro', models.CharField(blank=True, max_length=240, null=True, verbose_name='Bairro')),
                ('cidade', models.CharField(blank=True, max_length=240, null=True, verbose_name='Cidade')),
                ('estado', models.CharField(blank=True, max_length=240, null=True, verbose_name='Estado')),
                ('complemento', models.TextField(blank=True, null=True, verbose_name='Complemento')),
                ('grupoConvenio', models.TextField(blank=True, null=True, verbose_name='Convenios')),
                ('grupoFamiliar', models.TextField(blank=True, null=True, verbose_name='Familiares')),
                ('convenio1', models.CharField(blank=True, max_length=240, null=True, verbose_name='Convênio 1')),
                ('convenio2', models.CharField(blank=True, max_length=240, null=True, verbose_name='Convênio 2')),
                ('convenio3', models.CharField(blank=True, max_length=240, null=True, verbose_name='Convênio 3')),
                ('convenio4', models.CharField(blank=True, max_length=240, null=True, verbose_name='Convênio 4')),
                ('numeroCarteira1', models.CharField(blank=True, max_length=50, null=True, verbose_name='Número Carteira 1')),
                ('numeroCarteira2', models.CharField(blank=True, max_length=50, null=True, verbose_name='Número Carteira 2')),
                ('numeroCarteira3', models.CharField(blank=True, max_length=50, null=True, verbose_name='Número Carteira 3')),
                ('numeroCarteira4', models.CharField(blank=True, max_length=50, null=True, verbose_name='Número Carteira 4')),
                ('convenioValidade1', models.CharField(blank=True, max_length=20, null=True, verbose_name='Validade do Convênio 1')),
                ('convenioValidade2', models.CharField(blank=True, max_length=20, null=True, verbose_name='Validade do Convênio 2')),
                ('convenioValidade3', models.CharField(blank=True, max_length=20, null=True, verbose_name='Validade do Convênio 3')),
                ('convenioValidade4', models.CharField(blank=True, max_length=20, null=True, verbose_name='Validade do Convênio 4')),
                ('nomeFamiliar1', models.CharField(blank=True, max_length=120, null=True, verbose_name='Nome do Familiar 4')),
                ('nomeFamiliar2', models.CharField(blank=True, max_length=120, null=True, verbose_name='Nome do Familiar 4')),
                ('nomeFamiliar3', models.CharField(blank=True, max_length=120, null=True, verbose_name='Nome do Familiar 4')),
                ('nomeFamiliar4', models.CharField(blank=True, max_length=120, null=True, verbose_name='Nome do Familiar 4')),
                ('grau1', models.CharField(blank=True, max_length=20, null=True, verbose_name='Grau do Familiar 1')),
                ('grau2', models.CharField(blank=True, max_length=20, null=True, verbose_name='Grau do Familiar 2')),
                ('grau3', models.CharField(blank=True, max_length=20, null=True, verbose_name='Grau do Familiar 3')),
                ('grau4', models.CharField(blank=True, max_length=20, null=True, verbose_name='Grau do Familiar 4')),
                ('clinica', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Clinica')),
            ],
        ),
    ]
