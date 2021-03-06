# Generated by Django 3.2.3 on 2021-05-22 05:46

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
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, default='', max_length=250)),
                ('status', models.CharField(choices=[('started', 'Started'), ('completed', 'Completed'), ('progress', 'Progress'), ('failed', 'Failed')], default='Started', max_length=10)),
                ('report', models.URLField(blank=True)),
                ('pushNotification', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='snippets', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created', '-updated'),
            },
        ),
    ]
