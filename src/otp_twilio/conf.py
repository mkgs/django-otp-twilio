import django.conf
import django.test.utils


class Settings(object):
    """
    This is a simple class to take the place of the global settings object. An
    instance will contain all of our settings as attributes, with default
    values if they are not specified by the configuration.
    """
    _defaults = {
        'OTP_TWILIO_URL': "https://api.twilio.com",
        'OTP_TWILIO_ACCOUNT': None,
        'OTP_TWILIO_API_KEY': None,
        'OTP_TWILIO_AUTH': None,
        'OTP_TWILIO_CHALLENGE_MESSAGE': "Sent by SMS",
        'OTP_TWILIO_FROM': None,
        'OTP_TWILIO_FROM_UK': None,
        'OTP_TWILIO_NO_DELIVERY': False,
        'OTP_TWILIO_THROTTLE_FACTOR': 1,
        'OTP_TWILIO_TOKEN_TEMPLATE': '{token}',
        'OTP_TWILIO_TOKEN_VALIDITY': 30,
    }

    def __getattr__(self, name):
        if hasattr(django.conf.settings, name):
            value = getattr(django.conf.settings, name)
        elif name in self._defaults:
            value = self._defaults[name]
        else:
            raise AttributeError(name)

        return value


settings = Settings()
