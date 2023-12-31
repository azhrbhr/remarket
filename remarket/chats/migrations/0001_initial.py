# Generated by Django 4.2.5 on 2023-09-29 14:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('interests', '0003_alter_interest_message_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('buyer', 'Buyer'), ('seller', 'Seller')], max_length=10)),
                ('status', models.CharField(choices=[('active', 'Active'), ('archived', 'Archived'), ('closed', 'Closed')], default='active', max_length=10)),
                ('unread_messages_count', models.PositiveIntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('interest', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='interests.interest')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('is_read', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chats.chat')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
