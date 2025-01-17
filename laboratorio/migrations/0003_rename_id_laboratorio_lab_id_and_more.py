# Generated by Django 5.1.1 on 2024-10-27 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0002_rename_f_fabricacion2_producto_f_fabricacion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='laboratorio',
            old_name='id',
            new_name='lab_id',
        ),
        migrations.RenameField(
            model_name='laboratorio',
            old_name='nombre',
            new_name='lab_nombre',
        ),
        migrations.AddField(
            model_name='directorgeneral',
            name='especialidad',
            field=models.CharField(default='Medico General', max_length=255),
        ),
        migrations.AddField(
            model_name='laboratorio',
            name='lab_ciudad',
            field=models.CharField(default='Santiago', max_length=255),
        ),
        migrations.AddField(
            model_name='laboratorio',
            name='lab_pais',
            field=models.CharField(default='Chile', max_length=255),
        ),
        migrations.AlterField(
            model_name='producto',
            name='f_fabricacion',
            field=models.IntegerField(choices=[(2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024)]),
        ),
        migrations.DeleteModel(
            name='ProductoLaboratorio',
        ),
    ]
