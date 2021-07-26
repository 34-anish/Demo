# Generated by Django 3.2.4 on 2021-07-25 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rest_API', '0003_index_subindex_topgainers_toploosers_toptradedshares_topturnovers'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatewiseIndex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('NepseIndex', models.TextField()),
                ('AbsoluteChange', models.FloatField()),
                ('PercentageChange', models.FloatField()),
            ],
        ),
    ]
