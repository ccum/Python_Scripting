#!/usr/bin/env python

import subprocess

try:
    output = subprocess.check_output(
        ['ls', '-la'],
        stderr = subprocess.STDOUT
    )
except OSError as err:
    print("Caugth OSError")
    output = err
except subprocess.CalledProcessError as err:
    print("Caugth CalledProcessError")
    output = err

print(output)

#chmod u+x execute_shell_commands_from_within_python.py 