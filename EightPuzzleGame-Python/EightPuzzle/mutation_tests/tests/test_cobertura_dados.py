import unittest
import puzzle_game as mut


class TestCoberturaDadosLine(unittest.TestCase):

    def setUp(self):
        # 1  2  3
        # 4  5  6
        # 7  8  -
        self.puzzle_game = mut.PuzzleGame(3)

    def test_get_tile_All_c_uses_Some_p_use_path_1(self):
        print("TestCoberturaDadosLine.test_get_tile_All_c_uses_Some_p_use")

        result = self.puzzle_game.get_tile(2, 2)

        self.assertEqual(result, 5)

    def test_get_tile_All_p_uses_path_1(self):
        print("TestCoberturaDadosLine.test_get_tile_All_p_uses_path_1")
        with self.assertRaises(mut.InvalidPositionException):
            self.puzzle_game.get_tile(0, 2)

    def test_get_tile_All_p_uses_path_2(self):
        print("TestCoberturaDadosLine.test_get_tile_All_p_uses_path_2")
        result = self.puzzle_game.get_tile(3, 3)

        self.assertEqual(result, " ")

    def test_get_tile_All_p_uses_path_3(self):
        print("TestCoberturaDadosLine.test_get_tile_All_p_uses_path_3")
        result = self.puzzle_game.get_tile(2, 2)

        self.assertEqual(result, 5)


class TestCoberturaDadosColumn(unittest.TestCase):

    def setUp(self):
        # 1  2  3
        # 4  5  6
        # 7  8  -
        self.puzzle_game = mut.PuzzleGame(3)

    def test_get_tile_All_c_uses_Some_p_use_path_1(self):
        print("TestCoberturaDadosColumn.test_get_tile_All_c_uses_Some_p_use")

        result = self.puzzle_game.get_tile(2, 2)

        self.assertEqual(result, 5)

    def test_get_tile_All_p_uses_path_1(self):
        print("TestCoberturaDadosColumn.test_get_tile_All_p_uses_path_1")
        with self.assertRaises(mut.InvalidPositionException):
            self.puzzle_game.get_tile(2, 0)

    def test_get_tile_All_p_uses_path_2(self):
        print("TestCoberturaDadosColumn.test_get_tile_All_p_uses_path_2")
        result = self.puzzle_game.get_tile(3, 3)

        self.assertEqual(result, " ")

    def test_get_tile_All_p_uses_path_3(self):
        print("TestCoberturaDadosColumn.test_get_tile_All_p_uses_path_3")
        result = self.puzzle_game.get_tile(2, 2)

        self.assertEqual(result, 5)
