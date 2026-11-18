# Synthetic VXU Error-Resolution Case Study

## Purpose

This case study recreates a professional HL7 immunization testing pattern using newly authored synthetic values. It does not identify a jurisdiction, organization, vendor, facility, patient, or implementation-guide profile.

## Scenario

A synthetic `VXU^V04` immunization message was prepared for IIS testing. The message contained the core patient, order, and vaccination information, but the patient-department information did not contain a recognized primary-facility value.

## Iterative Test and Interpretation

| Iteration | Test action | Response interpretation | Disposition |
|---|---|---|---|
| 1 | Submit a VXU message with the primary-facility value omitted | ACK/ERR response identifies a required-field and segment-sequence issue in PD1 | Correct the missing value |
| 2 | Add `SYNTH-FACILITY-001` to the relevant PD1 field | Response changes to a table-value-not-found error | Confirm the value must exist in the approved table |
| 3 | Replace it with `SYNTH-FACILITY-VALID` | Message is accepted with MSA / AA | Record the successful correction |
| 4 | Convert the patient request into synthetic Z34 and Z44 QBP messages | Exercise immunization-history and evaluated-history/forecast query workflows | Compare expected and actual query behavior |

## Skills Demonstrated

- Creating and inspecting HL7 v2.5.1 VXU and QBP messages
- Interpreting ACK, MSA, and ERR segments
- Tracing findings to a segment, field, and error category
- Distinguishing a missing required value from an unrecognized table value
- Correcting messages iteratively based on system feedback
- Testing related history and forecast query workflows
- Documenting expected behavior, observed behavior, and disposition

## Public-Data Boundary

All values in this case study are synthetic. Do not add source messages from a real project to this repository. Remove patient names, addresses, phone numbers, medical-record numbers, facility identifiers, client identifiers, control IDs, internal timestamps, proprietary codes, and restricted implementation-guide content.

## Important Limitation

The error categories and field locations shown here are illustrative. Actual validation depends on the receiving IIS, applicable implementation guide, profile version, terminology tables, and local configuration.
