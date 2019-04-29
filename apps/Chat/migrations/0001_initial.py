# Generated by Django 2.1.5 on 2019-04-28 00:36

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
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amigos', models.ManyToManyField(blank=True, related_name='_contacto_amigos_+', to='Chat.Contacto')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amigos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('contacto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensajes', to='Chat.Contacto')),
            ],
        ),
        migrations.AddField(
            model_name='chat',
            name='mensajes',
            field=models.ManyToManyField(blank=True, to='Chat.Mensaje'),
        ),
        migrations.AddField(
            model_name='chat',
            name='participantes',
            field=models.ManyToManyField(related_name='chats', to='Chat.Contacto'),
        ),
    ]