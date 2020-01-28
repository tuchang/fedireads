# Generated by Django 3.0.2 on 2020-01-28 09:04

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('private_key', models.TextField(blank=True, null=True)),
                ('public_key', models.TextField(blank=True, null=True)),
                ('api_key', models.CharField(blank=True, max_length=255, null=True)),
                ('actor', models.CharField(max_length=255)),
                ('inbox', models.CharField(max_length=255)),
                ('outbox', models.CharField(max_length=255)),
                ('summary', models.TextField(blank=True, null=True)),
                ('local', models.BooleanField(default=True)),
                ('localname', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('followers', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(max_length=255, unique=True)),
                ('content', django.contrib.postgres.fields.jsonb.JSONField(max_length=5000)),
                ('activity_type', models.CharField(max_length=255)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('openlibrary_key', models.CharField(max_length=255)),
                ('data', django.contrib.postgres.fields.jsonb.JSONField()),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activitypub_id', models.CharField(max_length=255)),
                ('openlibrary_key', models.CharField(max_length=255)),
                ('data', django.contrib.postgres.fields.jsonb.JSONField()),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('authors', models.ManyToManyField(to='fedireads.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Shelf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activitypub_id', models.CharField(max_length=255)),
                ('identifier', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=100)),
                ('editable', models.BooleanField(default=True)),
                ('shelf_type', models.CharField(default='custom', max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('openlibrary_key', models.CharField(max_length=255)),
                ('data', django.contrib.postgres.fields.jsonb.JSONField()),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('activity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fedireads.Activity')),
            ],
            bases=('fedireads.activity',),
        ),
        migrations.CreateModel(
            name='ShelfBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fedireads.Book')),
                ('shelf', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fedireads.Shelf')),
            ],
            options={
                'unique_together': {('book', 'shelf')},
            },
        ),
        migrations.AddField(
            model_name='shelf',
            name='books',
            field=models.ManyToManyField(through='fedireads.ShelfBook', to='fedireads.Book'),
        ),
        migrations.AddField(
            model_name='shelf',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='book',
            name='shelves',
            field=models.ManyToManyField(through='fedireads.ShelfBook', to='fedireads.Shelf'),
        ),
        migrations.AddField(
            model_name='book',
            name='works',
            field=models.ManyToManyField(to='fedireads.Work'),
        ),
        migrations.CreateModel(
            name='ShelveActivity',
            fields=[
                ('activity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fedireads.Activity')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fedireads.Book')),
                ('shelf', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fedireads.Shelf')),
            ],
            bases=('fedireads.activity',),
        ),
        migrations.AlterUniqueTogether(
            name='shelf',
            unique_together={('user', 'name')},
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('activity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fedireads.Activity')),
                ('name', models.TextField()),
                ('rating', models.IntegerField(default=0)),
                ('review_content', models.TextField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fedireads.Book')),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fedireads.Work')),
            ],
            bases=('fedireads.activity',),
        ),
        migrations.CreateModel(
            name='FollowActivity',
            fields=[
                ('activity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fedireads.Activity')),
                ('followed', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='followed', to=settings.AUTH_USER_MODEL)),
            ],
            bases=('fedireads.activity',),
        ),
    ]
