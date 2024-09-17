"""Imports"""
import re

# set regex rules for determining a valid expression
LOW_PRIO_SIGN = re.compile(r"[\+\-]")
HIGH_PRIO_SIGN = re.compile(r"[\*\/]")
INDICES = re.compile(r"\*\*")

NUMBER = re.compile(r"(\d+\.\d+)|((?<!\.)\d+)")

SIGN = re.compile(rf"{INDICES.pattern}|{HIGH_PRIO_SIGN.pattern}({LOW_PRIO_SIGN.pattern})*|({LOW_PRIO_SIGN.pattern})+")
EXP_ADDITIONAL = re.compile(rf"(({SIGN.pattern})[\(]*({NUMBER.pattern})[\)]*)*")
EXP_BASE = re.compile(rf"({LOW_PRIO_SIGN.pattern})*({NUMBER.pattern}){EXP_ADDITIONAL.pattern}")
  # An EXP_BASE consists of
  # Any amount of LOW_PRIO_SIGN followed by NUMBER
  # THEN EITHER one HIGH_PRIO_SIGN followed by any amount of LOW_PRIO_SIGN
  # OR At least one LOW_PRIO_SIGN
  # Followed by NUMBER, repeat any amount of times.

# EXP but at least one additional sequence needs to occur.
#EXPLICIT_EXP = re.compile(
#  rf"({LOW_PRIO_SIGN.pattern})*" +
#  NUMBER.pattern +
#  rf"""(({HIGH_PRIO_SIGN.pattern}({LOW_PRIO_SIGN.pattern})*|({LOW_PRIO_SIGN.pattern}){{1,}}){NUMBER.pattern}){{1,}}""")
