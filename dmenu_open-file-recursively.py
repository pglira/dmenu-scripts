#!/usr/bin/env python
# philipp.glira@gmail.com
# https://github.com/pglira

import argparse
import os
import sys
import shutil
import pathlib
import subprocess


def parse_args(args_in):
    def dir_type(value):
        if not os.path.isdir(value):
            msg = 'Directory "{}" not found!'.format(value)
            raise argparse.ArgumentTypeError(msg)
        return value

    def program_type(value):
        if shutil.which(value) is None:
            msg = 'Program "{}" not found!'.format(value)
            raise argparse.ArgumentTypeError(msg)
        return value

    # Define own formatter which combines multiple formatters
    class Formatter(argparse.ArgumentDefaultsHelpFormatter,
        argparse.RawDescriptionHelpFormatter): pass

    scriptname = os.path.basename(__file__)
    description = 'Use dmenu to recursively search for a file in a search directory.'
    examples = []
    examples.append('{} -d "$HOME/Documents" -s "*.pdf" -p okular -o "-i -l 20 -p pdf:"'.format(
        scriptname))
    examples.append('{} -d "$HOME/Videos" -s "*.mp4" -p mpv -o "-i -l 20 -p videos:"'.format(
        scriptname))
    epilog = 'Examples:\n  ' + '\n  '.join(examples)
    parser = argparse.ArgumentParser(description=description,
        formatter_class=Formatter, epilog=epilog)
    parser._action_groups.pop()
    required = parser.add_argument_group('required arguments')
    optional = parser.add_argument_group('optional arguments')
    required.add_argument('-d', '--search-dir', help='Path to search directory', dest='search_dir',
        required=True, type=dir_type)
    required.add_argument('-s', '--search-pattern', help='Search pattern', dest='search_pattern',
        required=True, type=str)
    optional.add_argument('-p', '--program', help='Program to open file', dest='program',
        required=False, type=program_type, default='xdg-open')
    optional.add_argument('-o', '--dmenu-options', help='Options to pass to dmenu',
        dest='dmenu_options', required=False, type=str, default='')
    args = parser.parse_args(args_in)

    return args


def get_files(search_dir, search_pattern):
    matches = sorted(pathlib.Path(search_dir).rglob(search_pattern))
    files = [str(file) for file in matches]
    return files


def select_file(files, dmenu_options):
    if shutil.which('dmenu') is None:
        print('Error: "dmenu" not found on path!')
        sys.exit(1)
    input_string = '\n'.join(files) + '\n'
    command = ['dmenu'] + dmenu_options.split()
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stdin=subprocess.PIPE,
        encoding='utf8')
    selected_file = process.communicate(input_string)[0].rstrip()
    if process.returncode != 0:
        sys.exit(1)
    return (selected_file)


def open_file(file, program):
    if not os.path.isfile(file):
        print('File "{}" not found!'.format(file))
        sys.exit(1)
    process = subprocess.Popen([program, file], stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL)
    process.communicate()


def main(args_in):
    args = parse_args(args_in)
    files = get_files(args.search_dir, args.search_pattern)
    selected_file = select_file(files, args.dmenu_options)
    open_file(os.path.join(args.search_dir, selected_file), args.program)


if __name__ == '__main__':
    main(sys.argv[1:])
