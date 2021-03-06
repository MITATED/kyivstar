# Generated by Django 2.0.3 on 2018-03-28 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_auto_20180328_1847'),
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house', models.CharField(max_length=15, verbose_name='Квартира')),
            ],
            options={
                'verbose_name_plural': 'Дома',
                'verbose_name': 'Дом',
            },
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=15, verbose_name='Квартира')),
            ],
            options={
                'verbose_name_plural': 'Улицы',
                'verbose_name': 'Улица',
            },
        ),
        migrations.AlterModelOptions(
            name='apartment',
            options={'verbose_name': 'Квартира', 'verbose_name_plural': 'Квартиры'},
        ),
        migrations.AlterModelOptions(
            name='application',
            options={'verbose_name': 'Заявка', 'verbose_name_plural': 'Заявки'},
        ),
        migrations.AlterModelOptions(
            name='apptypes',
            options={'verbose_name': 'Тип', 'verbose_name_plural': 'Типы'},
        ),
        migrations.AlterField(
            model_name='apartment',
            name='house',
            field=models.ForeignKey(on_delete='', to='application.House', verbose_name='Дом'),
        ),
        migrations.AlterField(
            model_name='apptypes',
            name='types',
            field=models.CharField(max_length=64, verbose_name='Название типа'),
        ),
        migrations.AddField(
            model_name='house',
            name='street',
            field=models.ForeignKey(on_delete='', to='application.Street', verbose_name='Улица'),
        ),
    ]
