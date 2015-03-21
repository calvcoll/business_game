import unittest
import score

class TestScores(unittest.TestCase):
    def setUp(self):
        self.player_score = score.Score()
        self.orig_score = self.player_score.getScore()
    
    def test_score_add(self):
        self.player_score.setScore(True, False, False)
        self.assertEqual(self.player_score.getScore(), self.orig_score + 10)

    def test_score_double(self):
        self.player_score.setScore(True, True, False)
        self.assertEqual(self.player_score.getScore(), self.orig_score + 20)

    def test_score_fifty(self):
        self.player_score.setScore(True, False, True)
        self.assertEqual(self.player_score.getScore(), self.orig_score + 5)

    def test_score_incorrect(self):
        self.player_score.setScore(False, False, False)
        self.assertEqual(self.player_score.getScore(), self.orig_score + 0)

    def test_score_double_incorrect(self):
        self.player_score.setScore(False, True, False)
        self.assertEqual(self.player_score.getScore(), self.orig_score - 20)

    def test_score_fifty_incorrect(self):
        self.player_score.setScore(False, False, True)
        self.assertEqual(self.player_score.getScore(), self.orig_score - 10)

