# Generated by Django 4.1.3 on 2022-12-28 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('mobile', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('city', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('country', models.CharField(default='india', max_length=100)),
                ('state', models.CharField(default='gujrat', max_length=100)),
                ('pincode', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(default='gandhinagar', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(default='india', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='pincode',
            field=models.IntegerField(default=360570),
        ),
        migrations.AddField(
            model_name='user',
            name='state',
            field=models.CharField(default='gujrat', max_length=100),
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('made_on', models.DateTimeField(auto_now_add=True)),
                ('amount', models.IntegerField()),
                ('order_id', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('checksum', models.CharField(blank=True, max_length=100, null=True)),
                ('made_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='myapp.user')),
            ],
        ),
    ]
