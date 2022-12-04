# Generated by Django 3.2.16 on 2022-12-02 20:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0004_area'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='逻辑删除')),
                ('name', models.CharField(max_length=40, verbose_name='地址名')),
                ('receiver', models.CharField(max_length=40, verbose_name='收货人')),
                ('place', models.CharField(max_length=40, verbose_name='详情地址')),
                ('mobile', models.CharField(max_length=11, verbose_name='手机')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='city_address', to='users.area', verbose_name='市')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='district_address', to='users.area', verbose_name='区')),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='province_address', to='users.area', verbose_name='省')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'db_table': 'address',
                'ordering': ['-update_time'],
            },
        ),
    ]