import sys
import argparse
from core.scanner import Scanner
import report.js_statistics as stats
import datetime
from colorama import Fore
from colorama import Style
import subprocess
import git


def arg_parser():
    """
    This function gets the inputs from the user to use them in the tools
    :return: the Namespace of the input arguments.
    """
    parser = argparse.ArgumentParser(prog='js_sast.py', usage='%(prog)s [options]')
    options = parser.add_argument_group('Argument options')
    options.add_argument('-p', '--path', action='store',
                         help='file: file or directory path to be scanned')
    options.add_argument('-g', '--gosec', action='store', help='-g gosec, to run gosec on the target repository to scan'
                                                               'for vulnerabilities in Go source code.')
    options.add_argument('-b', '--bandit', action='store', help='-b bandit, to run bandit on the target repository to '
                                                                'scan for vulnerabilities in Python source code.')
    options.add_argument('-c', '--clone', action='store', help='-c https://github.com/O72/JS_SAST.git, to clone remote'
                                                              'repository to the current directory to be scanned')

    if len(sys.argv) < 2:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()
    return args


def main():
    args = arg_parser()

    print(f"[INFO] Scan Started: {Fore.GREEN}{datetime.datetime.utcnow()}{Style.RESET_ALL}")

    if args.clone:
        repo = args.clone.split("/")[-1].split(".")[0]
        git.Repo.clone_from(f'{args.clone}', f'{repo}')

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
