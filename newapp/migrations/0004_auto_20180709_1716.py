# Generated by Django 2.0.7 on 2018-07-10 00:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0003_auto_20180709_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='newapp.Person'),
        ),
    ]
