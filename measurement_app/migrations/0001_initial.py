# Generated by Django 4.1 on 2023-04-19 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MeasurementRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('height', models.DecimalField(decimal_places=3, default=0, max_digits=20)),
                ('weight', models.DecimalField(decimal_places=3, default=0, max_digits=20)),
                ('age', models.DecimalField(decimal_places=3, default=0, max_digits=20)),
                ('waist', models.DecimalField(decimal_places=3, default=0, max_digits=20)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
