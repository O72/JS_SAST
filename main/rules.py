import re
from report.formatting import Format


class Rule:

    def __init__(self, filename, line, line_number):
        self.filename = filename
        self.line = line.strip()
        self.line_number = line_number
        self.secrets()
        self.sql_injection()
        self.open_redirect()
        self.weak_hash()
        self.eval_function()

    def secrets(self):
        issue_type = "Possible hardcoded secrets"
        severity = 'High'
        confidence = 'High'
        CWE = 'CWE-798: Use of Hard-coded Credentials (https://cwe.mitre.org/data/definitions/798.html)'
        description = "Learn More: (https://owasp.org/Top10/A07_2021-Identification_and_Authentication_Failures/)"
        location = f'{self.filename}#{self.line_number}'
        secret = re.search(r"((pas+wo?r?d|pass(phrase)?|pwd|token|secrete?).(?:=))", self.line, re.IGNORECASE)
        if secret:
            Format(self.filename, self.line, self.line_number, issue_type, severity, confidence, CWE, location, description)

    def sql_injection(self):
        issue_type = "Improper sanitization of SQL query"
        severity = 'Medium'
        confidence = 'High'
        CWE = 'CWE-89: Improper Neutralization of Special Elements used in an SQL Command (SQL Injection) (' \
              'https://cwe.mitre.org/data/definitions/89.html)'
        description = "Learn More: (https://owasp.org/Top10/A03_2021-Injection/)"
        location = f'{self.filename}#{self.line_number}'
        secret = re.search(r"(?:select|find|drop|create|delete|count|bulk|copy).*where.*?=.*?(req\.id|req\.query|req\.body|req\.param)", self.line, re.IGNORECASE)
        if secret:
            Format(self.filename, self.line, self.line_number, issue_type, severity, confidence, CWE, location, description)

    def open_redirect(self):
        issue_type = "Redirection to Untrusted Site"
        severity = 'Low'
        confidence = 'Low'
        CWE = "CWE-601: URL Redirection to Untrusted Site ('Open Redirect')(https://cwe.mitre.org/data/definitions/601.html)"
        description = "Learn More: (https://owasp.org/Top10/A04_2021-Insecure_Design/)"
        location = f'{self.filename}#{self.line_number}'
        secret = re.search(
            r"(res\.redirect\()", self.line, re.IGNORECASE)
        if secret:
            Format(self.filename, self.line, self.line_number, issue_type, severity, confidence, CWE, location, description)

    def weak_hash(self):
        issue_type = "Use of Weak Hash"
        severity = 'Low'
        confidence = 'Medium'
        CWE = "CWE-328: Use of Weak Hash (https://cwe.mitre.org/data/definitions/328.html)"
        description = "Learn More: (https://owasp.org/Top10/A02_2021-Cryptographic_Failures/)"
        location = f'{self.filename}#{self.line_number}'
        secret = re.search(
            r"(createHash\((?:'|\")md5(?:'|\")|createHash\((?:'|\")sha1(?:'|\"))", self.line, re.IGNORECASE)
        if secret:
            Format(self.filename, self.line, self.line_number, issue_type, severity, confidence, CWE, location, description)

    def eval_function(self):
        issue_type = "Eval Injection"
        severity = 'Low'
        confidence = 'Medium'
        CWE = "CWE-95: Improper Neutralization of Directives in Dynamically Evaluated Code ('Eval Injection') (" \
              "https://cwe.mitre.org/data/definitions/95.html) "
        description = "Learn More: (https://owasp.org/www-community/attacks/Direct_Dynamic_Code_Evaluation_Eval%20Injection)"
        location = f'{self.filename}#{self.line_number}'
        secret = re.search(
            r"(eval.\(*.*\))", self.line, re.IGNORECASE)
        if secret:
            Format(self.filename, self.line, self.line_number, issue_type, severity, confidence, CWE, location, description)


# switch the rules to be parsed through json file


# csrf https://owasp.org/Top10/A10_2021-Server-Side_Request_Forgery_%28SSRF%29/