# Synthetic test-message playbook

The most important professional skill represented by this repository is not
writing a parser in isolation. It is translating an implementation-guide
requirement into a testable message and a defensible expected result.

## Test-case design pattern

For each synthetic scenario, define:

1. **Profile or rule under review** — the requirement being exercised.
2. **Message change** — the field, segment, value, or repetition changed.
3. **Expected result** — error, warning, pass, or ignored condition.
4. **Observed result** — what the tool or script actually returned.
5. **Disposition** — accepted, defect, false positive, or needs clarification.

## Scenarios represented here

| Scenario | Message change | Expected demonstration result |
|---|---|---|
| Complete message | Includes MSH, PID, ORC, and RXA | `PASS_BASIC_CHECKS` |
| Missing patient segment | Removes PID | `MISSING_PID` |
| Missing administration segment | Removes RXA | `MISSING_RXA` |
| Wrong message type | Uses ADT instead of VXU^V04 | `UNEXPECTED_MESSAGE_TYPE` |
| Wrong HL7 version | Uses a version other than 2.5.1 | `UNEXPECTED_HL7_VERSION` |
| Invalid illustrative PID-8 value | Uses a value outside the demo set | `ILLUSTRATIVE_PID8_VALUE` |
| Repeated message header | Adds a second MSH | `MULTIPLE_MSH_SEGMENTS` |

The scenarios are intentionally simplified. A real project requires the
applicable profile, field-level usage, cardinality, terminology, conditional
logic, and implementation-guide version before a result can be treated as a
formal conformance finding.

## Safe-publication rule

Do not paste project test messages into this repository unless they have been
reviewed for patient identifiers, organization and vendor identifiers,
production control IDs, addresses, dates that could identify a person, internal
URLs, proprietary code systems, and restricted implementation-guide content.
When in doubt, recreate the scenario with new synthetic values instead of
redacting a production message in place.
