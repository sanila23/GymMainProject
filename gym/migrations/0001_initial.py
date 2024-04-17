# Generated by Django 3.1.6 on 2022-08-08 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Due_date', models.DateField()),
                ('Customer_id', models.CharField(max_length=50)),
                ('Mobileno', models.CharField(max_length=10)),
                ('From_date', models.DateField()),
                ('To_date', models.DateField()),
                ('Package_Type', models.CharField(choices=[('--select--', '--select--'), ('One Month', 'One Month'), ('Three Month', 'Three Month'), ('Six Month', 'Six Month'), ('Twelve Month', 'Twelve Month')], default='--select--', max_length=50)),
                ('Amount', models.CharField(max_length=50)),
                ('Payed', models.CharField(max_length=50)),
                ('Batch', models.CharField(choices=[('--select--', '--select--'), ('Morning', 'Morning'), ('Evening', 'Evening')], default='--select--', max_length=50)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Paid', 'Paid')], default='Pending', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Diet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Diet', models.CharField(max_length=50)),
                ('Solution1', models.CharField(max_length=100)),
                ('Solution2', models.CharField(max_length=100)),
                ('Process', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=100)),
                ('Other_Notes', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=30)),
                ('Password', models.CharField(max_length=20)),
                ('Mobile', models.CharField(max_length=10)),
                ('Weight', models.CharField(max_length=20)),
                ('Height', models.CharField(max_length=20)),
                ('Age', models.CharField(max_length=20)),
                ('Address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dayno', models.CharField(max_length=50)),
                ('Schedule_for', models.CharField(max_length=100)),
                ('Trainee_level', models.CharField(max_length=100)),
                ('Process', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=100)),
                ('Other_Notes', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Total_no_of_days', models.CharField(max_length=50)),
                ('No_of_days_present', models.CharField(max_length=100)),
                ('Email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.member')),
            ],
        ),
    ]
