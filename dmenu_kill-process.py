#!/usr/bin/env python
# philipp.glira@gmail.com
# https://github.com/pglira

import argparse
import os
import sys
import shutil
import subprocess
import signal


def parse_args(args_in):
    # Define own formatter which combines multiple formatters
    class Formatter(argparse.ArgumentDefaultsHelpFormatter,
        argparse.RawDescriptionHelpFormatter): pass

    scriptname = os.path.basename(__file__)
    description = 'Use dmenu to kill a running process.'
    examples = []
    examples.append('{}'.format(scriptname))
    epilog = 'Examples:\n  ' + '\n  '.join(examples)
    parser = argparse.ArgumentParser(description=description, formatter_class=Formatter,
        epilog=epilog)
    parser._action_groups.pop()
    # required = parser.add_argument_group('required arguments')
    optional = parser.add_argument_group('optional arguments')
    optional.add_argument('-o', '--dmenu-options', help='Options to pass to dmenu',
        dest='dmenu_options', required=False, type=str, default='')
    args = parser.parse_args(args_in)

    return args


def get_processes():
    processes = subprocess.run(['ps', 'ax', '--user', os.getlogin(), '-F'], stdout=subprocess.PIPE,
        encoding='utf8').stdout.splitlines()
    return processes


def select_process(processes, dmenu_options):
    if shutil.which('dmenu') is None:
        print('Error: "dmenu" not found on path!')
        sys.exit(1)
    input_string = '\n'.join(processes) + '\n'
    command = ['dmenu'] + dmenu_options.split()
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stdin=subprocess.PIPE,
        encoding='utf8')
    selected_process = process.communicate(input_string)[0].rstrip()
    if process.returncode != 0:
        sys.exit(1)
    try:
        selected_process_pid = int(selected_process.split()[1])
    except:  # e.g. if first line is selected
        sys.exit(1)
    return selected_process_pid


def kill_process(pid):
    os.kill(pid, signal.SIGKILL)


def main(args_in):
    args = parse_args(args_in)
    processes = get_processes()
    selected_process_pid = select_process(processes, args.dmenu_options)
    kill_process(selected_process_pid)


if __name__ == '__main__':
    main(sys.argv[1:])
