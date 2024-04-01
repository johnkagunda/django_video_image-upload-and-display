# Generated by Django 5.0.2 on 2024-04-01 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media')),
                ('video', models.FileField(blank=True, null=True, upload_to='media')),
            ],
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
