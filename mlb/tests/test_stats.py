#!/usr/bin/env python

import unittest

import mlbgame


class TestStats(unittest.TestCase):

    def __test_team_picher_stats(self, team):
        self.assertIsInstance(team.bb, int)
        self.assertIsInstance(team.bf, int)
        self.assertIsInstance(team.er, int)
        self.assertIsInstance(team.era, float)
        self.assertIsInstance(team.h, int)
        self.assertIsInstance(team.hr, int)
        self.assertIsInstance(team.out, int)
        self.assertIsInstance(team.r, int)
        self.assertIsInstance(team.so, int)
        self.assertIsInstance(team.team_flag, str)

    def __test_team_batter_stats(self, team):
        self.assertIsInstance(team.ab, int)
        self.assertIsInstance(team.avg, float)
        self.assertIsInstance(team.bb, int)
        self.assertIsInstance(team.d, int)
        self.assertIsInstance(team.da, int)
        self.assertIsInstance(team.h, int)
        self.assertIsInstance(team.hr, int)
        self.assertIsInstance(team.lob, int)
        self.assertIsInstance(team.obp, float)
        self.assertIsInstance(team.ops, float)
        self.assertIsInstance(team.po, int)
        self.assertIsInstance(team.r, int)
        self.assertIsInstance(team.rbi, int)
        self.assertIsInstance(team.slg, float)
        self.assertIsInstance(team.so, int)
        self.assertIsInstance(team.t, int)
        self.assertIsInstance(team.team_flag, str)

    def test_team_stats(self):
        stats = mlbgame.team_stats('2016_08_02_nyamlb_nynmlb_1')
        self.assertEqual(stats.game_id, '2016_08_02_nyamlb_nynmlb_1')
        self.__test_team_picher_stats(stats.away_pitching)
        self.__test_team_picher_stats(stats.home_pitching)
        self.__test_team_batter_stats(stats.away_batting)
        self.__test_team_batter_stats(stats.home_batting)
        pitching = stats.home_pitching
        batting = stats.home_batting
        self.assertEqual(pitching.bb, 2)
        self.assertEqual(pitching.bf, 35)
        self.assertEqual(pitching.er, 1)
        self.assertEqual(pitching.era, 3.35)
        self.assertEqual(pitching.h, 6)
        self.assertEqual(pitching.hr, 1)
        self.assertEqual(pitching.out, 27)
        self.assertEqual(pitching.r, 1)
        self.assertEqual(pitching.so, 10)
        self.assertEqual(pitching.team_flag, 'home')
        self.assertEqual(batting.ab, 35)
        self.assertEqual(batting.avg, 0.238)
        self.assertEqual(batting.bb, 0)
        self.assertEqual(batting.d, 3)
        self.assertEqual(batting.da, 7)
        self.assertEqual(batting.h, 10)
        self.assertEqual(batting.hr, 2)
        self.assertEqual(batting.lob, 10)
        self.assertEqual(batting.obp, 0.309)
        self.assertEqual(batting.ops, 0.717)
        self.assertEqual(batting.po, 27)
        self.assertEqual(batting.r, 7)
        self.assertEqual(batting.rbi, 7)
        self.assertEqual(batting.slg, 0.408)
        self.assertEqual(batting.so, 5)
        self.assertEqual(batting.t, 0)
        self.assertEqual(batting.team_flag, 'home')

    def test_player_stats(self):
        stats = mlbgame.player_stats('2016_08_02_nyamlb_nynmlb_1')
        self.assertEqual(stats.game_id, '2016_08_02_nyamlb_nynmlb_1')
        pitchers = stats.home_pitching + stats.away_pitching
        batters = stats.home_batting + stats.away_batting
        for player in pitchers:
            self.assertIsInstance(player.bb, int)
            self.assertIsInstance(player.bf, int)
            self.assertIsInstance(player.bs, int)
            self.assertIsInstance(player.er, int)
            self.assertIsInstance(player.era, float)
            self.assertIsInstance(player.game_score, int)
            self.assertIsInstance(player.h, int)
            self.assertIsInstance(player.hld, int)
            self.assertIsInstance(player.hr, int)
            self.assertIsInstance(player.id, int)
            self.assertIsInstance(player.l, int)
            self.assertIsInstance(player.name, str)
            self.assertIsInstance(player.name_display_first_last, str)
            self.assertIsInstance(player.np, int)
            self.assertIsInstance(player.out, int)
            self.assertIsInstance(player.pos, str)
            self.assertIsInstance(player.r, int)
            self.assertIsInstance(player.s, int)
            self.assertIsInstance(player.s_bb, int)
            self.assertIsInstance(player.s_er, int)
            self.assertIsInstance(player.s_h, int)
            self.assertIsInstance(player.s_ip, float)
            self.assertIsInstance(player.s_r, int)
            self.assertIsInstance(player.s_so, int)
            self.assertIsInstance(player.so, int)
            self.assertIsInstance(player.sv, int)
            self.assertIsInstance(player.w, int)
        for player in batters:
            self.assertIsInstance(player.a, int)
            self.assertIsInstance(player.ab, int)
            self.assertIsInstance(player.ao, int)
            self.assertIsInstance(player.avg, float)
            self.assertIsInstance(player.bb, int)
            self.assertIsInstance(player.bo, int)
            self.assertIsInstance(player.cs, int)
            self.assertIsInstance(player.d, int)
            self.assertIsInstance(player.e, int)
            self.assertIsInstance(player.fldg, float)
            self.assertIsInstance(player.h, int)
            self.assertIsInstance(player.hbp, int)
            self.assertIsInstance(player.hr, int)
            self.assertIsInstance(player.id, int)
            self.assertIsInstance(player.lob, int)
            self.assertIsInstance(player.name, str)
            self.assertIsInstance(player.name_display_first_last, str)
            self.assertIsInstance(player.obp, float)
            self.assertIsInstance(player.ops, float)
            self.assertIsInstance(player.po, int)
            self.assertIsInstance(player.pos, str)
            self.assertIsInstance(player.r, int)
            self.assertIsInstance(player.rbi, int)
            self.assertIsInstance(player.s_bb, int)
            self.assertIsInstance(player.s_h, int)
            self.assertIsInstance(player.s_hr, int)
            self.assertIsInstance(player.s_r, int)
            self.assertIsInstance(player.s_rbi, int)
            self.assertIsInstance(player.s_so, int)
            self.assertIsInstance(player.sac, int)
            self.assertIsInstance(player.sb, int)
            self.assertIsInstance(player.sf, int)
            self.assertIsInstance(player.slg, float)
            self.assertIsInstance(player.so, int)
            self.assertIsInstance(player.t, int)
        pitcher = pitchers[0]
        batter = batters[0]
        self.assertEqual(pitcher.bb, 1)
        self.assertEqual(pitcher.bf, 26)
        self.assertEqual(pitcher.bs, 0)
        self.assertEqual(pitcher.er, 0)
        self.assertEqual(pitcher.era, 2.41)
        self.assertEqual(pitcher.game_score, 80)
        self.assertEqual(pitcher.h, 4)
        self.assertEqual(pitcher.hld, 0)
        self.assertEqual(pitcher.hr, 0)
        self.assertEqual(pitcher.id, 594798)
        self.assertEqual(pitcher.l, 5)
        self.assertEqual(pitcher.name, 'deGrom')
        self.assertEqual(pitcher.name_display_first_last, 'Jacob deGrom')
        self.assertEqual(pitcher.note, '(W, 7-5)')
        self.assertEqual(pitcher.np, 103)
        self.assertEqual(pitcher.out, 21)
        self.assertEqual(pitcher.pos, 'P')
        self.assertEqual(pitcher.r, 0)
        self.assertEqual(pitcher.s, 69)
        self.assertEqual(pitcher.s_bb, 26)
        self.assertEqual(pitcher.s_er, 32)
        self.assertEqual(pitcher.s_h, 101)
        self.assertEqual(pitcher.s_ip, 119.2)
        self.assertEqual(pitcher.s_r, 35)
        self.assertEqual(pitcher.s_so, 117)
        self.assertEqual(pitcher.so, 8)
        self.assertEqual(pitcher.sv, 0)
        self.assertEqual(pitcher.w, 7)
        self.assertEqual(pitcher.win, 'true')
        self.assertEqual(pitcher.__str__(), 'Jacob deGrom (P)')
        self.assertEqual(batter.a, 0)
        self.assertEqual(batter.ab, 3)
        self.assertEqual(batter.ao, 1)
        self.assertEqual(batter.avg, 0.211)
        self.assertEqual(batter.bb, 0)
        self.assertEqual(batter.bo, 100)
        self.assertEqual(batter.cs, 0)
        self.assertEqual(batter.d, 0)
        self.assertEqual(batter.e, 0)
        self.assertEqual(batter.fldg, 1.0)
        self.assertEqual(batter.go, 1)
        self.assertEqual(batter.h, 1)
        self.assertEqual(batter.hbp, 0)
        self.assertEqual(batter.hr, 1)
        self.assertEqual(batter.id, 457477)
        self.assertEqual(batter.lob, 0)
        self.assertEqual(batter.name, 'De Aza')
        self.assertEqual(batter.name_display_first_last, 'Alejandro De Aza')
        self.assertEqual(batter.obp, 0.3)
        self.assertEqual(batter.ops, 0.623)
        self.assertEqual(batter.po, 5)
        self.assertEqual(batter.pos, 'CF')
        self.assertEqual(batter.r, 1)
        self.assertEqual(batter.rbi, 2)
        self.assertEqual(batter.s_bb, 14)
        self.assertEqual(batter.s_h, 28)
        self.assertEqual(batter.s_hr, 3)
        self.assertEqual(batter.s_r, 12)
        self.assertEqual(batter.s_rbi, 9)
        self.assertEqual(batter.s_so, 42)
        self.assertEqual(batter.sac, 0)
        self.assertEqual(batter.sb, 0)
        self.assertEqual(batter.sf, 0)
        self.assertEqual(batter.slg, 0.323)
        self.assertEqual(batter.so, 0)
        self.assertEqual(batter.t, 0)
        self.assertEqual(batter.__str__(), 'Alejandro De Aza (CF)')
