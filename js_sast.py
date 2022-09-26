import sys
import argparse
import scanner
import datetime
from colorama import Fore
from colorama import Style


def arg_parser():
    """
    This function gets the inputs from the user to use them in the tools
    :return: the Namespace of the input arguments.
    """
    parser = argparse.ArgumentParser(prog='js_sast.py', usage='%(prog)s [options]')
    options = parser.add_argument_group('Flag options', '')
    options.add_argument('-p', '--path', nargs=1,
                         help='file: file or directory path to be scanned')
    options.add_argument('-r', '--recursive', action='store_true', help='Recursively scan the directory')

    if len(sys.argv) < 2:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()
    return args


def main():
    args = arg_parser()

    print(f"[INFO] Scan Started: {Fore.GREEN}{datetime.datetime.utcnow()}{Style.RESET_ALL}")

    if args.recursive:
        path = args.path[0]
        js_files = scanner.get_js_files(path)

        for file in js_files:
            scanner.scan_file(file)


if __name__ == '__main__':
    main()
