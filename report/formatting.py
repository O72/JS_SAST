from colorama import Fore
from colorama import Style
import report.js_statistics as stats

class Format:

    def __init__(self, filename, line, line_number, issue_type, severity, confidence, CWE, location, description, remediation):
        self.filename = filename
        self.line = line
        self.line_number = line_number
        self.issue_type = issue_type
        self.severity = severity
        self.confidence = confidence
        self.CWE = CWE
        self.location = location
        self.description = description
        self.remediation = remediation
        if self.confidence == "High":
            stats.set_highs_by_confidence(1)
        if self.confidence == "Medium":
            stats.set_mediums_by_confidence(1)
        if self.confidence == "Low":
            stats.set_lows_by_confidence(1)
        if self.severity == "High":
            self.color = Fore.RED
            stats.set_highs_by_severity(1)
        if self.severity == "Medium":
            self.color = Fore.YELLOW
            stats.set_mediums_by_severity(1)
        if self.severity == "Low":
            stats.set_lows_by_severity(1)
            self.color = Fore.LIGHTBLUE_EX

        self.formatting()

    def formatting(self):

        print(f"~ {self.color}Rule Type: {self.issue_type} \n"
              f"  Severity: {self.severity} \n"
              f"  Confidence: {self.confidence} \n"
              f"  Location: {self.location} \n"
              f"  {self.CWE} \n"
              f"  {self.description} {Style.RESET_ALL}\n"
              f"  {Fore.GREEN}Remediation: {self.remediation} {Style.RESET_ALL} \n"
              f"      {self.line} \n"
              f"----------------------------------------------")
