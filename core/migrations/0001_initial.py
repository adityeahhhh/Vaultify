# Generated by Django 5.1.7 on 2025-04-13 17:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=255)),
                ('content', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('unlock_datetime', models.DateTimeField()),
                ('visibility', models.CharField(choices=[('public', 'Public'), ('private', 'Private')], default='private', max_length=10)),
                ('file', models.FileField(blank=True, null=True, upload_to='files/')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('video', models.FileField(blank=True, null=True, upload_to='videos/')),
                ('mood', models.CharField(blank=True, max_length=50)),
                ('is_nsfw', models.BooleanField(default=False)),
                ('is_malicious', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
