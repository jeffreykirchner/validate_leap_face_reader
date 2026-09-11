from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0078_rename_email_ms_auth_access_token_parameters_email_ms_access_token_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ParameterSetBarrier',
        ),
    ]