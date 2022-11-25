from colorama import Fore
from colorama import Style

# By Severity
all_highs_by_severity = 0
all_mediums_by_severity = 0
all_lows_by_severity = 0


def set_highs_by_severity(highs):
    """
    This function is responsible of track highs severity findings
    :param highs: int to track the number of highs
    """
    global all_highs_by_severity
    all_highs_by_severity += highs


def set_mediums_by_severity(mediums):
    """
    This function is responsible of track mediums severity findings
    :param mediums: int to track the number of mediums
    """
    global all_mediums_by_severity
    all_mediums_by_severity += mediums


def set_lows_by_severity(lows):
    """
    This function is responsible of track lows severity findings
    :param lows: int to track the number of lows
    """
    global all_lows_by_severity
    all_lows_by_severity += lows


# By Confidence
all_highs_by_confidence = 0
all_mediums_by_confidence = 0
all_lows_by_confidence = 0


def set_highs_by_confidence(highs):
    """
    This function is responsible of track high confidence findings
    :param highs: int to track the number of highs
    """
    global all_highs_by_confidence
    all_highs_by_confidence += highs


def set_mediums_by_confidence(mediums):
    """
    This function is responsible of track mediums confidence findings
    :param mediums: int to track the number of highs
    """
    global all_mediums_by_confidence
    all_mediums_by_confidence += mediums


def set_lows_by_confidence(lows):
    """
    This function is responsible of track lows confidence findings
    :param lows: int to track the number of highs
    """
    global all_lows_by_confidence
    all_lows_by_confidence += lows


def overall_stats(scanned_lines):
    # Total Issues
    total_issues = all_highs_by_severity + all_mediums_by_severity + all_lows_by_severity

    print(f"{Fore.LIGHTMAGENTA_EX}Overall Statistics: {Style.RESET_ALL} \n"
          f"  Total scanned lines of code: {scanned_lines} \n"
          f"  Total Issues Found {total_issues}! \n"
          f"  Total Issues (by severity): \n"
          f"        {Fore.LIGHTBLUE_EX}Low:{Style.RESET_ALL} {all_lows_by_severity}{Style.RESET_ALL} \n"
          f"        {Fore.YELLOW}Medium:{Style.RESET_ALL} {all_mediums_by_severity} \n"
          f"        {Fore.RED}High:{Style.RESET_ALL} {all_highs_by_severity}\n"
          f"  Total Issues (by confidence): \n"
          f"        {Fore.LIGHTBLUE_EX}Low:{Style.RESET_ALL} {all_lows_by_confidence} \n"
          f"        {Fore.YELLOW}Medium:{Style.RESET_ALL} {all_mediums_by_confidence} \n"
          f"        {Fore.RED}High:{Style.RESET_ALL} {all_highs_by_confidence}\n")
