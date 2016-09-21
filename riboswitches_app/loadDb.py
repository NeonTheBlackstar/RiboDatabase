'''
# Example of use:
	python3 loadDb.py database

This file should require superuser privilages
'''

import os
import sys
import re
import datetime

appName = str(sys.argv[1])
  
answer = input("You're about to wipe away whole database content and reconstruct database models with updated structure. The process is irreversible. If you know what you're doing type 'yes', else the operation will be aborted.\n")
if answer != 'yes':
	print("Operation aborted.\n")
	sys.exit(0)
os.system('rm db.sqlite3')
for f in os.listdir(appName + '/migrations'): #########################
	if f!='__init__.py':
		os.system('rm -rf ' + appName + '/migrations/{}'.format(str(f)) ) ########################
os.system('python3 manage.py makemigrations ' + appName)
os.system('python3 manage.py migrate')
print("Operation succeeded.")