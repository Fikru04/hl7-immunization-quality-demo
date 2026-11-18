"""Educational HL7-like VXU review. NOT a conformant HL7 validator."""

import argparse
import csv
from pathlib import Path


def assess_message(message):
    """Return illustrative structural and field-level flags.

    The rules intentionally remain small and transparent. They demonstrate how a
    test message can be inspected and translated into reviewable findings; they
    do not replace an implementation-guide validator.
    """
    segments = [line.strip() for line in message.splitlines() if line.strip()]
    names = [line.split('|', 1)[0] for line in segments]
    flags = []
    for required in ("MSH", "PID", "ORC", "RXA"):
        if required not in names:
            flags.append(f"MISSING_{required}")
    msh = next((line for line in segments if line.startswith('MSH|')), '')
    # MSH fields are special in HL7; this is a simplified, demonstrative check only.
    if not msh or 'VXU^V04' not in msh:
        flags.append('UNEXPECTED_MESSAGE_TYPE')
    if msh and not msh.endswith('|2.5.1'):
        flags.append('UNEXPECTED_HL7_VERSION')
    if names.count('MSH') > 1:
        flags.append('MULTIPLE_MSH_SEGMENTS')
    pid = next((line for line in segments if line.startswith('PID|')), '')
    if pid:
        pid_fields = pid.split('|')
        if len(pid_fields) > 8 and pid_fields[8] not in {'M', 'F', 'O', 'U'}:
            flags.append('ILLUSTRATIVE_PID8_VALUE')
    return flags or ['PASS_BASIC_CHECKS']


def read_examples(path):
    """Split synthetic examples on blank lines."""
    content = Path(path).read_text(encoding='utf-8')
    return [block for block in content.strip().split('\n\n') if block.strip()]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', help='Text file containing fictional messages separated by blank lines')
    parser.add_argument('--output', default='review_results.csv', help='CSV results path')
    args = parser.parse_args()
    examples = read_examples(args.input)
    with open(args.output, 'w', newline='', encoding='utf-8') as output:
        writer = csv.writer(output)
        writer.writerow(['synthetic_example_number', 'review_status', 'issue_flags'])
        for index, msg in enumerate(examples, start=1):
            flags = assess_message(msg)
            status = 'PASS' if flags == ['PASS_BASIC_CHECKS'] else 'REVIEW'
            writer.writerow([index, status, '; '.join(flags)])
    print(f'Reviewed {len(examples)} synthetic examples; wrote {args.output}')


if __name__ == '__main__':
    main()
