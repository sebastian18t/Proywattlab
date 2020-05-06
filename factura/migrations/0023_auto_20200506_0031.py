# Generated by Django 3.0.3 on 2020-05-06 00:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('factura', '0022_auto_20200506_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banco',
            name='cnsctvo_cdd',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='factura.Ciudad'),
        ),
        migrations.AlterField(
            model_name='ciudad',
            name='cnsctvo_dprtmnto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='factura.Departamento'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cnsctvo_tpo_clnte',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='factura.TipoCliente'),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='cnsctvo_cdd',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='factura.Ciudad'),
        ),
        migrations.AlterField(
            model_name='subestacion',
            name='cnsctvo_cdd',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='factura.Ciudad'),
        ),
    ]
