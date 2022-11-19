import glob
from main.rules import Rule
from colorama import Fore
from colorama import Style

class Scanner:

    def __init__(self, path, filename):

        self.path = path
        self.filename = filename
        self.line_number = 0

    def get_js_files(self) -> list:
        js_files = []
        if self.path.endswith("/") is False:
            # path needs a trailing slash (i.e. /root/dir/)
            self.path = ''.join([self.path, '/'])

        for filename in glob.iglob(self.path + '**/*.js', recursive=True):
            js_files.append(filename)
        if js_files is not None:
            print(f"{Fore.LIGHTMAGENTA_EX}Scan Results:{Style.RESET_ALL}")

        return js_files

    def scan_file(self):

        with open(self.filename, 'r') as f:
            current_file = f.readlines()
            for line in current_file:
                self.line_number += 1
                Rule(self.filename, line, self.line_number)
        return self.line_number
