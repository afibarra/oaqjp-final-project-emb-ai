from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):

    def test_emotion_detector_analyzer(self):
        test_joy = emotion_detector("I am glad this happened")
        self.assertEqual(test_joy['dominant_emotion'], 'joy')

        test_joy = emotion_detector("I am really mad about this")
        self.assertEqual(test_joy['dominant_emotion'], 'anger')

        test_joy = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(test_joy['dominant_emotion'], 'disgust')

        test_joy = emotion_detector("I am so sad about this")
        self.assertEqual(test_joy['dominant_emotion'], 'sadness')

        test_joy = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(test_joy['dominant_emotion'], 'fear')

unittest.main()
