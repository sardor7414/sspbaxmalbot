# Generated by Django 4.2 on 2023-04-25 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appeals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=150, verbose_name='Korxona yoki tashkilot nomi')),
                ('address', models.CharField(max_length=255, verbose_name='Korxona manzili')),
                ('name', models.CharField(max_length=200, verbose_name='Murojaatchi FIO')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Telefon raqami')),
                ('content_appeal', models.TextField(unique=True, verbose_name='Murojaat mazmuni')),
                ('type_appeal', models.CharField(max_length=30, verbose_name='Murojaat turi')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Murojaat qilingan vaqt')),
            ],
            options={
                'verbose_name': 'Murojaat',
                'verbose_name_plural': 'Murojaatlar',
            },
        ),
    ]
