#!/usr/bin/env python

import os
from pathlib import Path
import subprocess

# Deletes
# - django_home/*/migrations/*.py
# - django_home/*/*.sqlite3

estim_proj_home = Path(os.path.dirname(os.path.abspath(__file__))).parent
print(estim_proj_home, str(estim_proj_home))

for dir2nd_b in os.listdir(estim_proj_home):
    dir2nd = os.path.join(estim_proj_home, dir2nd_b)
    if os.path.isdir(dir2nd) and not dir2nd_b.startswith("."):
        # dir2nd may be a file.
        migration_dir = os.path.join(dir2nd, "migrations")
        # print("Check", migration_dir)
        if os.path.isdir(migration_dir):
            for cdir, fdirs_b, ffiles_b in os.walk(migration_dir):
                for ifile_b in ffiles_b:
                    filpath = os.path.join(cdir, ifile_b)
                    if (os.path.isfile(filpath) and
                            ifile_b.lower().endswith(".py") and
                            ifile_b.lower() != "__init__.py"):
                        os.remove(filpath)
                        print("Deleted migration-related file:", filpath)

        for file3rd_b in os.listdir(dir2nd):
            filpath = os.path.join(dir2nd, file3rd_b)
            if (os.path.isfile(filpath) and
                    file3rd_b.lower().endswith("sqlite3")):
                os.remove(filpath)
                print("Deleted sqlite file:", filpath)

# os.chdir(estim_proj_home)
#
# coms = (
#     [ "python", "./manage.py", "makemigrations" ],
#     [ "python", "./manage.py", "makemigrations", "appTMCS" ],
#     [ "python", "./manage.py", "makemigrations", "appMHoutBatch" ],
#
#     [ "python", "./manage.py", "migrate" ],
#     [ "python", "./manage.py", "migrate", "--database=tmcs" ],
#     [ "python", "./manage.py", "migrate", "--database=mhoutb" ],
#
# )
#
# for icom in coms:
#     print("--- Invoking :", " ".join(icom))
#     subprocess.run(icom)

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IAB_TsuruCoho2.settings')
# try:
#     from django.core.management import execute_from_command_line
# except ImportError as exc:
#     raise ImportError(
#         "Couldn't import Django. Are you sure it's installed and "
#         "available on your PYTHONPATH environment variable? Did you "
#         "forget to activate a virtual environment?"
#     ) from exc
# execute_from_command_line([ "./manage.py", "makemigrations" ])
