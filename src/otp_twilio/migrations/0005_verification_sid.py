from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otp_twilio', '0004_sidechanneldevice'),
    ]

    operations = [
        migrations.AddField(
            model_name='twiliosmsdevice',
            name='verification_sid',
            field=models.CharField(max_length=34, null=True),
        ),
    ]
