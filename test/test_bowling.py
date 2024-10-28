import unittest

from bowling import BowlingGame
from bowling_error import BowlingError
from frame import Frame

class TestBowlingGame(unittest.TestCase):

    def test_game_created(self):
        f = Frame(1,5)
        game = BowlingGame()
        game.add_frame(f)
        self.assertEqual(f, game.get_frame_at(0))

    def test_empty_game(self):
        game = BowlingGame()
        self.assertRaises(BowlingError, game.get_frame_at, 0)

    def test_game_created_10_frames(self):
        game = BowlingGame()
        game.add_frame(Frame(1,5))
        game.add_frame(Frame(3,6))
        game.add_frame(Frame(7,2))
        game.add_frame(Frame(3,6))
        game.add_frame(Frame(4,4))
        game.add_frame(Frame(5,3))
        game.add_frame(Frame(3,3))
        game.add_frame(Frame(4,5))
        game.add_frame(Frame(8,1))
        f = Frame(2,6)
        game.add_frame(f)
        self.assertEqual(f, game.get_frame_at(9))

    def test_game_created_11_frames(self):
        game = BowlingGame()
        game.add_frame(Frame(1,5))
        game.add_frame(Frame(3,6))
        game.add_frame(Frame(7,2))
        game.add_frame(Frame(3,6))
        game.add_frame(Frame(4,4))
        game.add_frame(Frame(5,3))
        game.add_frame(Frame(3,3))
        game.add_frame(Frame(4,5))
        game.add_frame(Frame(8,1))
        game.add_frame(Frame(8, 1))
        self.assertRaises(BowlingError, game.add_frame, Frame(2,6))

    def test_calculate_score(self):
        game = BowlingGame()
        game.add_frame(Frame(1, 5))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(7, 2))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(4, 4))
        game.add_frame(Frame(5, 3))
        game.add_frame(Frame(3, 3))
        game.add_frame(Frame(4, 5))
        game.add_frame(Frame(8, 1))
        game.add_frame(Frame(2, 6))
        self.assertEqual(81, game.calculate_score())

    def test_calculate_score_spare(self):
        game = BowlingGame()
        game.add_frame(Frame(9, 1))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(7, 2))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(4, 4))
        game.add_frame(Frame(5, 3))
        game.add_frame(Frame(3, 3))
        game.add_frame(Frame(4, 5))
        game.add_frame(Frame(8, 1))
        game.add_frame(Frame(2, 6))
        self.assertEqual(88, game.calculate_score())

    def test_calculate_score_strike(self):
        game = BowlingGame()
        game.add_frame(Frame(10, 0))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(7, 2))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(4, 4))
        game.add_frame(Frame(5, 3))
        game.add_frame(Frame(3, 3))
        game.add_frame(Frame(4, 5))
        game.add_frame(Frame(8, 1))
        game.add_frame(Frame(2, 6))
        self.assertEqual(94, game.calculate_score())

    def test_calculate_score_strike_followed_by_spare(self):
        game = BowlingGame()
        game.add_frame(Frame(10, 0))
        game.add_frame(Frame(4, 6))
        game.add_frame(Frame(7, 2))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(4, 4))
        game.add_frame(Frame(5, 3))
        game.add_frame(Frame(3, 3))
        game.add_frame(Frame(4, 5))
        game.add_frame(Frame(8, 1))
        game.add_frame(Frame(2, 6))
        self.assertEqual(103, game.calculate_score())

    def test_calculate_score_strike_followed_by_strike(self):
        game = BowlingGame()
        game.add_frame(Frame(10, 0))
        game.add_frame(Frame(10, 0))
        game.add_frame(Frame(7, 2))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(4, 4))
        game.add_frame(Frame(5, 3))
        game.add_frame(Frame(3, 3))
        game.add_frame(Frame(4, 5))
        game.add_frame(Frame(8, 1))
        game.add_frame(Frame(2, 6))
        self.assertEqual(112, game.calculate_score())

    def test_calculate_score_spare_followed_by_spare(self):
        game = BowlingGame()
        game.add_frame(Frame(8, 2))
        game.add_frame(Frame(5, 5))
        game.add_frame(Frame(7, 2))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(4, 4))
        game.add_frame(Frame(5, 3))
        game.add_frame(Frame(3, 3))
        game.add_frame(Frame(4, 5))
        game.add_frame(Frame(8, 1))
        game.add_frame(Frame(2, 6))
        self.assertEqual(98, game.calculate_score())

    def test_calculate_score_last_frame_spare(self):
        game = BowlingGame()
        game.add_frame(Frame(1, 5))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(7, 2))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(4, 4))
        game.add_frame(Frame(5, 3))
        game.add_frame(Frame(3, 3))
        game.add_frame(Frame(4, 5))
        game.add_frame(Frame(8, 1))
        game.add_frame(Frame(2, 8))
        game.set_first_bonus_throw(7)
        self.assertEqual(90, game.calculate_score())

    def test_calculate_score_last_frame_strike(self):
        game = BowlingGame()
        game.add_frame(Frame(1, 5))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(7, 2))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(4, 4))
        game.add_frame(Frame(5, 3))
        game.add_frame(Frame(3, 3))
        game.add_frame(Frame(4, 5))
        game.add_frame(Frame(8, 1))
        game.add_frame(Frame(10, 0))
        game.set_first_bonus_throw(7)
        game.set_second_bonus_throw(2)
        self.assertEqual(92, game.calculate_score())

    def test_calculate_score_last_2_frames_strike(self):
        game = BowlingGame()
        game.add_frame(Frame(1, 5))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(7, 2))
        game.add_frame(Frame(3, 6))
        game.add_frame(Frame(4, 4))
        game.add_frame(Frame(5, 3))
        game.add_frame(Frame(3, 3))
        game.add_frame(Frame(4, 5))
        game.add_frame(Frame(10, 0))
        game.add_frame(Frame(10, 0))
        game.set_first_bonus_throw(7)
        game.set_second_bonus_throw(2)
        self.assertEqual(110, game.calculate_score())



