import sys
sys.path.append('../transcription/')
import unittest
import transcribe
import filecmp
import os

def removeFile(file):
    """
    helper function to remove a file in the current directory, handling OSError if file does not exist.
    """
    try:
        os.remove(file)
    except OSError:
        pass

class TestTranscription(unittest.TestCase):
    """
    Test transcription of audio file at the default difficulty.
    """
    def runTest(self):
        removeFile("test.mid")
        transcribe.transcribe("test.ogg")
        self.assertTrue(filecmp.cmp("test.mid", "test_expected.mid", shallow = False))

class TestDiff0Transcription(unittest.TestCase):
    """
    Test transcription of audio file at difficulty 0.
    """
    def runTest(self):
        removeFile("test.mid")
        transcribe.transcribe("test.ogg",0)
        self.assertTrue(filecmp.cmp("test.mid", "diff0_expected.mid", shallow = False))

class TestDiff1Transcription(unittest.TestCase):
    """
    Test transcription of audio file at difficulty 1.
    """
    def runTest(self):
        removeFile("test.mid")
        transcribe.transcribe("test.ogg",1)
        self.assertTrue(filecmp.cmp("test.mid", "diff1_expected.mid", shallow = False))

class TestDiff2Transcription(unittest.TestCase):
    """
    Test transcription of audio file at difficulty 2.
    """
    def runTest(self):
        removeFile("test.mid")
        transcribe.transcribe("test.ogg",2)
        self.assertTrue(filecmp.cmp("test.mid", "diff2_expected.mid", shallow = False))

class TestDiff3Transcription(unittest.TestCase):
    """
    Test transcription of audio file at difficulty 3.
    """
    def runTest(self):
        removeFile("test.mid")
        transcribe.transcribe("test.ogg",3)
        self.assertTrue(filecmp.cmp("test.mid", "diff3_expected.mid", shallow = False))

if __name__ == "__main__":
    unittest.main()
