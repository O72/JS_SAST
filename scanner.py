import glob
from rules import Rule
from colorama import Fore
from colorama import Style

def get_js_files(root_dir) -> list:
    js_files = []
    if root_dir.endswith("/") is False:
        # root_dir needs a trailing slash (i.e. /root/dir/)
        root_dir = ''.join([root_dir, '/'])

    for filename in glob.iglob(root_dir + '**/*.js', recursive=True):
        js_files.append(filename)
    if js_files is not None:
        print(f"{Fore.LIGHTMAGENTA_EX}Scan Results:{Style.RESET_ALL}")

    return js_files


def scan_file(filename):
    with open(filename, 'r') as f:
        current_file = f.readlines()
        line_number = 0

        for line in current_file:
            line_number += 1
            Rule(filename, line, line_number)
