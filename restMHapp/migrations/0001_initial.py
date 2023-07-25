# Generated by Django 4.2.3 on 2023-07-25 19:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ctclid', models.CharField(max_length=100)),
                ('contractName', models.CharField(max_length=100)),
                ('assetName', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=4, max_digits=20)),
                ('quantity', models.PositiveIntegerField()),
                ('side', models.CharField(max_length=10)),
                ('lotside', models.PositiveIntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
