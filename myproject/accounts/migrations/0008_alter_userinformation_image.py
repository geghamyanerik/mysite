# Generated by Django 5.1.4 on 2025-01-14 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_userinformation_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinformation',
            name='image',
            field=models.ImageField(blank=True, default='/1.jpg', null=True, upload_to='profile_images/'),
        ),
    ]
