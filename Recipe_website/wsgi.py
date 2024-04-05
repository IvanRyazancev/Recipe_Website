# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
import os
import sys

from dotenv import load_dotenv

project_folder = os.path.expanduser('~/Recipe_Website') # adjust as appropriate
load_dotenv(os.path.join(project_folder, '.env'))

## assuming your django settings file is at '/home/Ryazancev/mysite/mysite/settings.py'
## and your manage.py is is at '/home/Ryazancev/mysite/manage.py'
path = '/home/Ryazancev/Recipe_Website'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'Recipe_website.settings'

## then:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()