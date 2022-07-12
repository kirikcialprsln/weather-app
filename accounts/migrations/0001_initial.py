# Generated by Django 4.0.6 on 2022-07-12 18:07

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('username', models.CharField(help_text='30 karakter veya daha az, Türkçe olmayan, harf ve rakamlardan bir kelime.', max_length=30, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='Kullanıcı Adı')),
                ('first_name', models.CharField(blank=True, max_length=80, null=True, verbose_name='Ad')),
                ('last_name', models.CharField(blank=True, max_length=80, null=True, verbose_name='Soyad')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-Posta')),
                ('is_active', models.BooleanField(default=True, help_text='Bu kullanıcının etkin olarak işlem görüp görmediğini belirler. Hesapları silmek yerine bunun işaretini kaldırın.', verbose_name='Kullanıcı etkin mi ?')),
                ('user_permission', models.CharField(choices=[('superuser', 'Yönetici'), ('user', 'Kullanıcı')], default='seller', help_text='Kullanıcının sitedeki erişim sınırını belirler.', max_length=20, verbose_name='Kullanıcı Yetki')),
                ('last_login', models.DateTimeField(blank=True, help_text='Kullanıcının en son sistemde oturum açma tarihi.', null=True, verbose_name='Son Oturum Açma')),
                ('date_joined', models.DateTimeField(auto_now_add=True, help_text='Kullanıcının sisteme kayıt tarihi.', verbose_name='Kayıt Tarihi')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Kullanıcı',
                'verbose_name_plural': 'Kullanıcılar',
                'db_table': 'users',
                'ordering': ('id',),
            },
        ),
    ]