# Generated by Django 3.0.1 on 2022-05-25 03:57

from django.db import migrations, models
import django.db.models.deletion
import enigma.users.models


class Migration(migrations.Migration):

    dependencies = [
        ('oth', '0017_auto_20220525_0357'),
        ('users', '0018_auto_20170308_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cur_phase',
            field=models.ForeignKey(default=enigma.users.models.get_or_create_phase, null=True, on_delete=django.db.models.deletion.PROTECT, to='oth.Phase'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
    ]