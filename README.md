# Immunization HL7 v2.5.1 — Data Quality Learning Demo

**Portfolio exercise | Synthetic data only | Not an official CDC, HL7, NIST, or IIS validation tool**

This small educational project explores basic data-quality checks on simplified, fictional immunization HL7 v2.5.1-like VXU messages. It demonstrates a public health informatics workflow: identifying message structure, reviewing key fields, reporting issues, and documenting limitations.

## Background

I am a public health informatics and epidemiology professional with experience supporting HL7 v2.5.1 immunization messaging implementation-guide reviews, IIS stakeholder coordination, NIST IGAMT-based implementation guide work, data quality, and REDCap/Power BI reporting. This independent learning demo uses **newly authored example code**; it is **not** CDC work product, and it does not contain patient or organizational data.

## What the demo does

- Reads fictional HL7-like messages from `data/synthetic_vxu_messages.txt`.
- Checks for `MSH`, `PID`, `ORC`, and `RXA` segments and basic message-type indicators.
- Generates a CSV summary of flagged issues, without storing personally identifiable data.
- Includes small automated tests.

These are **illustrative checks**, not complete conformance rules. Actual HL7 v2.5.1 immunization message validation requires the applicable national/jurisdictional implementation guides, conditional usage rules, terminology bindings, and purpose-built tools such as IGAMT-based validation.

## Try it

Requires Python 3.9 or later; uses only standard-library packages.

```bash
python src/review_messages.py data/synthetic_vxu_messages.txt --output review_results.csv
python -m unittest discover -s tests -v
```

Example output categories: `PASS_BASIC_CHECKS`, `MISSING_PID`, `MISSING_RXA`, `MISSING_ORC`, `UNEXPECTED_MESSAGE_TYPE`.

## Repository map

- `src/review_messages.py` — small Python learning exercise
- `data/synthetic_vxu_messages.txt` — completely fictional example messages
- `tests/test_review_messages.py` — automated checks
- `docs/lessons_learned.md` — reflection and learning goals

## Ethics and confidentiality

No CDC-owned documents, production interface profiles, live patient data, employer code, access credentials, or internal screenshots are included. All names, dates, identifiers, and vaccine codes in the samples are fictional or illustrative. **Do not use this software for clinical decision-making, production validation, or public health reporting.**

## References

- [CDC IIS HL7 Implementation Guide information](https://www.cdc.gov/iis/technical-guidance/hl7.html)
- [CDC Immunization Information Systems](https://www.cdc.gov/iis/)

## Authorship statement

The source code and initial documentation were prepared with AI assistance as a starter exercise. I will review, run, explain, and extend the project before presenting it as a demonstration of my own programming ability.
