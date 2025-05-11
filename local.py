# Every setting in base.py can be overloaded by redefining it here.
from .base import *

SECRET_KEY = os.environ.get("AA_SECRET_KEY")
SITE_NAME = os.environ.get("AA_SITENAME")
SITE_URL = (
    f"{os.environ.get('PROTOCOL')}"
    f"{os.environ.get('AUTH_SUBDOMAIN')}."
    f"{os.environ.get('DOMAIN')}"
)
CSRF_TRUSTED_ORIGINS = [SITE_URL]
DEBUG = os.environ.get("AA_DEBUG", False)
DATABASES["default"] = {
    "ENGINE": "django.db.backends.mysql",
    "NAME": os.environ.get("AA_DB_NAME"),
    "USER": os.environ.get("AA_DB_USER"),
    "PASSWORD": os.environ.get("AA_DB_PASSWORD"),
    "HOST": os.environ.get("AA_DB_HOST"),
    "PORT": os.environ.get("AA_DB_PORT", "3306"),
    "OPTIONS": {
        "charset": os.environ.get("AA_DB_CHARSET", "utf8mb4")
    }
}

# Register an application at https://developers.eveonline.com for Authentication
# & API Access and fill out these settings. Be sure to set the callback URL
# to https://example.com/sso/callback substituting your domain for example.com
# Logging in to auth requires the publicData scope (can be overridden through the
# LOGIN_TOKEN_SCOPES setting). Other apps may require more (see their docs).


ESI_SSO_CLIENT_ID = os.environ.get("ESI_SSO_CLIENT_ID")
ESI_SSO_CLIENT_SECRET = os.environ.get("ESI_SSO_CLIENT_SECRET")
ESI_SSO_CALLBACK_URL = f"{SITE_URL}/sso/callback"
ESI_USER_CONTACT_EMAIL = os.environ.get(
    "ESI_USER_CONTACT_EMAIL"
)  # A server maintainer that CCP can contact in case of issues.

# By default emails are validated before new users can log in.
# It's recommended to use a free service like SparkPost or Elastic Email to send email.
# https://www.sparkpost.com/docs/integrations/django/
# https://elasticemail.com/resources/settings/smtp-api/
# Set the default from email to something like 'noreply@example.com'
# Email validation can be turned off by uncommenting the line below. This can break some services.
REGISTRATION_VERIFY_EMAIL = False
EMAIL_HOST = os.environ.get("AA_EMAIL_HOST", "")
EMAIL_PORT = os.environ.get("AA_EMAIL_PORT", 587)
EMAIL_HOST_USER = os.environ.get("AA_EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = os.environ.get("AA_EMAIL_HOST_PASSWORD", "")
EMAIL_USE_TLS = os.environ.get("AA_EMAIL_USE_TLS", True)
DEFAULT_FROM_EMAIL = os.environ.get("AA_DEFAULT_FROM_EMAIL", "")

ROOT_URLCONF = "myauth.urls"
WSGI_APPLICATION = "myauth.wsgi.application"
STATIC_ROOT = "/var/www/myauth/static/"
BROKER_URL = f"redis://{os.environ.get('AA_REDIS', 'redis:6379')}/1"
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://{os.environ.get('AA_REDIS', 'redis:6379')}/2",  # change the 1 here to change the database used
    }
}


# Add any additional apps to this list.
INSTALLED_APPS += [
    'corptools',
    'pinger',
    'securegroups',
    'charlink',
    'package_monitor',
    'allianceauth.services.modules.discord',
    'allianceauth.corputils',
    'celeryanalytics',
    'wizardmisc',
    'eveuniverse',
    'wizardskillfarm',
    'marketmanager',
    'blueprints',
    'wizardindustry',
    'discordproxy',
    'discordnotify',
    'miningtaxes',
    'django_celery_results',
    'moonmining',
]

#######################################
# Add any custom settings below here. #
#######################################
CHARLINK_IGNORE_APPS=["miningtaxes.admin"]
CELERYBEAT_SCHEDULE['package_monitor_update_distributions'] = {
    'task': 'package_monitor.tasks.update_distributions',
    'schedule': crontab(minute='*/60'),
}
PACKAGE_MONITOR_SHOW_ALL_PACKAGES = False

DISCORD_GUILD_ID = os.environ.get("DISCORD_GUILD_ID")
DISCORD_CALLBACK_URL = f"{SITE_URL}/discord/callback/"
DISCORD_APP_ID = os.environ.get("DISCORD_APP_ID")
DISCORD_APP_SECRET = os.environ.get("DISCORD_APP_SECRET")
DISCORD_BOT_TOKEN = os.environ.get("DISCORD_BOT_TOKEN")
DISCORD_SYNC_NAMES = False

DISCORDPROXY_HOST = os.environ.get("DISCORDPROXY_HOST")

CELERYBEAT_SCHEDULE['discord.update_all_usernames'] = {
    'task': 'discord.update_all_usernames',
    'schedule': crontab(minute='0', hour='*/12'),
}

JABBERBOT_URL = os.environ.get("JABBERBOT_URL")
HR_FORUM_WEBHOOK = os.environ.get("HR_FORUM_WEBHOOK")

## Settings for AA-MarketManager
# Market Orders
CELERYBEAT_SCHEDULE['marketmanager_fetch_public_market_orders'] = {
    'task': 'marketmanager.tasks.fetch_public_market_orders',
    'schedule': crontab(minute=0, hour='*/3'),
}
CELERYBEAT_SCHEDULE['marketmanager_fetch_all_character_orders'] = {
    'task': 'marketmanager.tasks.fetch_all_character_orders',
    'schedule': crontab(minute=0, hour='*/3'),
}
CELERYBEAT_SCHEDULE['marketmanager_fetch_all_corporation_orders'] = {
    'task': 'marketmanager.tasks.fetch_all_corporation_orders',
    'schedule': crontab(minute=0, hour='*/3'),
}
CELERYBEAT_SCHEDULE['marketmanager_fetch_all_structure_orders'] = {
    'task': 'marketmanager.tasks.fetch_all_structure_orders',
    'schedule': crontab(minute=0, hour='*/3'),
}
# Structure Information
CELERYBEAT_SCHEDULE['marketmanager_fetch_public_structures'] = {
    'task': 'marketmanager.tasks.fetch_public_structures',
    'schedule': crontab(minute=0, hour=4),
}
CELERYBEAT_SCHEDULE['marketmanager_update_private_structures'] = {
    'task': 'marketmanager.tasks.update_private_structures',
    'schedule': crontab(minute=0, hour=5),
}
CELERYBEAT_SCHEDULE['marketmanager_fetch_all_corporations_structures'] = {
    'task': 'marketmanager.tasks.fetch_all_corporations_structures',
    'schedule': crontab(minute=0, hour=6),
}
# Watch Configs
CELERYBEAT_SCHEDULE['marketmanager_update_managed_supply_configs'] = {
    'task': 'marketmanager.tasks.update_managed_supply_configs',
    'schedule': crontab(minute='0', hour='2'),
}
CELERYBEAT_SCHEDULE['marketmanager_run_all_watch_configs'] = {
    'task': 'marketmanager.tasks.run_all_watch_configs',
    'schedule': crontab(minute=0, hour='*/3'),
}
# Background Tasks
CELERYBEAT_SCHEDULE['marketmanager_update_all_type_statistics'] = {
    'task': 'marketmanager.tasks.update_all_type_statistics',
    'schedule': crontab(minute=0, hour=0, day_of_week=1),
}
# Cleanup
CELERYBEAT_SCHEDULE['marketmanager_garbage_collection'] = {
    'task': 'marketmanager.tasks.garbage_collection',
    'schedule': crontab(minute='0', hour=0),
}


## Settings for AA-Blueprints
CELERYBEAT_SCHEDULE['blueprints_update_all_blueprints'] = {
    'task': 'blueprints.tasks.update_all_blueprints',
    'schedule': crontab(minute=0, hour='*/3'),
}
CELERYBEAT_SCHEDULE['blueprints_update_all_industry_jobs'] = {
    'task': 'blueprints.tasks.update_all_industry_jobs',
    'schedule': crontab(minute=0, hour='*'),
}
CELERYBEAT_SCHEDULE['blueprints_update_all_locations'] = {
    'task': 'blueprints.tasks.update_all_locations',
    'schedule': crontab(minute=0, hour='*/12'),
}


## Settings for AA-MiningTaxes
CELERY_RESULT_BACKEND = 'django-db'
CELERY_CACHE_BACKEND = 'django-cache'

MININGTAXES_UNKNOWN_TAX_RATE = 0
MININGTAXES_ALWAYS_TAX_REFINED = True

CELERYBEAT_SCHEDULE['miningtaxes_update_daily'] = {
    'task': 'miningtaxes.tasks.update_daily',
    'schedule':  crontab(minute=0, hour='1'),
}

# Notifiy everyone of their current taxes on the second day of every month.
CELERYBEAT_SCHEDULE['miningtaxes_notifications'] = {
    'task': 'miningtaxes.tasks.notify_taxes_due',
    'schedule': crontab(0, 0, day_of_month='2'),
}


## Settings for AA-Moonmining
CELERYBEAT_SCHEDULE['moonmining_run_regular_updates'] = {
    'task': 'moonmining.tasks.run_regular_updates',
    'schedule': crontab(minute='*/10'),
}
CELERYBEAT_SCHEDULE['moonmining_run_report_updates'] = {
    'task': 'moonmining.tasks.run_report_updates',
    'schedule': crontab(minute=30, hour='*/1'),
}
CELERYBEAT_SCHEDULE['moonmining_run_value_updates'] = {
 'task': 'moonmining.tasks.run_calculated_properties_update',
 'schedule': crontab(minute=30, hour=3)
}


## Settings for corporationstats
CELERYBEAT_SCHEDULE['update_all_corpstats'] = {
    'task': 'allianceauth.corputils.tasks.update_all_corpstats',
    'schedule': crontab(day_of_month="1", hour=0, minute=32),
}
