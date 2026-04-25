import unittest
import puzzle_game as mut
import shufflers_for_testing_puzzles as shufflers


class TestComandosMoveTile(unittest.TestCase):

    def test_move_tile_without_tile_in_the_board_path1(self):
        puzzle_game = mut.PuzzleGame(3)
        puzzle_game.dic_positions_of_tiles.update({"qualquer coisa": (4, 4)})

        result = puzzle_game.move_tile("qualquer coisa")

        self.assertFalse(result)

    def test_move_tile_with_valid_move_path2(self):
        puzzle_game = mut.PuzzleGame(3)

        result = puzzle_game.move_tile(8)

        self.assertTrue(result)


class TestBranchesMoveTile(unittest.TestCase):

    def test_move_tile_without_tile_in_the_board_path1(self):
        puzzle_game = mut.PuzzleGame(3)
        puzzle_game.dic_positions_of_tiles.update({"qualquer coisa": (4, 4)})

        result = puzzle_game.move_tile("qualquer coisa")

        self.assertFalse(result)

    def test_move_tile_with_valid_move_path2(self):
        puzzle_game = mut.PuzzleGame(3)

        result = puzzle_game.move_tile(8)

        self.assertTrue(result)

    def test_move_tile_with_not_adjacent_position_path3(self):
        puzzle_game = mut.PuzzleGame(3)

        result = puzzle_game.move_tile(2)

        self.assertFalse(result)
