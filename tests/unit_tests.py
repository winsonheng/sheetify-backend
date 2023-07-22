import sys
sys.path.append('../transcription/')
import unittest
import transcribe
import filecmp

class TestTranscription(unittest.TestCase):
    def runTest(self):
        transcribe.transcribe("test.ogg") # generate test.mid
        self.assertTrue(filecmp.cmp("test.mid", "test_expected.mid", shallow = False))

if __name__ == "__main__":
    unittest.main()
