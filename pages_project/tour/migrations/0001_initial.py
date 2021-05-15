# Generated by Django 2.0.7 on 2021-05-13 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
                ('price', models.IntegerField()),
                ('offer', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery_pics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(default=None, upload_to='pics')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lname', models.CharField(default='chalyoo', max_length=100)),
                ('phone_number', models.CharField(default='chalyoo', max_length=100)),
                ('email', models.CharField(default='chalyoo', max_length=100)),
                ('destination', models.CharField(default='chalyoo', max_length=100)),
                ('startdate', models.CharField(default='chalyoo', max_length=100)),
                ('adult', models.IntegerField(null=True)),
                ('child', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField()),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]