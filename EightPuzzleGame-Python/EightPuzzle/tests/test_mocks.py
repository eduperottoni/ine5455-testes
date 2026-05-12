import unittest
from puzzle_game import PuzzleGame
from unittest.mock import patch
import os
from puzzle_game_with_mock import PuzzleGameWithPlayer
import puzzle_game_with_mock


class TestMockGetTile(unittest.TestCase):

    # Testes do método get_tile sem mock:

    def test_get_tile_returns_valid_position(self):
        game = PuzzleGame(3)

        assert 5 == game.get_tile(2, 2)

    def test_get_tile_returns_empty_position(self):
        game = PuzzleGame(3)

        result = game.get_tile(3, 3)

        self.assertEqual(" ", result)

    # Testes do método get_tile com mock:

    @patch("puzzle_game.Board.get_tile")
    def test_get_tile_returns_valid_position_with_mock(self, mock_board_get_tile):
        game = PuzzleGame(3)
        mock_board_get_tile.return_value = 9
        assert 9 == game.get_tile(2, 2)

    def test_get_tile_returns_empty_position_with_mock(self):
        game = PuzzleGame(3)

        with patch.object(game, "line_of_empty_position", 2):
            with patch.object(game, "column_of_empty_position", 2):
                assert " " == game.get_tile(2, 2)

    # Testes do método end_of_the_game sem mock:

    def test_end_of_the_game_finished(self):
        game = PuzzleGameWithPlayer(3, "PlayerVencedor")

        result = game.end_of_the_game()

        self.assertEqual(result, "Saved")
        self.assertTrue(os.path.exists("PlayerVencedor.txt"))

        if os.path.exists("PlayerVencedor.txt"):
            os.remove("PlayerVencedor.txt")

    def test_end_of_the_game_not_finished(self):
        game = PuzzleGameWithPlayer(3, "PlayerAtivo")
        game.move_tile(6)

        result = game.end_of_the_game()

        self.assertEqual(result, "Game not finished")
        self.assertFalse(os.path.exists("PlayerAtivo.txt"))

    # Testes do método end_of_the_game com mock:

    @patch("puzzle_game_with_mock.PuzzleGameWithPlayer.save_game_to_file")
    def test_end_of_the_game_finished_with_mock(self, mock_save):
        mock_save.return_value = "Saved (Mocked)"

        game = PuzzleGameWithPlayer(3, "PlayerMock")

        result = game.end_of_the_game()

        self.assertEqual(result, "Saved")
        mock_save.assert_called_once()

    @patch("puzzle_game_with_mock.PuzzleGameWithPlayer.save_game_to_file")
    def test_end_of_the_game_not_finished_with_mock(self, mock_save):
        game = PuzzleGameWithPlayer(3, "PlayerMock")
        game.move_tile(6)

        result = game.end_of_the_game()

        self.assertEqual(result, "Game not finished")
        mock_save.assert_not_called()
