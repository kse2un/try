# Generated by Django 3.0.8 on 2020-09-09 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aliceapp', '0004_auto_20200903_2029'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer1', models.CharField(max_length=500)),
                ('answer2', models.CharField(max_length=500)),
                ('image1', models.ImageField(upload_to='images/')),
                ('image2', models.ImageField(upload_to='images/')),
            ],
        ),
    ]