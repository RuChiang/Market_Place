# Generated by Django 2.1.2 on 2018-10-31 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asp', '0007_auto_20181031_1416'),
    ]

    operations = [
        migrations.CreateModel(
            name='Available_Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='item',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='item',
            name='supplying_hospital',
        ),
        migrations.AddField(
            model_name='available_items',
            name='item_abstract',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asp.Item'),
        ),
        migrations.AddField(
            model_name='available_items',
            name='supplying_hospital',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asp.Hospital'),
        ),
    ]
