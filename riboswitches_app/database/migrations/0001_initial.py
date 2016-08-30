# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-30 11:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('pmid', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Gene',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=20, verbose_name='nazwa')),
                ('accession_number', models.CharField(default='Undefined', max_length=15, verbose_name='numer_dostepu')),
                ('start_pos', models.IntegerField(default=0)),
                ('end_pos', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Ligand',
            fields=[
                ('name', models.CharField(default=None, max_length=20, primary_key=True, serialize=False, verbose_name='nazwa')),
                ('description', models.TextField(default='None', verbose_name='opis')),
            ],
        ),
        migrations.CreateModel(
            name='Ligand_class',
            fields=[
                ('name', models.CharField(default=None, max_length=20, primary_key=True, serialize=False, verbose_name='nazwa')),
                ('description', models.TextField(default='None')),
            ],
        ),
        migrations.CreateModel(
            name='Organism',
            fields=[
                ('scientific_name', models.CharField(default=None, max_length=250, primary_key=True, serialize=False, verbose_name='nazwa_naukowa')),
                ('common_name', models.CharField(default='Undefined', max_length=250, verbose_name='nazwa_zwyczajowa')),
                ('accession_number', models.CharField(default='Undefined', max_length=15, verbose_name='numer_dostepu')),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.IntegerField(default=0)),
                ('end', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Undefined', max_length=20, verbose_name='nazwa')),
                ('sequence', models.TextField(default='Undefined', verbose_name='sekwencja')),
                ('genes_under_operon_regulation', models.CharField(default='Undefined', max_length=3000, verbose_name='geny_pod_regulacja_operonu')),
                ('_3D_structure', models.TextField(default='Undefined', verbose_name='struktura 3D')),
                ('effect', models.IntegerField(choices=[(1, 'ACTIVATION'), (0, 'UNKNOWN'), (-1, 'SILECING')], default=0)),
                ('mechanism', models.CharField(choices=[('TRN', 'TRANSCRIPTION'), ('TRL', 'TRANSLATION'), ('UN', 'UNKNOWN'), ('DG', 'DEGRADATION')], default='UN', max_length=3)),
                ('strand', models.CharField(choices=[('+', 'LEADING STRAND'), ('-', 'LAGGING STRAND'), ('0', 'UNKNOWN')], default='0', max_length=1)),
                ('articles', models.ManyToManyField(to='database.Article')),
            ],
        ),
        migrations.CreateModel(
            name='RiboClass',
            fields=[
                ('name', models.CharField(default=None, max_length=10, primary_key=True, serialize=False, verbose_name='nazwa')),
                ('description', models.TextField(default='None', verbose_name='opis')),
                ('alignment', models.TextField(default='Undefined')),
            ],
        ),
        migrations.CreateModel(
            name='RiboFamily',
            fields=[
                ('name', models.CharField(default=None, max_length=10, primary_key=True, serialize=False, verbose_name='nazwa')),
                ('description', models.TextField(default='', verbose_name='opis')),
                ('alignment', models.TextField(default='Undefined')),
                ('ribo_class', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='database.RiboClass')),
            ],
        ),
        migrations.CreateModel(
            name='Structure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('without_ligand', models.TextField(default='Undefined', verbose_name='bez_ligandu')),
                ('with_ligand', models.TextField(default='Undefined', verbose_name='z_ligandem')),
                ('predicted', models.TextField(default='Undefined', verbose_name='przewidziana')),
            ],
        ),
        migrations.AddField(
            model_name='record',
            name='family',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='database.RiboFamily'),
        ),
        migrations.AddField(
            model_name='record',
            name='gene',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='database.Gene'),
        ),
        migrations.AddField(
            model_name='record',
            name='ligand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='database.Ligand'),
        ),
        migrations.AddField(
            model_name='record',
            name='organism',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='database.Organism'),
        ),
        migrations.AddField(
            model_name='record',
            name='promoter',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='promoter', to='database.Position'),
        ),
        migrations.AddField(
            model_name='record',
            name='structure',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='database.Structure'),
        ),
        migrations.AddField(
            model_name='record',
            name='switch_position',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='switch_position', to='database.Position'),
        ),
        migrations.AddField(
            model_name='record',
            name='terminator',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='terminator', to='database.Position'),
        ),
        migrations.AddField(
            model_name='ligand',
            name='ligand_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='database.Ligand_class'),
        ),
        migrations.AddField(
            model_name='gene',
            name='organism',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Organism'),
        ),
    ]
