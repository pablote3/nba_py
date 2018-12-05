import unittest
from nba_py import player
from nba_py.player import get_player


class TestPlayer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.playerId = get_player('Tim', 'Duncan')
        cls.vs_playerId = get_player('Stephen', 'Curry')
        cls.teamId = ''
        cls.measureType = 'Base'
        cls.perMode = 'PerGame'
        cls.plusMinus = 'N'
        cls.paceAdjust = 'N'
        cls.rank = 'Y'
        cls.leagueId = '00'
        cls.season = '2015-16'
        cls.seasonType = 'Regular Season'
        cls.poRound = ''
        cls.outcome = ''
        cls.location = 'Home'
        cls.month = 0
        cls.sessionSegment = ''
        cls.dateFrom = ''
        cls.dateTo = ''
        cls.opponentTeamId = 0
        cls.vsConference = ''
        cls.vsDivision = ''
        cls.gameSegment = ''
        cls.period = 1
        cls.shotClockRange = ''
        cls.lastNGames = 0

    def testAll(self):
        assert player.PlayerList()
        assert player.PlayerSummary(self.playerId)
        # assert player.PlayerGeneralSplits(self.playerId)
        # assert player.PlayerOpponentSplits(self.playerId)
        assert player.PlayerLastNGamesSplits(self.playerId)
        assert player.PlayerInGameSplits(self.playerId)
        assert player.PlayerClutchSplits(self.playerId)
        # assert player.PlayerShootingSplits(self.playerId)
        assert player.PlayerPerformanceSplits(self.playerId)
        assert player.PlayerYearOverYearSplits(self.playerId)

        assert player.PlayerCareer(self.playerId)

        assert player.PlayerProfile(self.playerId)
        assert player.PlayerGameLogs(self.playerId)
        assert player.PlayerShotTracking(self.playerId)
        assert player.PlayerReboundTracking(self.playerId)
        assert player.PlayerPassTracking(self.playerId)
        assert player.PlayerDefenseTracking(self.playerId)
        # assert player.PlayerShotLogTracking(self.playerId)
        # assert player.PlayerReboundLogTracking(self.playerId)
        assert player.PlayerVsPlayer(self.playerId, self.vs_playerId)

    def testPlayerCareer(self):
        playercareer = player.PlayerCareer(self.playerId)

        allstarseasontotals = playercareer.all_star_season_totals()
        self.assertTrue((15, 27), allstarseasontotals.shape)
        self.assertTrue(('WST' == allstarseasontotals[1:2].TEAM_ABBREVIATION).all())

        careerallstarseasontotals = playercareer.career_all_star_season_totals()
        self.assertTrue((1, 24), careerallstarseasontotals.shape)
        self.assertTrue((15 == careerallstarseasontotals[0:1].GP).all())

        collegeseasoncareertotals = playercareer.college_season_career_totals()
        self.assertTrue((1, 24), collegeseasoncareertotals.shape)
        self.assertTrue((128 == collegeseasoncareertotals[0:1].GP).all())

        collegeseasontotals = playercareer.college_season_totals()
        self.assertTrue((4, 27), collegeseasontotals.shape)
        self.assertTrue((31 == collegeseasontotals[0:1].GP).all())

        postseasoncareertotals = playercareer.post_season_career_totals()
        self.assertTrue((1, 24), postseasoncareertotals.shape)
        self.assertTrue((251 == postseasoncareertotals[0:1].GP).all())

        postseasontotals = playercareer.post_season_totals()
        self.assertTrue((18, 27), postseasontotals.shape)
        self.assertTrue((9 == postseasontotals[0:1].GP).all())

        #postseasonrankings = playercareer.post_season_rankings()

        preseasoncareertotals = playercareer.preseason_career_totals()
        self.assertTrue((18, 27), preseasoncareertotals.shape)
        self.assertTrue(('NR' == preseasoncareertotals[0:1].GP).all())

        preseasonseasontotals = playercareer.preseason_season_totals()
        self.assertTrue((19, 27), preseasonseasontotals.shape)
        self.assertTrue(('NR' == preseasonseasontotals[0:1].GP).all())

        regularseasoncareertotals = playercareer.regular_season_career_totals()
        self.assertTrue((1, 24), regularseasoncareertotals.shape)
        self.assertTrue((1392 == regularseasoncareertotals[0:1].GP).all())

        regularseasontotals = playercareer.regular_season_totals()
        self.assertTrue((19, 27), regularseasontotals.shape)
        self.assertTrue((82 == regularseasontotals[0:1].GP).all())

        #regularseasonrankings = playercareer.regular_season_rankings()

    def testPlayerClutchSplits(self):
        playercluchsplits = player.PlayerClutchSplits(self.playerId,
                                                      self.teamId,
                                                      self.measureType,
                                                      self.perMode,
                                                      self.plusMinus,
                                                      self.paceAdjust,
                                                      self.rank,
                                                      self.leagueId,
                                                      self.season,
                                                      self.seasonType,
                                                      self.poRound,
                                                      self.outcome,
                                                      self.location,
                                                      self.month,
                                                      self.sessionSegment,
                                                      self.dateFrom,
                                                      self.dateTo,
                                                      self.opponentTeamId,
                                                      self.vsConference,
                                                      self.vsDivision,
                                                      self.gameSegment,
                                                      self.lastNGames)

        self.assertTrue((1, 62) == playercluchsplits.overall().shape)
        self.assertTrue((31 == playercluchsplits.overall()[0:1].GP).all())
        self.assertTrue((1 == playercluchsplits.last5min_deficit_5point()[0:1].GP).all())
        self.assertTrue((8 == playercluchsplits.last5min_plusminus_5point()[0:1].GP).all())
        self.assertTrue((1 == playercluchsplits.last3min_deficit_5point()[0:1].GP).all())
        self.assertTrue((8 == playercluchsplits.last3min_plusminus_5point()[0:1].GP).all())
        self.assertTrue((1 == playercluchsplits.last1min_deficit_5point()[0:1].GP).all())
        self.assertTrue((6 == playercluchsplits.last1min_plusminus_5point()[0:1].GP).all())
        self.assertTrue((1 == playercluchsplits.last30sec_deficit_3point()[0:1].GP).all())
        self.assertTrue((1 == playercluchsplits.last10sec_deficit_3point()[0:1].GP).all())
