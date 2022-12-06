# Generated by Django 4.0.4 on 2022-12-06 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان')),
                ('image', models.ImageField(upload_to='images/slider', verbose_name='تصویر')),
                ('url_address', models.URLField(verbose_name='آدرس URL')),
            ],
            options={
                'verbose_name': 'اسلایدر مجله',
                'verbose_name_plural': 'اسلایدر های مجله',
            },
        ),
        migrations.CreateModel(
            name='SliderHome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/slider', verbose_name='تصویر اسلایدر')),
                ('image_title', models.CharField(max_length=255, verbose_name='عنوان تصویر')),
                ('image_alt', models.CharField(max_length=255, verbose_name='متن جایگزین تصویر')),
                ('url', models.URLField(verbose_name='آدرس URL')),
                ('status', models.BooleanField(default=False, verbose_name='وضعیت انتشار')),
            ],
            options={
                'verbose_name': 'اسلایدر فروشگاه',
                'verbose_name_plural': 'اسلایدر های فروشگاه',
            },
        ),
        migrations.CreateModel(
            name='SliderOfferDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when', models.DateTimeField(verbose_name='تاریخ تخفیف')),
            ],
            options={
                'verbose_name': 'تاریخ تخفیف فروشگاه',
                'verbose_name_plural': 'تاریخ های تخفیف فروشگاه',
            },
        ),
        migrations.CreateModel(
            name='SliderHomeOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product', verbose_name='محصول')),
            ],
            options={
                'verbose_name': 'اسلایدر تخفیف فروشگاه',
                'verbose_name_plural': 'اسلایدر های تخفیف فروشگاه',
            },
        ),
    ]
