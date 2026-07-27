#!/usr/bin/env python3
"""Turn a JSON verdict blob into JUnit XML.

`/test:run` collects verdicts from the evaluator agents and pipes them here.
Escaping is the reason this exists as a script rather than being written by the
model directly: evidence text quotes source and documentation, so it routinely
contains `<`, `&`, and quote characters that must be escaped correctly every
time. An XML library does that by construction.

Input (stdin): a JSON array of verdicts.

  [
    {
      "name": "documentation-consistency",
      "result": "PASS" | "FAIL" | "ERROR",
      "duration": 47.2,
      "error": null,
      "assertions": [
        {"assertion": "...", "result": "PASS" | "FAIL",
         "evidence": "...", "reason": "..."}
      ]
    }
  ]

Usage:
  ... | bin/junit.py results.xml     # write to a file
  ... | bin/junit.py                 # write to stdout
"""

import json
import sys
from pathlib import Path
from xml.dom import minidom
from xml.etree import ElementTree as ET


def build(verdicts) -> str:
    suites = ET.Element("testsuites")
    for v in verdicts:
        name = v.get("name", "(unnamed)")
        assertions = v.get("assertions", [])
        failures = sum(1 for a in assertions if a.get("result") == "FAIL")
        errored = v.get("result") == "ERROR"
        suite = ET.SubElement(
            suites, "testsuite",
            name=name, tests=str(len(assertions)),
            failures=str(failures), errors="1" if errored else "0",
            time=f"{float(v.get('duration') or 0):.3f}",
        )
        if errored:
            case = ET.SubElement(suite, "testcase", name="(evaluation)", classname=name)
            message = v.get("error") or "evaluation error"
            ET.SubElement(case, "error", message=message).text = message
        for a in assertions:
            case = ET.SubElement(suite, "testcase",
                                 name=a.get("assertion", ""), classname=name)
            if a.get("result") == "FAIL":
                reason = a.get("reason") or "assertion failed"
                fail = ET.SubElement(case, "failure", message=reason)
                fail.text = f"evidence: {a.get('evidence', '')}\nreason: {reason}"
    return minidom.parseString(ET.tostring(suites)).toprettyxml(indent="  ")


def main():
    try:
        verdicts = json.load(sys.stdin)
    except json.JSONDecodeError as e:
        print(f"junit.py: could not parse verdicts as JSON: {e}", file=sys.stderr)
        return 2
    if not isinstance(verdicts, list):
        print("junit.py: expected a JSON array of verdicts", file=sys.stderr)
        return 2

    xml = build(verdicts)
    if len(sys.argv) > 1:
        Path(sys.argv[1]).write_text(xml)
        print(f"JUnit XML written to {sys.argv[1]}")
    else:
        sys.stdout.write(xml)
    return 0


if __name__ == "__main__":
    sys.exit(main())
