# Generated by Django 2.1.4 on 2019-06-13 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='链接名称')),
                ('link', models.URLField(verbose_name='链接地址')),
                ('sequence', models.IntegerField(unique=True, verbose_name='排序')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_mod_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '友情链接',
                'verbose_name_plural': '友情链接',
                'ordering': ['sequence'],
            },
        ),
        migrations.AddField(
            model_name='article',
            name='commentstatus',
            field=models.CharField(choices=[('o', '打开'), ('c', '关闭')], default='o', max_length=1, verbose_name='评论状态'),
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('d', '草稿'), ('p', '发表')], default='o', max_length=1, verbose_name='文章状态'),
        ),
    ]
