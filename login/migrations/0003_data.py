# Generated by Django 5.0.2 on 2024-03-02 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_delete_data_delete_figure'),
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
