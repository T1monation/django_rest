# Generated by Django 4.1.4 on 2023-02-03 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0005_rename_autor_article_author_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]