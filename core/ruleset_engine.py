import re
from report.formatting import Format
import yaml

# This class is responsible of applying each of the rulesets to each of the js source code lines.
class Rule:
    def __init__(self, filename, line, line_number):
        self.filename = filename
        self.line = line.strip()
        self.line_number = line_number
        self.ruleset_engine()

    def ruleset_engine(self):
        """
        This function alternate over each of the rulesets on ruleset.yaml file and scan it against each js line.
        :return:
        """
        with open('core/ruleset.yaml', 'r') as ruleset:
            rules = yaml.safe_load(ruleset)
            for rule in rules:
                location = f'{self.filename}#{self.line_number}'
                issue = re.search(rf"{rules[rule]['regex']}", self.line,
                                  re.IGNORECASE)
                if issue:
                    Format(self.filename, self.line, self.line_number, rules[rule]['issue_type'], rules[rule]['severity']
                           , rules[rule]['confidence'], rules[rule]['CWE'], location, rules[rule]['description'],
                           rules[rule]['remediation'])
