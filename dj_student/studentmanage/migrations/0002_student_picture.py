# Generated by Django 5.0.6 on 2024-05-27 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentmanage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='student_pictures/'),
        ),
    ]