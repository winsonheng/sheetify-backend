from django.test import TestCase
# Create your tests here.
from utils import transcribe
import filecmp
import os

TEST_LOC = "./test_data/"
TEST_INPUT = TEST_LOC + "test.mid"
TEST_OUTPUT = TEST_LOC + "test.ogg"

class TestTranscription(TestCase):
    def removeFile(file):
        """
        helper function to remove a file in the current directory, handling OSError if file does not exist.
        """
        try:
            os.remove(file)
        except OSError:
            pass
    
    def testTranscription(self):
        """
        Test transcription of audio file at the default difficulty.
        """
        removeFile(TEST_OUTPUT)
        transcribe(TEST_INPUT)
        self.assertTrue(filecmp.cmp(TEST_OUTPUT, TEST_LOC + "expected.mid", shallow = False))

    def testTranscription0(self):
        """
        Test transcription of audio file at difficulty 0.
        """
        removeFile(TEST_OUTPUT)
        transcribe(TEST_INPUT,0)
        self.assertTrue(filecmp.cmp(TEST_OUTPUT, TEST_LOC + "diff0_expected.mid", shallow = False))

    def testTranscription1(self):
        """
        Test transcription of audio file at difficulty 1.
        """
        removeFile(TEST_OUTPUT)
        transcribe(TEST_INPUT,1)
        self.assertTrue(filecmp.cmp(TEST_OUTPUT, TEST_LOC + "diff1_expected.mid", shallow = False))
    
    def testTranscription2(self):
        """
        Test transcription of audio file at difficulty 2.
        """
        removeFile(TEST_OUTPUT)
        transcribe(TEST_INPUT,2)
        self.assertTrue(filecmp.cmp(TEST_OUTPUT, TEST_LOC + "diff2_expected.mid", shallow = False))

    def testTranscription3(self):
        """
        Test transcription of audio file at difficulty 3.
        """
        removeFile(TEST_OUTPUT)
        transcribe(TEST_INPUT,3)
        self.assertTrue(filecmp.cmp(TEST_OUTPUT, TEST_LOC + "diff3_expected.mid", shallow = False))

    