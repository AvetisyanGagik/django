# Generated by Django 4.0.6 on 2022-07-14 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Category name')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Product name')),
                ('price', models.IntegerField(verbose_name='Product price')),
                ('img', models.ImageField(upload_to='media', verbose_name='Product image')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='catprod', to='main.category')),
            ],
        ),
    ]