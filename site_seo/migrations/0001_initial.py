# Generated by Django 4.0.4 on 2022-12-06 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogSeo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_description', models.TextField(max_length=300, verbose_name='توضیحات متای صفحه اصلی مجله')),
                ('meta_keywords', models.TextField(max_length=300, verbose_name='کلمه های کلیدی صفحه اصلی مجله')),
                ('meta_robots', models.CharField(default='index,follow', max_length=100, verbose_name='تگ robots صفحه اصلی سایت')),
                ('link_canonical', models.CharField(default='https://hamtagame.ir/mag', max_length=100, verbose_name='تگ canonical صفحه اصلی سایت')),
            ],
            options={
                'verbose_name': 'سئوی صفحه اصلی مجله',
                'verbose_name_plural': 'سئوی صفحه اصلی مجله',
            },
        ),
        migrations.CreateModel(
            name='HomeSeo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_description', models.TextField(max_length=300, verbose_name='توضیحات متای صفحه اصلی سایت')),
                ('meta_keywords', models.TextField(max_length=300, verbose_name='کلمه های کلیدی صفحه اصلی سایت')),
                ('meta_robots', models.CharField(default='index,follow', max_length=100, verbose_name='تگ robots صفحه اصلی سایت')),
                ('link_canonical', models.CharField(default='https://hamtagame.ir', max_length=100, verbose_name='تگ canonical صفحه اصلی سایت')),
            ],
            options={
                'verbose_name': 'سئوی صفحه اصلی',
                'verbose_name_plural': 'سئوی صفحه اصلی',
            },
        ),
        migrations.CreateModel(
            name='SiteSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_title', models.CharField(max_length=150, verbose_name='عنوان سایت')),
                ('site_address', models.CharField(max_length=255, verbose_name='آدرس سایت')),
                ('site_phone', models.CharField(max_length=15, verbose_name='شماره تماس')),
                ('site_email', models.CharField(max_length=50, verbose_name='ایمیل سایت')),
                ('site_favicon_logo', models.ImageField(upload_to='images/icon', verbose_name='لوگوی سایت در مرورگر')),
                ('site_header_logo', models.ImageField(upload_to='', verbose_name='لوگو اصلی سایت')),
                ('site_header_logo_alt', models.CharField(max_length=100, verbose_name='متن جایگزین لوگوی اصلی سایت')),
                ('site_footer_logo', models.ImageField(upload_to='', verbose_name='لوگو اصلی فوتر سایت')),
                ('site_footer_logo_alt', models.CharField(max_length=100, verbose_name='متن جایگزین لوگوی اصلی فوتر سایت')),
                ('blog_header_logo', models.ImageField(upload_to='', verbose_name='لوگو اصلی مجله')),
                ('blog_header_logo_dark', models.ImageField(upload_to='', verbose_name='لوگو اصلی مجله دارک')),
                ('blog_header_logo_alt', models.CharField(max_length=100, verbose_name='متن جایگزین لوگوی اصلی مجله')),
                ('site_instagram', models.URLField(max_length=100, verbose_name='آدرس اینستاگرام')),
                ('site_footer_description', models.TextField(verbose_name='توضیحات فوتر سایت')),
                ('site_footer_text', models.TextField(verbose_name='متن فوتر فروشگاه')),
            ],
            options={
                'verbose_name': 'تنظیمات سایت',
                'verbose_name_plural': 'تنظیمات سایت',
            },
        ),
    ]
