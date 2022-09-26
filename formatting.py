import re
from colorama import Fore
from colorama import Style

class Formatting:

    def __init__(self, filename, line, line_number, issue_type, severity, confidence, CWE, location, color):
        self.filename = filename
        self.line = line
        self.line_number = line_number
        self.issue_type = issue_type
        self.severity = severity
        self.confidence = confidence
        self.CWE = CWE
        self.location = location
        self.color = color

        self.printer()

    def printer(self):

        print(f"~ {self.color}Rule Type: {self.issue_type} \n"
              f"  Severity: {self.severity} \n"
              f"  Confidence: {self.confidence} \n"
              f"  Location: {self.location} \n"
              f"  {self.CWE} {Style.RESET_ALL}\n"
              f"      {self.line} \n"
              f"----------------------------------------------")
