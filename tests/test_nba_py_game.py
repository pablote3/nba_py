import unittest
from nba_py import game


class TestGame(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.gameId = '0021800040'

    def testAll(self):
        assert game.BoxscoreSummary(self.gameId)
        assert game.Boxscore(self.gameId)
        assert game.BoxscoreScoring(self.gameId)
        assert game.BoxscoreUsage(self.gameId)
        assert game.BoxscoreMisc(self.gameId)
        assert game.BoxscoreAdvanced(self.gameId)
        assert game.BoxscoreFourFactors(self.gameId)
        assert game.PlayByPlay(self.gameId)
        assert game.HustleStats(self.gameId)

    def testBoxScoreSummary(self):
        boxscoresummary = game.BoxscoreSummary(self.gameId)
        officials = boxscoresummary.officials()
        self.assertTrue((3, 4), officials.shape)
        self.assertTrue(('Orr' == officials[1:2].LAST_NAME).all())

    def testBoxScoreScoring(self):
        boxscorescoring = game.BoxscoreScoring(self.gameId)
        playerscores = boxscorescoring.sql_players_scoring()
        self.assertTrue((26, 24), playerscores.shape)
        self.assertTrue(('Aaron Gordon' == playerscores[1:2].PLAYER_NAME).all())
