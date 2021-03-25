#!/usr/bin/env python
# philipp.glira@gmail.com
# https://github.com/pglira

import os
import subprocess

with open('../README.md', 'wt') as f:
    f.write('# dmenu_scripts\n\n')

    dmenu_scripts = [name for name in os.listdir("..") if
                     name.startswith("dmenu_") and name.endswith(".py")]

    for script in dmenu_scripts:
        f.write('## {}\n\n'.format(script))
        helpscreen = subprocess.check_output(script + ' --help', shell=True, encoding='utf8')
        f.write('```\n' + helpscreen + '```\n\n')
