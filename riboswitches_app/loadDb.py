
import os, sys
import re
import datetime
  
#os.system('rm db.sqlite3')
for f in os.listdir('mainApp/migrations'): #########################
    if f!='__init__.py':
        os.system('rm mainApp/migrations/%s' % f) ########################
os.system('python manage.py makemigrations mainApp')
os.system('python manage.py migrate')


#proj_path = "/var/www/rrna/"
proj_path = "/media/data1/orcan/" ################################
# This is so Django knows where to find stuff.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orcan.settings")
sys.path.append(proj_path)

# This is so my local_settings.py gets loaded.
os.chdir(proj_path)

# This is so models get loaded.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from mainApp.models import Domain, Organism, Proteome, UniprotRelease