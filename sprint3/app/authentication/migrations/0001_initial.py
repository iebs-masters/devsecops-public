# Generated by Django 4.2.4 on 2023-08-09 06:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bio', models.TextField(blank=True, max_length=1000, null=True)),
                ('profile_image', models.FileField(blank=True, null=True, upload_to='profile_images')),
                ('cover_image', models.FileField(blank=True, null=True, upload_to='cover_images')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('country', models.TextField(blank=True, max_length=300, null=True)),
                ('city', models.TextField(blank=True, max_length=300, null=True)),
                ('street', models.TextField(blank=True, max_length=300, null=True)),
                ('postcode', models.TextField(blank=True, max_length=300, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]