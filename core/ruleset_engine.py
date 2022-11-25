import re
from report.formatting import Format

# This class is responsible of applying each of the rulesets to each of the js source code lines.
class Rule:
    def __init__(self, filename, line, line_number, rules):
        self.filename = filename
        self.line = line.strip()
        self.line_number = line_number
        self.rules = rules
        self.ruleset_engine()

    def ruleset_engine(self):
        """
        This function alternate over each of the rulesets on ruleset.yaml file and scan it against each js line.
        :return:
        """
        for rule in self.rules:
            location = f'{self.filename}#{self.line_number}'
            issue = re.search(rf"{self.rules[rule]['regex']}", self.line,
                              re.IGNORECASE)
            if issue:
                Format(self.filename, self.line, self.line_number, self.rules[rule]['issue_type'], self.rules[rule]['severity']
                       , self.rules[rule]['confidence'], self.rules[rule]['CWE'], location, self.rules[rule]['description'],
                       self.rules[rule]['remediation'])
