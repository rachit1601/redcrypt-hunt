# Generated by Django 4.0.4 on 2022-06-26 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortner', '0002_urlshortner_content_urlshortner_is_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlshortner',
            name='content',
            field=models.CharField(blank=True, max_length=999999, null=True),
        ),
    ]
