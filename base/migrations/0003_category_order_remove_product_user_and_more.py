# Generated by Django 4.0.6 on 2022-09-28 18:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0002_remove_product_createdtime'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('desc', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('createdTime', models.DateTimeField(auto_now_add=True)),
                ('total', models.IntegerField()),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='user',
        ),
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.SmallIntegerField(),
        ),
        migrations.CreateModel(
            name='Pita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order_det',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('amount', models.IntegerField()),
                ('total', models.IntegerField()),
                ('order_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.order')),
                ('prod_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.product')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='cat_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.category'),
        ),
    ]
