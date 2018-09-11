# Generated by Django 2.0.7 on 2018-07-17 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0004_auto_20180709_1716'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='person',
            name='address',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone_number',
            field=models.CharField(max_length=40, null=True),
        ),
    ]