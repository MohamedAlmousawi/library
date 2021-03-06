# Generated by Django 4.0.5 on 2022-06-20 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='اسم الكتاب: ')),
                ('auther', models.CharField(blank=True, max_length=50, null=True, verbose_name='اسم المؤلف: ')),
                ('book_image', models.ImageField(blank=True, null=True, upload_to='images/books', verbose_name='صورة الكتاب')),
                ('auther_image', models.ImageField(blank=True, null=True, upload_to='images/authers', verbose_name='صورة الكتاب')),
                ('pages', models.IntegerField(blank=True, default=1, null=True, verbose_name='عدد الصفحات : ')),
                ('status', models.CharField(choices=[('rented', 'مؤجر'), ('sold', 'مباع'), ('Available', 'متاح')], max_length=50, verbose_name='حالة الكتاب : ')),
                ('prise', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='السعر : ')),
                ('rented_prise_day', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='سعر التأجير في اليوم: ')),
                ('rented_time', models.IntegerField(blank=True, null=True, verbose_name='مدة التأجير : ')),
                ('rented_prise', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='سعر التأجير النهائي : ')),
                ('book_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home1.category')),
            ],
        ),
    ]
