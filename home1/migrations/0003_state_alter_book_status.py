# Generated by Django 4.0.5 on 2022-06-20 23:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home1', '0002_alter_book_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home1.state'),
        ),
    ]