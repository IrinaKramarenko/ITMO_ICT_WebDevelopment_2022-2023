# Generated by Django 4.1.2 on 2022-11-07 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw_app', '0003_alter_studenthomework_date_submit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studenthomework',
            name='grade',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]