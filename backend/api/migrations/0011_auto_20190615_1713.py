# Generated by Django 2.2.1 on 2019-06-16 00:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20190615_1713'),
        ('api', '0010_auto_20190528_1923'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='ratings',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='ratings',
            name='game',
        ),
        migrations.RemoveField(
            model_name='ratings',
            name='user',
        ),
        migrations.DeleteModel(
            name='Game',
        ),
        migrations.DeleteModel(
            name='Ratings',
        ),
    ]
