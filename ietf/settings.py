# Copyright The IETF Trust 2007, All Rights Reserved

# Django settings for ietf project.
# BASE_DIR and "settings_local" are from
# http://code.djangoproject.com/wiki/SplitSettings

import os
try:
    import syslog
    syslog.openlog("datatracker", syslog.LOG_PID, syslog.LOG_USER)
except ImportError:
    pass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# a place to put ajax logs if necessary.
LOG_DIR = '/var/log/datatracker'

import sys
sys.path.append(os.path.abspath(BASE_DIR + "/.."))

import datetime

DEBUG = False
TEMPLATE_DEBUG = DEBUG

# Domain name of the IETF
IETF_DOMAIN = 'ietf.org'

ADMINS = (
    ('IETF Django Developers', 'django-project@' + IETF_DOMAIN),
    ('GMail Tracker Archive', 'ietf.tracker.archive+errors@gmail.com'),
    ('Henrik Levkowetz', 'henrik@levkowetz.com'),
    ('Robert Sparks', 'rjsparks@nostrum.com'),
    ('Ole Laursen', 'olau@iola.dk'),
    ('Ryan Cross', 'rcross@amsl.com'),
)

ALLOWED_HOSTS = [".ietf.org", ".ietf.org.", "209.208.19.216", "4.31.198.44", ]

# Server name of the tools server
TOOLS_SERVER = 'tools.' + IETF_DOMAIN

# Override this in the settings_local.py file:
SERVER_EMAIL = 'Django Server <django-project@' + TOOLS_SERVER + '>'

DEFAULT_FROM_EMAIL = 'IETF Secretariat <ietf-secretariat-reply@' + IETF_DOMAIN + '>'

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'NAME': 'ietf_utf8',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'ietf',
        #'PASSWORD': 'ietf',
        #'OPTIONS': {},
    },
#    'legacy': {
#        'NAME': 'ietf',
#        'ENGINE': 'django.db.backends.mysql',
#        'USER': 'ietf',
#        #'PASSWORD': 'ietf',
#    },
}

DATABASE_TEST_OPTIONS = {
    # Comment this out if your database doesn't support InnoDB
    'init_command': 'SET storage_engine=InnoDB',
}

# Local time zone for this installation. Choices can be found here:
# http://www.postgresql.org/docs/8.1/static/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
# although not all variations may be possible on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'PST8PDT'

# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
# http://blogs.law.harvard.edu/tech/stories/storyReader$15
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

USE_TZ = False

MEDIA_URL = '//www.ietf.org/'

STATIC_URL = "/"
STATIC_ROOT = os.path.abspath(BASE_DIR + "/../static/")

WSGI_APPLICATION = "ietf.wsgi.application"

AUTHENTICATION_BACKENDS = ( 'django.contrib.auth.backends.ModelBackend', )

#DATABASE_ROUTERS = ["ietf.legacy_router.LegacyRouter"]

# ------------------------------------------------------------------------
# Django/Python Logging Framework Modifications

# enable HTML error emails
from django.utils.log import DEFAULT_LOGGING
LOGGING = DEFAULT_LOGGING.copy()
LOGGING['handlers']['mail_admins']['include_html'] = True

# Filter out "Invalid HTTP_HOST" emails
# Based on http://www.tiwoc.de/blog/2013/03/django-prevent-email-notification-on-suspiciousoperation/
from django.core.exceptions import SuspiciousOperation
def skip_suspicious_operations(record):
    if record.exc_info:
        exc_value = record.exc_info[1]
        if isinstance(exc_value, SuspiciousOperation):
            return False
    return True
LOGGING['filters']['skip_suspicious_operations'] = {
    '()': 'django.utils.log.CallbackFilter',
    'callback': skip_suspicious_operations,
}
LOGGING['handlers']['mail_admins']['filters'] += [ 'skip_suspicious_operations' ]
# Filter out UreadablePostError:
from django.http import UnreadablePostError
def skip_unreadable_post(record):
    if record.exc_info:
        exc_type, exc_value = record.exc_info[:2]
        if isinstance(exc_value, UnreadablePostError):
            return False
    return True
LOGGING['filters']['skip_unreadable_posts'] = {
    '()': 'django.utils.log.CallbackFilter',
    'callback': skip_unreadable_post,
}
LOGGING['handlers']['mail_admins']['filters'] += [ 'skip_unreadable_posts' ]




# End logging
# ------------------------------------------------------------------------

#SESSION_COOKIE_AGE = 60 * 60 * 24 * 7 * 2 # Age of cookie, in seconds: 2 weeks.
SESSION_COOKIE_AGE = 60 * 60 * 24 * 365 * 50 # Age of cookie, in seconds: 50 years

SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
    'ietf.dbtemplate.template.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'ietf.middleware.SQLLogMiddleware',
    'ietf.middleware.SMTPExceptionMiddleware',
    'ietf.middleware.RedirectTrailingPeriod',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'ietf.middleware.UnicodeNfkcNormalization',
)

ROOT_URLCONF = 'ietf.urls'

TEMPLATE_DIRS = (
    BASE_DIR + "/templates",
    BASE_DIR + "/secr/templates",
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.contrib.messages.context_processors.messages',
    'ietf.context_processors.server_mode',
    'ietf.context_processors.revision_info',
    'ietf.secr.context_processors.secr_revision_info',
    'ietf.secr.context_processors.static',
    'ietf.context_processors.rfcdiff_base_url',
)

INSTALLED_APPS = (
    # Django apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.humanize',
    'django.contrib.messages',
    # External apps 
    'bootstrap3',
    'form_utils',
    'tastypie',
    'widget_tweaks',
    # IETF apps
    'ietf.api',
    'ietf.community',
    'ietf.dbtemplate',
    'ietf.doc',
    'ietf.group',
    'ietf.idindex',
    'ietf.iesg',
    'ietf.ietfauth',
    'ietf.ipr',
    'ietf.liaisons',
    'ietf.mailinglists',
    'ietf.meeting',
    'ietf.message',
    'ietf.name',
    'ietf.nomcom',
    'ietf.person',
    'ietf.redirects',
    'ietf.release',
    'ietf.submit',
    'ietf.sync',
    'ietf.utils',
    'ietf.codematch',
    'ietf.codematch.matches',
    'ietf.codematch.requests',
    # IETF Secretariat apps
    'ietf.secr.announcement',
    'ietf.secr.areas',
    'ietf.secr.drafts',
    'ietf.secr.groups',
    'ietf.secr.meetings',
    'ietf.secr.proceedings',
    'ietf.secr.roles',
    'ietf.secr.rolodex',
    'ietf.secr.sreq',
    'ietf.secr.telechat',
)

# Settings for django-bootstrap3
# See http://django-bootstrap3.readthedocs.org/en/latest/settings.html
BOOTSTRAP3 = {
    # Label class to use in horizontal forms
    'horizontal_label_class': 'col-md-2',

    # Field class to use in horiozntal forms
    'horizontal_field_class': 'col-md-10',

    # Set HTML required attribute on required fields
    'set_required': True,

    # Set placeholder attributes to label if no placeholder is provided
    'set_placeholder': False,

    # Class to indicate required
    'form_required_class': 'bootstrap3-required',

    # Class to indicate error
    'form_error_class': 'bootstrap3-error',
}

INTERNAL_IPS = (
# AMS servers
	'64.170.98.32',
	'64.170.98.86',

# local
        '127.0.0.1',
        '::1',
)

# no slash at end
IDTRACKER_BASE_URL = "https://datatracker.ietf.org"
RFCDIFF_BASE_URL = "https://www.ietf.org/rfcdiff"

# Valid values:
# 'production', 'test', 'development'
# Override this in settings_local.py if it's not true
SERVER_MODE = 'production'

# The name of the method to use to invoke the test suite
TEST_RUNNER = 'ietf.utils.test_runner.IetfTestRunner'

# Fixtures which will be loaded before testing starts
GLOBAL_TEST_FIXTURES = [ 'names','ietf.utils.test_data.make_immutable_base_data' ]

TEST_DIFF_FAILURE_DIR = "/tmp/test/failure/"

TEST_GHOSTDRIVER_LOG_PATH = "ghostdriver.log"

TEST_MATERIALS_DIR = "tmp-meeting-materials-dir"

TEST_BLUESHEET_DIR = "tmp-bluesheet-dir"

# These are regexes
TEST_URL_COVERAGE_EXCLUDE = [
    "^\^admin/",
]

# Tese are filename globs
TEST_CODE_COVERAGE_EXCLUDE = [
    "*/tests*",
    "*/admin.py",
    "*/migrations/*",
    "ietf/settings*",
    "ietf/utils/test_runner.py",
]

TEST_COVERAGE_MASTER_FILE = os.path.join(BASE_DIR, "../release-coverage.json")
TEST_COVERAGE_LATEST_FILE = os.path.join(BASE_DIR, "../latest-coverage.json")

TEST_CODE_COVERAGE_CHECKER = None
if SERVER_MODE != 'production':
    import coverage
    TEST_CODE_COVERAGE_CHECKER = coverage.coverage(source=[ BASE_DIR ], cover_pylib=False, omit=TEST_CODE_COVERAGE_EXCLUDE)
    if len(TEST_CODE_COVERAGE_CHECKER.collector._collectors) == 0:
        TEST_CODE_COVERAGE_CHECKER.start()

TEST_CODE_COVERAGE_REPORT_PATH = "static/coverage/"
TEST_CODE_COVERAGE_REPORT_URL = os.path.join(STATIC_URL, TEST_CODE_COVERAGE_REPORT_PATH, "index.html")
TEST_CODE_COVERAGE_REPORT_DIR = os.path.join(STATIC_ROOT, TEST_CODE_COVERAGE_REPORT_PATH)
TEST_CODE_COVERAGE_REPORT_FILE = os.path.join(TEST_CODE_COVERAGE_REPORT_DIR, "index.html")

# WG Chair configuration
MAX_WG_DELEGATES = 3

DATE_FORMAT = "Y-m-d"
DATETIME_FORMAT = "Y-m-d H:i T"

# Override this in settings_local.py if needed
# *_PATH variables ends with a slash/ .
DOCUMENT_PATH_PATTERN = '/a/www/ietf-ftp/{doc.type_id}/'
INTERNET_DRAFT_PATH = '/a/www/ietf-ftp/internet-drafts/'
INTERNET_DRAFT_PDF_PATH = '/a/www/ietf-datatracker/pdf/'
RFC_PATH = '/a/www/ietf-ftp/rfc/'
CHARTER_PATH = '/a/www/ietf-ftp/charter/'
CONFLICT_REVIEW_PATH = '/a/www/ietf-ftp/conflict-reviews'
STATUS_CHANGE_PATH = '/a/www/ietf-ftp/status-changes'
AGENDA_PATH = '/a/www/www6s/proceedings/'
IPR_DOCUMENT_PATH = '/a/www/ietf-ftp/ietf/IPR/'
IESG_TASK_FILE = '/a/www/www6/iesg/internal/task.txt'
IESG_ROLL_CALL_FILE = '/a/www/www6/iesg/internal/rollcall.txt'
IESG_MINUTES_FILE = '/a/www/www6/iesg/internal/minutes.txt'
IESG_WG_EVALUATION_DIR = "/a/www/www6/iesg/evaluation"
INTERNET_DRAFT_ARCHIVE_DIR = '/a/www/www6s/draft-archive'
MEETING_RECORDINGS_DIR = '/a/www/audio'

# Mailing list info URL for lists hosted on the IETF servers
MAILING_LIST_INFO_URL = "https://www.ietf.org/mailman/listinfo/%(list_addr)s"

# Ideally, more of these would be local -- but since we don't support
# versions right now, we'll point to external websites
DOC_HREFS = {
    "charter": "https://www.ietf.org/charter/{doc.name}-{doc.rev}.txt",
    "draft": "https://www.ietf.org/archive/id/{doc.name}-{doc.rev}.txt",
    "slides": "https://www.ietf.org/slides/{doc.name}-{doc.rev}",
    "conflrev": "https://www.ietf.org/cr/{doc.name}-{doc.rev}.txt",
    "statchg": "https://www.ietf.org/sc/{doc.name}-{doc.rev}.txt",
}

MEETING_DOC_HREFS = {
    "agenda": "/meeting/{meeting}/agenda/{doc.group.acronym}/",
    "minutes": "https://www.ietf.org/proceedings/{meeting}/minutes/{doc.external_url}",
    "slides": "https://www.ietf.org/proceedings/{meeting}/slides/{doc.external_url}",
    "recording": "{doc.external_url}",
}

# Override this in settings_local.py if needed
CACHE_MIDDLEWARE_SECONDS = 300
CACHE_MIDDLEWARE_KEY_PREFIX = ''

# The default with no CACHES setting is 'django.core.cache.backends.locmem.LocMemCache'
# This setting is possibly overridden further down, after the import of settings_local
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

IPR_EMAIL_TO = 'ietf-ipr@ietf.org'
DOC_APPROVAL_EMAIL_CC = ["RFC Editor <rfc-editor@rfc-editor.org>", ]

IANA_EVAL_EMAIL = "drafts-eval@icann.org"
IANA_APPROVE_EMAIL = "drafts-approval@icann.org"

# Put real password in settings_local.py
IANA_SYNC_PASSWORD = "secret"
IANA_SYNC_CHANGES_URL = "https://datatracker.iana.org:4443/data-tracker/changes"
IANA_SYNC_PROTOCOLS_URL = "https://www.iana.org/protocols/"

RFC_TEXT_RSYNC_SOURCE="ftp.rfc-editor.org::rfcs-text-only"

RFC_EDITOR_SYNC_PASSWORD="secret"
RFC_EDITOR_SYNC_NOTIFICATION_URL = "https://www.rfc-editor.org/parser/parser.php"
RFC_EDITOR_QUEUE_URL = "https://www.rfc-editor.org/queue2.xml"
RFC_EDITOR_INDEX_URL = "https://www.rfc-editor.org/rfc/rfc-index.xml"

# Liaison Statement Tool settings
LIAISON_UNIVERSAL_FROM = 'Liaison Statement Management Tool <lsmt@' + IETF_DOMAIN + '>'
LIAISON_ATTACH_PATH = '/a/www/ietf-datatracker/documents/LIAISON/'
LIAISON_ATTACH_URL = '/documents/LIAISON/'

# NomCom Tool settings
ROLODEX_URL = ""
NOMCOM_PUBLIC_KEYS_DIR = '/a/www/nomcom/public_keys/'
NOMCOM_FROM_EMAIL = 'nomcom-chair@ietf.org'
NOMCOM_ADMIN_EMAIL = DEFAULT_FROM_EMAIL
OPENSSL_COMMAND = '/usr/bin/openssl'
DAYS_TO_EXPIRE_NOMINATION_LINK = ''
DEFAULT_FEEDBACK_TYPE = 'offtopic'
NOMINEE_FEEDBACK_TYPES = ['comment', 'questio', 'nomina']

# ID Submission Tool settings
IDSUBMIT_FROM_EMAIL = 'IETF I-D Submission Tool <idsubmission@ietf.org>'
IDSUBMIT_TO_EMAIL = 'internet-drafts@ietf.org'
IDSUBMIT_ANNOUNCE_FROM_EMAIL = 'internet-drafts@ietf.org'
IDSUBMIT_ANNOUNCE_LIST_EMAIL = 'i-d-announce@ietf.org'

# Days from meeting to day of cut off dates on submit -- cutoff_time_utc is added to this
IDSUBMIT_DEFAULT_CUTOFF_DAY_OFFSET_00 = 13
IDSUBMIT_DEFAULT_CUTOFF_DAY_OFFSET_01 = 13
IDSUBMIT_DEFAULT_CUTOFF_TIME_UTC = datetime.timedelta(hours=23, minutes=59, seconds=59)
IDSUBMIT_DEFAULT_CUTOFF_WARNING_DAYS = datetime.timedelta(days=21)

MEETING_MATERIALS_SUBMISSION_START_DAYS = -90
MEETING_MATERIALS_SUBMISSION_CUTOFF_DAYS = 26
MEETING_MATERIALS_SUBMISSION_CORRECTION_DAYS = 50

INTERNET_DRAFT_DAYS_TO_EXPIRE = 185

IDSUBMIT_REPOSITORY_PATH = INTERNET_DRAFT_PATH
IDSUBMIT_STAGING_PATH = '/a/www/www6s/staging/'
IDSUBMIT_STAGING_URL = '//www.ietf.org/staging/'
IDSUBMIT_IDNITS_BINARY = '/a/www/ietf-datatracker/scripts/idnits'

IDSUBMIT_MAX_PLAIN_DRAFT_SIZE = 6291456  # Max size of the txt draft in bytes

IDSUBMIT_MAX_DAILY_SAME_DRAFT_NAME = 20
IDSUBMIT_MAX_DAILY_SAME_DRAFT_NAME_SIZE = 50 # in MB
IDSUBMIT_MAX_DAILY_SAME_SUBMITTER = 50
IDSUBMIT_MAX_DAILY_SAME_SUBMITTER_SIZE = 150 # in MB
IDSUBMIT_MAX_DAILY_SAME_GROUP = 150
IDSUBMIT_MAX_DAILY_SAME_GROUP_SIZE = 450 # in MB
IDSUBMIT_MAX_DAILY_SUBMISSIONS = 1000
IDSUBMIT_MAX_DAILY_SUBMISSIONS_SIZE = 2000 # in MB

DOT_BINARY = '/usr/bin/dot'
UNFLATTEN_BINARY= '/usr/bin/unflatten'
PS2PDF_BINARY = '/usr/bin/ps2pdf'
RSYNC_BINARY = '/usr/bin/rsync'

# Account settings
DAYS_TO_EXPIRE_REGISTRATION_LINK = 3
HTPASSWD_COMMAND = "/usr/bin/htpasswd2"
HTPASSWD_FILE = "/www/htpasswd"

# Generation of bibxml files for xml2rfc
BIBXML_BASE_PATH = '/a/www/ietf-ftp/xml2rfc'

# Timezone files for iCalendar
TZDATA_ICS_PATH = BASE_DIR + '/../vzic/zoneinfo/'
CHANGELOG_PATH =  BASE_DIR + '/../changelog'

SECR_BLUE_SHEET_PATH = '/a/www/ietf-datatracker/documents/blue_sheet.rtf'
SECR_BLUE_SHEET_URL = '//datatracker.ietf.org/documents/blue_sheet.rtf'
SECR_INTERIM_LISTING_DIR = '/a/www/www6/meeting/interim'
SECR_MAX_UPLOAD_SIZE = 40960000
SECR_PROCEEDINGS_DIR = '/a/www/www6s/proceedings/'
SECR_STATIC_URL = '/secretariat/'
SECR_PPT2PDF_COMMAND = ['/usr/bin/goffice','--headless','--convert-to','pdf','--outdir']

USE_ETAGS=True

PRODUCTION_TIMEZONE = "America/Los_Angeles"

PYFLAKES_DEFAULT_ARGS= ["ietf", ]
VULTURE_DEFAULT_ARGS= ["ietf", ]

# Automatic Scheduling
#
# how much to login while running, bigger numbers make it more verbose.
BADNESS_CALC_LOG   = 0
#
# these penalties affect the calculation of how bad the assignments are.
BADNESS_UNPLACED   = 1000000

# following four are used only during migrations to setup up ConstraintName
# and penalties are taken from the database afterwards.
BADNESS_BETHERE    = 200000
BADNESS_CONFLICT_1 = 100000
BADNESS_CONFLICT_2 = 10000
BADNESS_CONFLICT_3 = 1000

BADNESS_TOOSMALL_50  = 5000
BADNESS_TOOSMALL_100 = 50000
BADNESS_TOOBIG     = 100
BADNESS_MUCHTOOBIG = 500

# do not run SELENIUM tests by default
SELENIUM_TESTS = False
SELENIUM_TESTS_ONLY = False

# Domain which hosts draft and wg alias lists
DRAFT_ALIAS_DOMAIN = IETF_DOMAIN
GROUP_ALIAS_DOMAIN = IETF_DOMAIN

# Path to the email alias lists.  Used by ietf.utils.aliases
DRAFT_ALIASES_PATH = "/a/postfix/draft-aliases"
DRAFT_VIRTUAL_PATH = "/a/postfix/draft-virtual"

# Set zdebug apps in DEV_APPS settings_local
DEV_APPS = ()
DRAFT_VIRTUAL_DOMAIN = "virtual.ietf.org"

GROUP_ALIASES_PATH = "/a/postfix/group-aliases"
GROUP_VIRTUAL_PATH = "/a/postfix/group-virtual"
GROUP_VIRTUAL_DOMAIN = "virtual.ietf.org"

POSTCONFIRM_PATH   = "/a/postconfirm/test-wrapper"

USER_PREFERENCE_DEFAULTS = {
    "expires_soon"  : "14",
    "new_enough"    : "14",
    "full_draft"    : "off",
    "left_menu"     : "on",
}


# Put the production SECRET_KEY in settings_local.py, and also any other
# sensitive or site-specific changes.  DO NOT commit settings_local.py to svn.
from settings_local import *            # pyflakes:ignore

# Add DEV_APPS to INSTALLED_APPS
INSTALLED_APPS += DEV_APPS

# We provide a secret key only for test and development modes.  It's
# absolutely vital that django fails to start in production mode unless a
# secret key has been provided elsewhere, not in this file which is
# publicly available, for instance from the source repository.
if SERVER_MODE != 'production':
    # stomp out the cached template loader, it's annoying
    TEMPLATE_LOADERS = tuple(l for e in TEMPLATE_LOADERS for l in (e[1] if isinstance(e, tuple) and "cached.Loader" in e[0] else (e,)))

    CACHES = {
         'default': {
             'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
         }
    }
    if 'SECRET_KEY' not in locals():
        SECRET_KEY = 'PDwXboUq!=hPjnrtG2=ge#N$Dwy+wn@uivrugwpic8mxyPfHka'
    ALLOWED_HOSTS = ['*',]