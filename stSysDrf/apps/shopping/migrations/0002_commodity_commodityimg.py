# Generated by Django 3.2.16 on 2022-12-03 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='逻辑删除')),
                ('name', models.CharField(max_length=40, verbose_name='商品名')),
                ('caption', models.CharField(max_length=40, verbose_name='副标题')),
                ('brand', models.CharField(blank=True, max_length=40, null=True, verbose_name='品牌')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='单价')),
                ('stock', models.IntegerField(verbose_name='库存')),
                ('pack', models.TextField(blank=True, null=True, verbose_name='包装信息')),
                ('service_aftersale', models.TextField(blank=True, null=True, verbose_name='售后服务')),
                ('sales', models.IntegerField(default=0, verbose_name='销量')),
                ('comments', models.IntegerField(default=0, verbose_name='评价数')),
                ('status', models.IntegerField(choices=[(0, '未发货'), (1, '已发货')], default=0, verbose_name='状态')),
                ('detail', models.TextField(blank=True, null=True, verbose_name='详情')),
                ('classification1', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='classification1', to='shopping.classification', verbose_name='一级分类')),
                ('classification2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='classification2', to='shopping.classification', verbose_name='二级分类')),
            ],
            options={
                'verbose_name': '商品',
                'verbose_name_plural': '商品',
                'db_table': 'commodity',
                'ordering': ['-sales', '-comments', '-create_time'],
            },
        ),
        migrations.CreateModel(
            name='CommodityImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src', models.TextField(verbose_name='图片地址')),
                ('priority', models.IntegerField(default=0, verbose_name='优先级')),
                ('commodity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.commodity', verbose_name='商品')),
            ],
            options={
                'verbose_name': '商品图',
                'verbose_name_plural': '商品图',
                'db_table': 'commodity_img',
                'ordering': ['-priority'],
            },
        ),
    ]
