from django.test import TestCase
# Create your tests here.
import transcribe
import filecmp
import os

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
        removeFile("test.mid")
        transcribe.transcribe("test.ogg")
        self.assertTrue(filecmp.cmp("test.mid", "test_expected.mid", shallow = False))

    def testTranscription0(self):
        """
        Test transcription of audio file at difficulty 0.
        """
        removeFile("test.mid")
        transcribe.transcribe("test.ogg",0)
        self.assertTrue(filecmp.cmp("test.mid", "diff0_expected.mid", shallow = False))

    def testTranscription1(self):
        """
        Test transcription of audio file at difficulty 1.
        """
        removeFile("test.mid")
        transcribe.transcribe("test.ogg",1)
        self.assertTrue(filecmp.cmp("test.mid", "diff1_expected.mid", shallow = False))
    
    def testTranscription2(self):
        """
        Test transcription of audio file at difficulty 2.
        """
        removeFile("test.mid")
        transcribe.transcribe("test.ogg",2)
        self.assertTrue(filecmp.cmp("test.mid", "diff2_expected.mid", shallow = False))

    def testTranscription3(self):
        """
        Test transcription of audio file at difficulty 3.
        """
        removeFile("test.mid")
        transcribe.transcribe("test.ogg",3)
        self.assertTrue(filecmp.cmp("test.mid", "diff3_expected.mid", shallow = False))

    