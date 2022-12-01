# Generated by Django 3.2.16 on 2022-11-25 16:45

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
            name='UserDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='逻辑删除')),
                ('avatar', models.TextField(blank=True, null=True, verbose_name='头像')),
                ('phone', models.CharField(blank=True, max_length=11, null=True, unique=True, verbose_name='手机号')),
                ('age', models.IntegerField(blank=True, null=True, verbose_name='年龄')),
                ('sex', models.IntegerField(blank=True, choices=[(0, '女'), (1, '男')], null=True, verbose_name='性别')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '用户详情',
                'verbose_name_plural': '用户详情',
                'db_table': 'user_detail',
            },
        ),
    ]
