'''
# Example of use:
	python3 loadDb.py database

This file should require superuser privilages
'''

import os, sys
import re
import datetime

appName = str(sys.argv[1])
  

answer = input("You're about to wipe away whole database content and reconstruct database models with updated structure. The process is irreversible. If you know what you're doing type 'yes', else the operation will be aborted.\n")
if answer != 'yes':
	print("Operation aborted.\n")
	sys.exit(0)
#os.system('python3 manage.py flush --noinput')
os.system('rm db.sqlite3')
for f in os.listdir(appName + '/migrations'): #########################
	if f!='__init__.py':
		os.system('rm -rf ' + appName + '/migrations/{}'.format(str(f)) ) ########################
os.system('python3 manage.py makemigrations ' + appName)
os.system('python3 manage.py migrate')
print("Operation succeeded.")

''' 
#### Not sure if it's important, so I leave it be here ####

#proj_path = "/var/www/rrna/"
#proj_path = "/media/data1/orcan/" ################################
# This is so Django knows where to find stuff.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "riboswitches_app.settings")
#sys.path.append(proj_path)

# This is so my local_settings.py gets loaded.
os.chdir(proj_path)

# This is so models get loaded.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
'''