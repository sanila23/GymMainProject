# Generated by Django 3.1.6 on 2022-08-09 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0003_auto_20220808_1328'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_name', models.CharField(max_length=50)),
                ('Product_pic', models.ImageField(upload_to='')),
                ('Price', models.CharField(max_length=20)),
                ('Product_description', models.CharField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='Attendance',
        ),
    ]
