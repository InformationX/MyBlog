# Generated by Django 2.1.4 on 2019-06-13 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190613_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='commentstatus',
            field=models.CharField(choices=[('o', '打开'), ('c', '关闭')], max_length=1, verbose_name='评论状态'),
        ),
    ]