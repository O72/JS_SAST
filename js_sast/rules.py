import re
from report.formatting import Format


class Rule:

    def __init__(self, filename, line, line_number):
        self.filename = filename
        self.line = line.strip()
        self.line_number = line_number
        self.secrets()
        self.sql_injection()
        self.xpath_injection()
        self.open_redirect()
        self.weak_hash()
        self.weak_cipher()
        self.eval_function()
        self.settimeout_function()
        self.logging_vulnerabilities()
        self.insecure_randomness()
        # change it to json or yaml and try to find an instance where json or yaml is an issue with rulesets

    def secrets(self):
        issue_type = "Hardcoded Secrets"
        severity = 'High'
        confidence = 'High'
        CWE = 'CWE-798: Use of Hard-coded Credentials (https://cwe.mitre.org/data/definitions/798.html)'
        description = "Learn More: (https://owasp.org/Top10/A02_2021-Cryptographic_Failures/)"
        remediation = "Remove hard-coded credentials, such as passwords and tokens from source code. \n" \
                      "Alternatively, store them in configuration files or environment variables \n" \
                      "If possible, store them in a secure location with restricted access, such as a vault. "
        location = f'{self.filename}#{self.line_number}'
        issue = re.search(r"((pas+wo?r?d|pass(phrase)?|pwd|token|secret?|cred?).(= ('|\"))|"
                          r"(pas+wo?r?d|pass(phrase)?|pwd|token|secret?|cred?)(: ('|\")))", self.line, re.IGNORECASE)
        if issue:
            Format(self.filename, self.line, self.line_number, issue_type, severity, confidence, CWE, location,
                   description, remediation)

    def sql_injection(self):
        issue_type = "Improper Sanitization of SQL Query"
        severity = 'Medium'
        confidence = 'Medium'
        CWE = 'CWE-89: Improper Neutralization of Special Elements used in an SQL Command (SQL Injection) (' \
              'https://cwe.mitre.org/data/definitions/89.html)'
        description = "Learn More: (https://owasp.org/Top10/A03_2021-Injection/)"
        remediation = ""
        location = f'{self.filename}#{self.line_number}'
        issue = re.search(
            r"(?:select|find|drop|create|delete|count|bulk|copy).*where.*?=.*?(req\.id|req\.query|req\.body|req\.param)",
            self.line, re.IGNORECASE)
        if issue:
            Format(self.filename, self.line, self.line_number, issue_type, severity, confidence, CWE, location,
                   description, remediation)

    def xpath_injection(self):
        issue_type = "Improper Neutralization of Data within XPath Expressions ('XPath Injection')"
        severity = 'Medium'
        confidence = 'Medium'
        CWE = "CWE-643: Improper Neutralization of Data within XPath Expressions ('XPath Injection') (https://cwe.mitre.org/data/definitions/643.html)"
        description = "Learn More: (https://owasp.org/Top10/A03_2021-Injection/)"
        remediation = ""
        location = f'{self.filename}#{self.line_number}'
        issue = re.search(
            r"(xpath.parse\((?:\'|\").+(\+))", self.line, re.IGNORECASE)
        if issue:
            Format(self.filename, self.line, self.line_number, issue_type, severity, confidence, CWE, location,
                   description, remediation)

    def open_redirect(self):
        issue_type = "Redirection to Untrusted Site"
        severity = 'Low'
        confidence = 'Medium'
        CWE = "CWE-601: URL Redirection to Untrusted Site ('Open Redirect')(https://cwe.mitre.org/data/definitions/601.html)"
        description = "Learn More: (https://owasp.org/Top10/A01_2021-Broken_Access_Control/)"
        remediation = ""
        location = f'{self.filename}#{self.line_number}'
        issue = re.search(
            r"(res.redirect\((?:req.body|req.id|req.param|req.query))", self.line, re.IGNORECASE)
        if issue:
            Format(self.filename, self.line, self.line_number, issue_type, severity, confidence, CWE, location,
                   description, remediation)

    def weak_hash(self):
        issue_type = "Use of Weak Hash"
        severity = 'Medium'
        confidence = 'High'
        CWE = "CWE-328: Use of Weak Hash (https://cwe.mitre.org/data/definitions/328.html)"
        description = "Learn More: (https://owasp.org/Top10/A02_2021-Cryptographic_Failures/)"
        remediation = "Use a secure password hashing algorithm such as BCRYPT, SCRYPT, PBKDF2, or Argon2."
        location = f'{self.filename}#{self.line_number}'
        issue = re.search(
            r"(createHash\((?:'|\"|.+)(.+md5|sha1)(?:'|\"))", self.line, re.IGNORECASE)
        if issue:
            Format(self.filename, self.line, self.line_number, issue_type, severity, confidence, CWE, location,
                   description, remediation)

    def weak_cipher(self):
        issue_type = "Use of a broken or weak cryptographic algorithm"
        severity = 'Medium'
        confidence = 'High'
        CWE = "CWE-327: Use of a Broken or Risky Cryptographic Algorithm (https://cwe.mitre.org/data/definitions/327.html)"
        description = "Learn More: (https://owasp.org/Top10/A02_2021-Cryptographic_Failures/)"
        remediation = ""
        location = f'{self.filename}#{self.line_number}'
        issue = re.search(
            r"(createCipher\((?:'|\"|.+)(.+des))", self.line, re.IGNORECASE)
        if issue:
            Format(self.filename, self.line, self.line_number, issue_type, severity, confidence, CWE, location,
                   description, remediation)

    def insecure_randomness(self):
        issue_type = "Insecure randomness"
        severity = 'Low'
        confidence = 'Medium'
        CWE = "CWE-338: Use of Cryptographically Weak Pseudo-Random Number Generator (PRNG)(https://cwe.mitre.org/data/definitions/338.html)"
        description = "Learn More: (https://owasp.org/Top10/A02_2021-Cryptographic_Failures/)"
        remediation = ""
        location = f'{self.filename}#{self.line_number}'
        issue = re.search(
            r"(Math.random)", self.line, re.IGNORECASE)
        if issue:
            Format(self.filename, self.line, self.line_number, issue_type, severity, confidence, CWE, location,
                   description, remediation)

    def eval_function(self):
        issue_type = "Eval Injection"
        severity = 'Low'
        confidence = 'Low'
        CWE = "CWE-95: Improper Neutralization of Directives in Dynamically Evaluated Code ('Eval Injection') (" \
              "https://cwe.mitre.org/data/definitions/95.html) "
        description = "Learn More: (https://owasp.org/www-community/attacks/Direct_Dynamic_Code_Evaluation_Eval%20Injection)"
        remediation = ""
        location = f'{self.filename}#{self.line_number}'
        issue = re.search(r"(eval.\(*.*\))", self.line, re.IGNORECASE)
        if issue:
            Format(self.filename, self.line, self.line_number, issue_type, severity, confidence, CWE, location,
                   description, remediation)

    def settimeout_function(self):
        issue_type = "Use of Potentially Dangerous Function"
        severity = 'Medium'
        confidence = 'Medium'
        CWE = "CWE-676: Use of Potentially Dangerous Function (https://cwe.mitre.org/data/definitions/676.html) "
        description = "Learn More: (https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/)"
        remediation = ""
        location = f'{self.filename}#{self.line_number}'
        issue = re.search(r"(settimeout\(.*(\"|\'))", self.line, re.IGNORECASE)
        if issue:
            Format(self.filename, self.line, self.line_number, issue_type, severity, confidence, CWE, location,
                   description, remediation)

    def logging_vulnerabilities(self):
        issue_type = "Insufficient Logging"
        severity = 'Low'
        confidence = 'Low'
        CWE = "CWE-532: Insertion of Sensitive Information into Log File (https://cwe.mitre.org/data/definitions/532.html)"
        description = "Learn More: (https://owasp.org/Top10/A09_2021-Security_Logging_and_Monitoring_Failures/)"
        remediation = ""
        location = f'{self.filename}#{self.line_number}'
        issue = re.search(
            r"(log\((?:\'|\"|.*)(?:req.id|req.query|req.body|req.param))", self.line, re.IGNORECASE)
        if issue:
            Format(self.filename, self.line, self.line_number, issue_type, severity, confidence, CWE, location,
                   description, remediation)
