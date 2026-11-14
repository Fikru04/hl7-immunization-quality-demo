"""Educational HL7-like VXU structure review. NOT a conformant HL7 validator."""

import argparse
import csv
from pathlib import Path


def assess_message(message):
    """Return illustrative structural flags for a fictional HL7-like VXU example."""
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
        writer.writerow(['synthetic_example_number', 'issue_flags'])
        for index, msg in enumerate(examples, start=1):
            writer.writerow([index, '; '.join(assess_message(msg))])
    print(f'Reviewed {len(examples)} synthetic examples; wrote {args.output}')


if __name__ == '__main__':
    main()
