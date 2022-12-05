import glob
from core.ruleset_engine import Rule
from colorama import Fore
from colorama import Style
import os

# This class is used to scan js files and look for instances matching rulesets.
class Scanner:

    def __init__(self, path, filename, rules=None):
        self.path = path
        self.filename = filename
        self.rules = rules
        self.line_number = 0

    def get_js_files(self) -> list:
        """
        This function is used to retrieve all of the js files in a given directory
        :return: a list of all of the js files within a repository
        """
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
        """
        This function applies the them to each of lines in a js file.
        :return: number of lines in a scanned file
        """
        if os.path.isdir(self.filename):
            return self.line_number
        with open(self.filename, 'r') as f:
            current_file = f.readlines()
            for line in current_file:
                self.line_number += 1
                Rule(self.filename, line, self.line_number, self.rules)
        return self.line_number
