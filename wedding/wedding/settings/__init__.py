import os

"""
This module attempts to find settings in two ways:

1. Via an environmental variable: ``DJANGO_RUNTIME_ENVIRONMENT`` which should be
one of the following: "dev", "staging", or "production". If the variable is not
set, the wedding project will default to "dev"

2. Via a ``local_settings.py`` file, placed in this directory. Under no
circumstances should this file be versioned. It is solely to override settings
for a specific environment outside of the dev/staging/production divide.

Note that when importing files of type 1 or 2, four special variables may
may be defined there that will be handled specially:

    ``TEMPLATE_DIRS_ENV_ADDITIONS``
    ``INSTALLED_APPS_ENV_ADDITIONS``
    ``TEMPLATE_CONTEXT_PROCESSORS_ENV_ADDITIONS``
    ``MIDDLEWARE_CLASSES_ENV_ADDITIONS``

These are *appended* to the base setting they refer to (e.g.``TEMPLATE_DIRS``)
rather than replacing them. (NB: These base settings are all iterables.) This
allows you to--for example--add some additional apps to be installed without
replacing all the base ones.

If you want to define some settings that are common for all environments, you
should do so in the ``base.py`` module in this directory.

"""


# Import base settings
base =  __import__('wedding.settings.base', {}, {}, ['base'], -1)
for setting in dir(base):
    if setting == setting.upper():
        locals().update({setting: getattr(base, setting)})

allowed_envs = ('dev', 'staging', 'production')
runtime_env = os.environ.get('DJANGO_RUNTIME_ENVIRONMENT', 'dev')
if not runtime_env in allowed_envs:
    from django.core.exceptions import ImproperlyConfigured
    raise ImproperlyConfigured((
        "The DJANGO_RUNTIME_ENVIRONMENT variable is not specified for the "
        "current host. Allowed values: %s"
    ) % ", ".join(list(allowed_envs)))

try:
    environment = __import__(
        'wedding.settings.%s' % runtime_env,
        globals(),
        locals(),
        [runtime_env],
        -1
    )
except ImportError:
    pass
else:
    for setting in dir(environment):
        if setting.isupper():
            if setting.endswith("_ENV_ADDITIONS"):
                setting_to_append_to = setting.replace("_ENV_ADDITIONS", "")
                local_setting = locals().get(setting_to_append_to)
                env_setting = getattr(environment, setting)
                if setting_to_append_to:
                    locals().update({
                        setting_to_append_to: local_setting + env_setting
                    })
                else:
                    locals().update({
                        setting_to_append_to: env_setting
                    })
            else:
                locals().update({setting: getattr(environment, setting)})


# A final override point for settings that don't need to be versioned.
try:
    from local_settings import *
except ImportError:
    pass
else:
    try:
        TEMPLATE_DIRS = TEMPLATE_DIRS + TEMPLATE_DIRS_ENV_ADDITIONS
    except NameError:
        pass
    try:
        INSTALLED_APPS = INSTALLED_APPS + INSTALLED_APPS_ENV_ADDITIONS
    except NameError:
        pass
    try:
        TEMPLATE_CONTEXT_PROCESSORS += TEMPLATE_CONTEXT_PROCESSORS_ENV_ADDITIONS
    except NameError:
        pass
    try:
        MIDDLEWARE_CLASSES += MIDDLEWARE_CLASSES_ENV_ADDITIONS
    except NameError:
        pass