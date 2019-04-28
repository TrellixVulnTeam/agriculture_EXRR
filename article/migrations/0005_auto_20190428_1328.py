# Generated by Django 2.2 on 2019-04-28 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_article_views'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('slug', models.SlugField(max_length=20, unique=True)),
            ],
        ),
        migrations.RenameField(
            model_name='article',
            old_name='views',
            new_name='viewscounter',
        ),
    ]
