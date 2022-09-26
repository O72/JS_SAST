import re
from formatting import Formatting
from colorama import Fore
from colorama import Style


class Rule:

    def __init__(self, filename, line, line_number):
        self.filename = filename
        self.line = line.strip()
        self.line_number = line_number
        self.secrets()

    def secrets(self):
        issue_type = "Possible hardcoded secrets"
        severity = 'High'
        confidence = 'Medium'
        color = Fore.YELLOW
        CWE = 'CWE-798: Use of Hard-coded Credentials (https://cwe.mitre.org/data/definitions/798.html)'
        location = f'{self.filename}#{self.line_number}'
        secret = re.search(r"(pas+wo?r?d|pass(phrase)?|pwd|token|secrete?)", self.line)
        if secret:
            Formatting(self.filename, self.line, self.line_number, issue_type, severity, confidence, CWE, location, color)


