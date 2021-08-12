from .base import *  # noqa isort:skip @UnusedWildImport

DEBUG = True

INSTALLED_APPS += ["debug_toolbar"]  # noqa: F405

MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")  # noqa: F405


# ==============================================================================
# EMAIL SETTINGS
# ==============================================================================
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
