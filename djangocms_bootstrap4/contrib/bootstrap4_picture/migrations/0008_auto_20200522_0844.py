# Generated by Django 2.2.10 on 2020-05-22 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bootstrap4_picture', '0007_auto_20190801_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bootstrap4picture',
            name='use_automatic_scaling',
            field=models.BooleanField(blank=True, default=True, help_text='Uses the placeholder dimensions to automatically calculate the size.', verbose_name='Automatic scaling'),
        ),
        migrations.AlterField(
            model_name='bootstrap4picture',
            name='use_crop',
            field=models.BooleanField(blank=True, default=False, help_text='Crops the image according to the thumbnail settings provided in the template.', verbose_name='Crop image'),
        ),
        migrations.AlterField(
            model_name='bootstrap4picture',
            name='use_no_cropping',
            field=models.BooleanField(blank=True, default=False, help_text='Outputs the raw image without cropping.', verbose_name='Use original image'),
        ),
        migrations.AlterField(
            model_name='bootstrap4picture',
            name='use_upscale',
            field=models.BooleanField(blank=True, default=False, help_text='Upscales the image to the size of the thumbnail settings in the template.', verbose_name='Upscale image'),
        ),
    ]
