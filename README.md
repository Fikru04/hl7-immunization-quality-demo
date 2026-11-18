# HL7 Immunization Interoperability Portfolio

**Public Health Informaticist | HL7 v2.5.1 | IIS messaging | Synthetic data only**

This repository combines a small, reproducible Python demonstration with an
anonymized description of hands-on public health informatics work. It shows how
I create, inspect, test, interpret, and document immunization HL7 v2.5.1
messages while separating public portfolio material from confidential project
artifacts.

> **Scope and confidentiality:** This repository contains newly authored code
> and synthetic examples only. It does not identify jurisdictions or technology
> partners, and it does not include production messages, proprietary
> implementation guides, patient information, credentials, or internal
> screenshots. It is not an official CDC, HL7, NIST, IIS, or vendor validation
> tool.

## Professional experience represented

In my work as a Public Health Informaticist, I have supported immunization
interoperability activities across multiple jurisdictional IIS environments and
technology partners. Publicly, I describe that experience at an intentionally
general level to protect confidential project information.

Relevant hands-on activities include:

- Reviewing and interpreting jurisdictional HL7 v2.5.1 immunization
  implementation-guide requirements.
- Creating positive and negative test messages to exercise required fields,
  optional fields, usage rules, cardinality, conditional logic, and data-format
  expectations.
- Comparing expected validation behavior with actual results and documenting
  defects, false positives, missing warnings, and implementation-guide gaps.
- Supporting implementation-guide digitization and review using **IGAMT**.
- Using **P-ACT** and related testing workflows to organize test scenarios and
  assess message behavior.
- Supporting interoperability testing and data-quality review using **CAART**.
- Serving as a liaison among IIS subject-matter experts, public health partners,
  developers, and technology partners.

The repository demonstrates the same reasoning pattern at a smaller, public,
synthetic scale: define a rule, construct a test message, identify the expected
result, run the check, and document the limitation.

## What this demonstration does

The script in `src/review_messages.py`:

- Reads fictional VXU-like messages from `data/synthetic_vxu_messages.txt`.
- Checks for basic `MSH`, `PID`, `ORC`, and `RXA` structure.
- Reviews the illustrative message type and HL7 version.
- Flags duplicate `MSH` segments and an illustrative invalid PID-8 value.
- Produces a CSV review summary with `PASS` or `REVIEW` status and issue flags.
- Includes automated tests for positive and negative scenarios.

These checks are deliberately transparent and limited. They are not a complete
HL7 conformance engine and must not be used for clinical decision-making,
production interface certification, or public health reporting.

## Run the demonstration

Requires Python 3.9 or later and no third-party packages.

```bash
python src/review_messages.py data/synthetic_vxu_messages.txt --output review_results.csv
python -m unittest discover -s tests -v
```

The generated CSV contains one row per synthetic message with the review status
and semicolon-separated issue flags.

## Repository map

| Path | Purpose |
|---|---|
| `src/review_messages.py` | Small, readable demonstration reviewer |
| `data/synthetic_vxu_messages.txt` | Fictional VXU-like sample messages |
| `tests/test_review_messages.py` | Automated positive and negative tests |
| `docs/hands_on_workflow.md` | Anonymized mapping from professional practice to this demo |
| `docs/test_message_playbook.md` | Synthetic test-message design and interpretation approach |
| `docs/lessons_learned.md` | Limitations, learning reflection, and next steps |

## Why synthetic data is used

The purpose of this portfolio is to demonstrate technical reasoning without
exposing protected health information, confidential implementation-guide
content, organization names, vendor names, production identifiers, or internal
project details. Any future examples added to this repository should be newly
authored or fully sanitized and should be reviewed before publication.

## References

- [CDC IIS HL7 technical guidance](https://www.cdc.gov/iis/technical-guidance/hl7.html)
- [CDC Immunization Information Systems](https://www.cdc.gov/iis/)

## Authorship

The initial starter code was prepared with AI assistance. I review, run,
explain, and extend the repository so that it accurately represents my own
public-health informatics practice and learning.
