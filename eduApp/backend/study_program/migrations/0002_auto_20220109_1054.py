# Generated by Django 3.1.5 on 2022-01-09 10:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('study_program', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='program_user_created',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Program_user_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='program',
            name='program_user_updated',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Program_user_updated', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('class_id', models.AutoField(primary_key=True, serialize=False)),
                ('class_updated_at', models.DateTimeField(auto_now=True)),
                ('class_created_at', models.DateTimeField(auto_now_add=True)),
                ('class_name', models.TextField(blank=True, max_length=250, null=True)),
                ('class_detail', models.TextField(blank=True, max_length=500, null=True)),
                ('class_status', models.BooleanField(blank=True, default=True, null=True)),
                ('class_abbreviations', models.TextField(blank=True, max_length=250, null=True)),
                ('class_program', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Class_program', to='study_program.program')),
                ('class_user_created', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Class_user_created', to=settings.AUTH_USER_MODEL)),
                ('class_user_updated', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Class_user_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'class',
            },
        ),
    ]
