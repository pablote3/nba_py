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

    def testBoxScore(self):
        boxscore = game.Boxscore(self.gameId)

        playerstats = boxscore.player_stats()
        self.assertTrue((26, 28), playerstats.shape)
        self.assertTrue(('Aaron Gordon' == playerstats[1:2].PLAYER_NAME).all())

        teamstats = boxscore.team_starter_bench_stats()
        self.assertTrue((4, 25), teamstats.shape)
        self.assertTrue(('Magic' == teamstats[1:2].TEAM_NAME).all())

        teamstarterbenchstats = boxscore.team_starter_bench_stats()
        self.assertTrue((4, 25), teamstarterbenchstats.shape)
        self.assertTrue(('Magic' == teamstarterbenchstats[1:2].TEAM_NAME).all())

    def testBoxScoreAdvanced(self):
        boxscoreadvanced = game.BoxscoreAdvanced(self.gameId)

        playeradvanced = boxscoreadvanced.sql_players_advanced()
        self.assertTrue((26, 29), playeradvanced.shape)
        self.assertTrue(('Aaron Gordon' == playeradvanced[1:2].PLAYER_NAME).all())

        teamadvanced = boxscoreadvanced.sql_team_advanced()
        self.assertTrue((2, 27), teamadvanced.shape)
        self.assertTrue(('Celtics' == teamadvanced[1:2].TEAM_NAME).all())

    def testBoxScoreFourFactors(self):
        boxscorefourfactors = game.BoxscoreFourFactors(self.gameId)
        playerfourfactors = boxscorefourfactors.sql_players_four_factors()
        self.assertTrue((26, 17), playerfourfactors.shape)
        self.assertTrue(('Aaron Gordon' == playerfourfactors[1:2].PLAYER_NAME).all())

    def testBoxScoreScoring(self):
        boxscorescoring = game.BoxscoreScoring(self.gameId)
        playerscoring = boxscorescoring.sql_players_scoring()
        self.assertTrue((26, 24), playerscoring.shape)
        self.assertTrue(('Aaron Gordon' == playerscoring[1:2].PLAYER_NAME).all())

    def testBoxScoreSummary(self):
        boxscoresummary = game.BoxscoreSummary(self.gameId)
        officials = boxscoresummary.officials()
        self.assertTrue((3, 4), officials.shape)
        self.assertTrue(('Orr' == officials[1:2].LAST_NAME).all())

    def testBoxScoreUsage(self):
        boxscoreusage = game.BoxscoreUsage(self.gameId)

        teamusage = boxscoreusage.sql_team_usage()
        self.assertTrue((2, 24), teamusage.shape)
        self.assertTrue(('Celtics' == teamusage[1:2].TEAM_NAME).all())

        playerusage = boxscoreusage.sql_players_usage()
        self.assertTrue((26, 27), playerusage.shape)
        self.assertTrue(('Aaron Gordon' == playerusage[1:2].PLAYER_NAME).all())

    def testHustleStats(self):
        hustlestats = game.HustleStats(self.gameId)

        statsavailable = hustlestats.hustle_stats_available()
        self.assertTrue((1, 2), statsavailable.shape)
        self.assertTrue((1 == statsavailable[0:1].HUSTLE_STATUS).all())

        playerstats = hustlestats.hustle_stats_player_box_score()
        self.assertTrue((26, 18), playerstats.shape)
        self.assertTrue(('Orlando' == playerstats[1:2].TEAM_CITY).all())

        teamstats = hustlestats.hustle_stats_team_box_score()
        self.assertTrue((2, 15), teamstats.shape)
        self.assertTrue(('Boston' == teamstats[1:2].TEAM_CITY).all())

    def testPlayByPlay(self):
        playbyplay = game.PlayByPlay(self.gameId)

        info = playbyplay.info()
        self.assertTrue((442, 12), info.shape)
        self.assertTrue((1 == info[1:2].PERIOD).all())

        availablevideo = playbyplay.available_video()
        self.assertTrue((1, 1), availablevideo.shape)
        self.assertTrue((2 == availablevideo.VIDEO_AVAILABLE_FLAG).all())

    def testPlayerTracking(self):
        playertracking = game.PlayerTracking(self.gameId)

        info = playertracking.info();
        self.assertTrue((26, 29), info.shape)
        self.assertTrue(('Aaron Gordon' == info[1:2].PLAYER_NAME).all())
