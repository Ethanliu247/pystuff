# If you are worried, don't be
# This process if perfectly safe

# Although, it does require your password...

# All it does is install:
# QL (harmless information file)
# The QL shell (up to you how it's used)
# And aliases the shell so you can type 'ql' into Terminal and launch it

# That's ALL it does

print('Initializing...')

import os
import sys

home = os.path.expanduser('~')

try:
    print('Collecting files...')
    
    bp = open(home+'/.bash_profile', 'a+')
    shell = open('shell.py', 'r+')
    langf = open('ql.py', 'r+')
    changes = open('changelog.py', 'r+')

    os.system('mkdir -p /usr/bin/QL/')
    bp.write('alias ql="python3 /usr/bin/QL/shell.py"\n')

    iShell = open('/usr/bin/QL/shell.py', 'w+')
    iLang = open('/usr/bin/QL/ql.py', 'w+')
    iCl = open('/usr/bin/QL/changelog.py', 'w+')
    dCl = open(home+'/Desktop/changes.py', 'w+')
    
except FileNotFoundError as e:
    print(e)
    print('An error occurred during installation. Did you sudo?')
    sys.exit()
except PermissionError as e:
    print(e)
    print('Permission denied. Did you sudo?')
    sys.exit()

print('Writing files...')

iShell.write(
shell.read()
    )
iLang.write(
langf.read()
    )
iCl.write(
changes.read()
    )
dCl.write(
changes.read()
    )

print('Closing files...')

bp.close()
shell.close()
langf.close()
changes.close()
iShell.close()
iLang.close()
iCl.close()
dCl.close()

print('Installation successful!')
