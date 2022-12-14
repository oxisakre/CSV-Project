# Generated by Django 3.2.5 on 2022-08-22 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Birthdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.DateTimeField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_type', models.CharField(choices=[('M', 'Masculine'), ('F', 'Feminine'), ('O', 'Other')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Identification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('birthdate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gview.birthdate')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gview.genre')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gview.person')),
            ],
        ),
    ]
