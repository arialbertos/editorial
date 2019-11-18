# Generated by Django 2.2.7 on 2019-11-18 03:42

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
            name='PerfilUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('run', models.CharField(max_length=20)),
                ('nacimiento', models.DateField()),
                ('telefono', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=50)),
                ('comuna', models.CharField(max_length=50)),
                ('vivienda', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
