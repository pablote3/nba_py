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

    def testBoxScoreScore(self):
        boxscore = game.Boxscore(self.gameId)
        playerstats = boxscore.player_stats()
        self.assertTrue((26, 28), playerstats.shape)
        self.assertTrue(('Aaron Gordon' == playerstats[1:2].PLAYER_NAME).all())

    def testBoxScoreScoring(self):
        boxscorescoring = game.BoxscoreScoring(self.gameId)
        playerscoring = boxscorescoring.sql_players_scoring()
        self.assertTrue((26, 24), playerscoring.shape)
        self.assertTrue(('Aaron Gordon' == playerscoring[1:2].PLAYER_NAME).all())

    def testBoxScoreUsage(self):
        boxscoreusage = game.BoxscoreUsage(self.gameId)
        playerusage = boxscoreusage.sql_players_usage()
        self.assertTrue((26, 27), playerusage.shape)
        self.assertTrue(('Aaron Gordon' == playerusage[1:2].PLAYER_NAME).all())

    def testBoxScoreAdvanced(self):
        boxscoreadvanced = game.BoxscoreAdvanced(self.gameId)
        playeradvanced = boxscoreadvanced.sql_players_advanced()
        self.assertTrue((26, 29), playeradvanced.shape)
        self.assertTrue(('Aaron Gordon' == playeradvanced[1:2].PLAYER_NAME).all())

    def testBoxScoreFourFactors(self):
        boxscorefourfactors = game.BoxscoreFourFactors(self.gameId)
        playerfourfactors = boxscorefourfactors.sql_players_four_factors()
        self.assertTrue((26, 17), playerfourfactors.shape)
        self.assertTrue(('Aaron Gordon' == playerfourfactors[1:2].PLAYER_NAME).all())

    def testGamePlayByPlay(self):
        gameplaybyplay = game.PlayByPlay(self.gameId)
        playerscores = gameplaybyplay.info()
        self.assertTrue((442, 12), playerscores.shape)
        self.assertTrue((4 == playerscores[1:2].EVENTNUM).all())

    def testGameHustleStats(self):
        gamehustlestats = game.HustleStats(self.gameId)
        playerhustlestats = gamehustlestats.hustle_stats_player_box_score()
        self.assertTrue((26, 18), playerhustlestats.shape)
        self.assertTrue(('Orlando' == playerhustlestats[1:2].TEAM_CITY).all())
