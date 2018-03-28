# Generated by Django 2.0.3 on 2018-03-28 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0005_auto_20180328_2001'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppError',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('error', models.CharField(max_length=15, verbose_name='Ошибка')),
            ],
            options={
                'verbose_name': 'Ошибка',
                'verbose_name_plural': 'Ошибки',
            },
        ),
        migrations.CreateModel(
            name='AppStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=15, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Статус',
                'verbose_name_plural': 'Статусы',
            },
        ),
        migrations.CreateModel(
            name='AppSuccess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('success', models.CharField(max_length=15, verbose_name='Выполнено')),
            ],
            options={
                'verbose_name': 'Выполнено',
                'verbose_name_plural': 'Выполнено',
            },
        ),
        migrations.AlterField(
            model_name='application',
            name='comment',
            field=models.CharField(max_length=2048, verbose_name='Комментарий отчета'),
        ),
        migrations.AlterField(
            model_name='application',
            name='comments',
            field=models.CharField(max_length=2048, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='application',
            name='connectors',
            field=models.IntegerField(default=0, verbose_name='Коннекторы'),
        ),
        migrations.AlterField(
            model_name='application',
            name='error',
            field=models.ForeignKey(on_delete='', to='application.AppError', verbose_name='Причины'),
        ),
        migrations.AlterField(
            model_name='application',
            name='num_router',
            field=models.CharField(max_length=15, verbose_name='Серийник роутера'),
        ),
        migrations.AlterField(
            model_name='application',
            name='num_tuner',
            field=models.CharField(max_length=50, verbose_name='MAC тюнера'),
        ),
        migrations.AlterField(
            model_name='application',
            name='port',
            field=models.IntegerField(blank=True, null=True, verbose_name='Порт'),
        ),
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.ForeignKey(on_delete='', to='application.AppStatus', verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='application',
            name='success',
            field=models.ForeignKey(on_delete='', to='application.AppSuccess', verbose_name='Тип работы'),
        ),
        migrations.AlterField(
            model_name='application',
            name='utp_external',
            field=models.IntegerField(default=0, verbose_name='Внешний кабель'),
        ),
        migrations.AlterField(
            model_name='application',
            name='utp_internal',
            field=models.IntegerField(default=0, verbose_name='Внутренний кабель'),
        ),
    ]
