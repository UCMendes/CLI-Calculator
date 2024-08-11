"""Imports"""
import re

# set regex rules for determining a valid expression
NUMBER = re.compile(r"(\d+\.\d+)|((?<!\.)\d+)")
LOW_PRIO_SIGN = re.compile(r"[\+\-]")
HIGH_PRIO_SIGN = re.compile(r"[\*\/]")
EXP = re.compile(rf"({LOW_PRIO_SIGN.pattern})*({NUMBER.pattern})(({HIGH_PRIO_SIGN.pattern}({LOW_PRIO_SIGN.pattern})*|({LOW_PRIO_SIGN.pattern})+)({NUMBER.pattern}))*")
  # Any amount of LOW_PRIO_SIGN followed by NUMBER
  # THEN EITHER one HIGH_PRIO_SIGN followed by any amount of LOW_PRIO_SIGN
  # OR At least one LOW_PRIO_SIGN
  # Followed by NUMBER, repeat line 15 any amount of times.

# EXP but at least one sequence of line 15 needs to occur.
#EXPLICIT_EXP = re.compile(
#  rf"({LOW_PRIO_SIGN.pattern})*" +
#  NUMBER.pattern +
#  rf"""(({HIGH_PRIO_SIGN.pattern}({LOW_PRIO_SIGN.pattern})*|({LOW_PRIO_SIGN.pattern}){{1,}}){NUMBER.pattern}){{1,}}""")
