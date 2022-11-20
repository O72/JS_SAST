import sys
import argparse
from JS_SAST.scanner import Scanner
import report.statistics as stats
import datetime
from colorama import Fore
from colorama import Style
import subprocess


def arg_parser():
    """
    This function gets the inputs from the user to use them in the tools
    :return: the Namespace of the input arguments.
    """
    parser = argparse.ArgumentParser(prog='js_sast.py', usage='%(prog)s [options]')
    options = parser.add_argument_group('Required options')
    options.add_argument('-p', '--path', action='store',
                         help='file: file or directory path to be scanned', required=True)
    parser.add_argument('-g', '--gosec', action='store', help='-g gosec, to run gosec on the target repository to scan'
                                                               'for vulnerabilities in Go source code.')
    parser.add_argument('-b', '--bandit', action='store', help='-b bandit, to run bandit on the target repository to '
                                                                'scan for vulnerabilities in Python source code.')

    if len(sys.argv) < 2:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()
    return args


def main():
    args = arg_parser()

    print(f"[INFO] Scan Started: {Fore.GREEN}{datetime.datetime.utcnow()}{Style.RESET_ALL}")

    path = args.path
    js_files = Scanner(path=path, filename=None).get_js_files()
    total_scan_lines = 0
    for file in js_files:
        line_number = Scanner(path=None, filename=file).scan_file()
        total_scan_lines += line_number

    stats.overall_stats(total_scan_lines)

    if args.gosec:
        subprocess.run(["gosec", f"{path}/..."], shell=False)
    if args.bandit:
        subprocess.run(["bandit", "-r", f"{path}"], shell=False)


if __name__ == '__main__':
    main()
