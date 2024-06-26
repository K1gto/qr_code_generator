# Generated by Django 5.0.6 on 2024-05-22 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='qrcode',
            old_name='created_time',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='qrcode',
            old_name='owner',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='qrcode',
            name='content',
        ),
        migrations.RemoveField(
            model_name='qrcode',
            name='title',
        ),
        migrations.AddField(
            model_name='qrcode',
            name='link',
            field=models.URLField(default='url'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='qrcode',
            name='qr_code_image',
            field=models.ImageField(default=1, upload_to='qr_codes/'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
