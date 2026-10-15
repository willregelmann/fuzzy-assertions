---
name: report-escaping
assertions:
  - Running bin/junit.py on verdicts.json exits with status 0
  - The XML it writes parses as well-formed XML
  - For each FAIL assertion and each ERROR in verdicts.json, its evidence, reason or error string appears in the parsed XML exactly, character for character
  - The ERROR verdict appears as an error element and not as a failure element
---

Check that the report writer survives evidence full of XML-special characters.

1. Run `python3 bin/junit.py < .claude/tests/report-escaping/verdicts.json` from the project root and capture its output.
2. Parse the output with `python3 -c "import sys, xml.dom.minidom; xml.dom.minidom.parseString(sys.stdin.read())"` to check it is well-formed.
3. Compare the parsed text of each failure and error against the strings in `verdicts.json`.
4. Quote the commands you ran, their exit statuses, and the relevant output.
