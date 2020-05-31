import os

import dj_database_url

from .settings import *

DATABASES = {
    "default": dj_database_url.config(
        default="sqlite:///" + os.path.join(BASE_DIR, "db.sqlite3")
    )
}

DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = [os.environ.get("ALLOWED_HOSTS"), "localhost"]
STATIC_ROOT = os.path.join(BASE_DIR, "static")
# SECRET_KEY = os.environ.get("SECRET_KEY")
SECRET_KEY = "(q1_p3t-7%l)i(1$@#s3g)&#@4#9)0r@^()y+ip8ffa^ua#ia$"

SITE_ID = 1
