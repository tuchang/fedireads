# Generated by Django 3.0.3 on 2020-03-07 22:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fedireads', '0010_auto_20200307_0655'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('read', models.BooleanField(default=False)),
                ('notification_type', models.CharField(max_length=255)),
                ('related_book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='fedireads.Book')),
                ('related_status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='fedireads.Status')),
                ('related_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='related_user', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
