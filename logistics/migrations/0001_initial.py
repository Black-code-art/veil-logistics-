# Generated by Django 5.1.2 on 2024-12-16 13:38

import django.db.models.deletion
import logistics.managers
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('role', models.CharField(choices=[('driver', 'driver'), ('user', 'user'), ('admin', 'admin')], max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', logistics.managers.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('tracking_id', models.CharField(max_length=50, unique=True)),
                ('sender_address', models.TextField()),
                ('receiver_address', models.TextField()),
                ('weight', models.FloatField()),
                ('dimensions', models.CharField(max_length=100)),
                ('service_level', models.Field(max_length=50)),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('IN_TRANSIT', 'In Transit'), ('DELIVERED', 'Delivered'), ('CANCELLED', 'Cancelled')], default='Pending', max_length=20)),
                ('current_location', models.CharField(max_length=450)),
                ('estimated_delivery_date', models.DateField()),
                ('shipment_history', models.TextField()),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer', to=settings.AUTH_USER_MODEL)),
                ('driver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='driver', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
