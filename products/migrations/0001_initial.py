# Generated by Django 3.2.5 on 2022-06-07 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
                ('Price', models.DecimalField(decimal_places=5, max_digits=6)),
                ('Description', models.CharField(max_length=500)),
                ('Color', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=50)),
                ('Quantite', models.DecimalField(decimal_places=5, max_digits=6)),
                ('Taille', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=4)),
                ('Present_Panier', models.BooleanField(default=False)),
            ],
        ),
    ]
