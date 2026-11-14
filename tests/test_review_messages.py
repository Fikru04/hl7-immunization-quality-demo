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

if __name__ == '__main__':
    unittest.main()
