# Generated by Django 2.1.7 on 2019-03-22 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Ac_Admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Officer_Table',
            fields=[
                ('officer_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('mobile', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=100)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=20)),
                ('dept_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ac_Admin.Department_Table')),
            ],
        ),
    ]
