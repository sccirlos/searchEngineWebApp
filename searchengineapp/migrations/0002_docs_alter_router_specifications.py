# Generated by Django 4.0.5 on 2022-06-27 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchengineapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Docs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urlDoc', models.TextField(verbose_name='Document')),
            ],
        ),
        migrations.AlterField(
            model_name='router',
            name='specifications',
            field=models.FileField(upload_to='router_specifications'),
        ),
    ]
