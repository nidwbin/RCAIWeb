# Generated by Django 3.2.7 on 2021-09-26 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True, verbose_name='姓名')),
                ('password', models.CharField(blank=True, max_length=30, null=True, verbose_name='密码')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='出生年月')),
                ('gender', models.CharField(choices=[('male', '男'), ('female', '女')], default='female', max_length=6, verbose_name='性别')),
                ('mobile', models.CharField(blank=True, max_length=11, null=True, verbose_name='电话')),
                ('email', models.EmailField(blank=True, max_length=100, null=True, verbose_name='邮箱')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
            },
        ),
    ]
