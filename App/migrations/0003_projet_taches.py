# Generated by Django 4.0.1 on 2022-04-12 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_alter_projet_statut_projet_relation_projet_tache'),
    ]

    operations = [
        migrations.AddField(
            model_name='projet',
            name='taches',
            field=models.ManyToManyField(through='App.Relation_Projet_Tache', to='App.Tache'),
        ),
    ]