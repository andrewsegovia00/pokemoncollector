# Generated by Django 4.2.3 on 2023-07-28 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_attack_names'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attack',
            name='description',
            field=models.TextField(default='None', max_length=250),
        ),
        migrations.AlterField(
            model_name='attack',
            name='names',
            field=models.CharField(default='Nameless', max_length=100),
        ),
    ]
