import sys
import argparse
from scanner import Scanner
import report.statistics as stats
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

    if len(sys.argv) < 2:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()
    return args


def main():
    args = arg_parser()

    print(f"[INFO] Scan Started: {Fore.GREEN}{datetime.datetime.utcnow()}{Style.RESET_ALL}")

    path = args.path[0]
    js_files = Scanner(path=path, filename=None).get_js_files()
    total_scan_lines = 0
    for file in js_files:
        line_number = Scanner(path=None, filename=file).scan_file()
        total_scan_lines += line_number

    stats.overall_stats(total_scan_lines)


if __name__ == '__main__':
    main()
