# Generated by Django 3.2.4 on 2021-06-26 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0013_alter_lecture_like_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
