# Generated by Django 3.1.2 on 2022-05-16 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_auto_20220516_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherstudent',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teachers', to='school.student'),
        ),
    ]