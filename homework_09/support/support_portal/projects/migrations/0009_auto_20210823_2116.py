# Generated by Django 3.2.4 on 2021-08-23 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_alter_task_create_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='member_owner',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='projects.member'),
        ),
        migrations.AlterField(
            model_name='task',
            name='project',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='projects.project'),
        ),
    ]
