from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0080_remove_parametersetwall_parameter_set_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ParameterSetGround',
        ),
    ]