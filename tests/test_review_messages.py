import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from review_messages import assess_message

class ReviewMessageTests(unittest.TestCase):
    def test_complete_synthetic_example(self):
        text = 'MSH|^~\\&|A|B|C|D|20260101||VXU^V04|ID|P|2.5.1\nPID|x\nORC|x\nRXA|x'
        self.assertEqual(assess_message(text), ['PASS_BASIC_CHECKS'])

    def test_missing_segments_are_reported(self):
        self.assertIn('MISSING_RXA', assess_message('MSH|VXU^V04\nPID|x\nORC|x'))

    def test_wrong_message_type_is_flagged(self):
        self.assertIn('UNEXPECTED_MESSAGE_TYPE', assess_message('MSH|ADT^A01\nPID|x\nORC|x\nRXA|x'))

    def test_unexpected_version_is_flagged(self):
        text = 'MSH|^~\\&|A|B|C|D|20260101||VXU^V04|ID|P|2.3.1\nPID|x\nORC|x\nRXA|x'
        self.assertIn('UNEXPECTED_HL7_VERSION', assess_message(text))

    def test_illustrative_pid8_value_is_flagged(self):
        text = 'MSH|^~\\&|A|B|C|D|20260101||VXU^V04|ID|P|2.5.1\nPID|1|||||||X\nORC|x\nRXA|x'
        self.assertIn('ILLUSTRATIVE_PID8_VALUE', assess_message(text))

    def test_multiple_msh_segments_are_flagged(self):
        text = ('MSH|^~\\&|A|B|C|D|20260101||VXU^V04|ID|P|2.5.1\n'
                'MSH|^~\\&|A|B|C|D|20260101||VXU^V04|ID2|P|2.5.1\n'
                'PID|x\nORC|x\nRXA|x')
        self.assertIn('MULTIPLE_MSH_SEGMENTS', assess_message(text))

if __name__ == '__main__':
    unittest.main()
