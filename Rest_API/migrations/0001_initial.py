# Generated by Django 3.2.4 on 2021-07-25 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SNo', models.IntegerField(verbose_name='SNo')),
                ('Symbol', models.CharField(max_length=50, verbose_name='Symbol')),
                ('Date', models.DateField(auto_now=True, verbose_name='Date')),
                ('Open', models.FloatField(verbose_name='Open')),
                ('High', models.FloatField(verbose_name='High')),
                ('Low', models.FloatField(verbose_name='Low')),
                ('Close', models.FloatField(verbose_name='Close')),
                ('Vol', models.FloatField(verbose_name='Vol')),
            ],
        ),
    ]