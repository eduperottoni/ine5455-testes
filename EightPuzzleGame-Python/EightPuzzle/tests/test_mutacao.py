from puzzle_game import PuzzleGame
import puzzle_game
import unittest


class TestMutacao(unittest.TestCase):

    def test_move_tile_correct_modifies_board(self):
        """
        puzzle_game.xǁPuzzleGameǁmove_tile__mutmut_20
        tests/test_cobertura.py::TestBranchesMoveTile::test_move_tile_with_not_adjacent_position_path3
        tests/test_cobertura.py::TestBranchesMoveTile::test_move_tile_with_valid_move_path2
        tests/test_cobertura.py::TestBranchesMoveTile::test_move_tile_without_tile_in_the_board_path1
        tests/test_cobertura.py::TestComandosMoveTile::test_move_tile_with_valid_move_path2
        tests/test_cobertura.py::TestComandosMoveTile::test_move_tile_without_tile_in_the_board_path1

        Em todos esses testes, apenas o resultado lógico retornado pelo move_tile é testado e não o estado do board, que é modificado durante o método

        self.board.put_tile(
            tile, self.line_of_empty_position, self.column_of_empty_position
        )

        self.board.put_tile(
            None, self.line_of_empty_position, self.column_of_empty_position
        )
        """

        game = PuzzleGame(3)

        game.move_tile(8)

        valor = game.board.get_tile(3, 3)

        # Antes não tinha esse statement
        # Agora se None for colocado na posição, vai falhar
        self.assertEqual(valor, 8)

    def test_get_tile_when_line_or_column_is_empty(self):
        """
        > puzzle_game.xǁPuzzleGameǁget_tile__mutmut_14
        tests/test_cobertura_dados.py::TestCoberturaDadosColumn::test_get_tile_All_c_uses_Some_p_use_path_1
        tests/test_cobertura_dados.py::TestCoberturaDadosColumn::test_get_tile_All_p_uses_path_1
        tests/test_cobertura_dados.py::TestCoberturaDadosColumn::test_get_tile_All_p_uses_path_2
        tests/test_cobertura_dados.py::TestCoberturaDadosColumn::test_get_tile_All_p_uses_path_3
        tests/test_cobertura_dados.py::TestCoberturaDadosLine::test_get_tile_All_c_uses_Some_p_use_path_1
        tests/test_cobertura_dados.py::TestCoberturaDadosLine::test_get_tile_All_p_uses_path_1
        tests/test_cobertura_dados.py::TestCoberturaDadosLine::test_get_tile_All_p_uses_path_2
        tests/test_cobertura_dados.py::TestCoberturaDadosLine::test_get_tile_All_p_uses_path_3

        Em nenhum desses testes, o caso em que apenas linha ou coluna está na correspondente da casa vazia foi testado

        if (
            line == self.line_of_empty_position and column == self.column_of_empty_position
        ):

        if (
            line == self.line_of_empty_position or column == self.column_of_empty_position
        ):
        """

        game = PuzzleGame(3)

        result = game.get_tile(3, 2)

        # Garantimos que o resultado deve ser diferente de vazio
        # Nesse caso, o OR faz o teste falhar, pois vai retornar vazio
        # self.assertNotEqual(result, " ")
        self.assertEqual(result, 8)

    def test_get_tile_for_column_one(self):
        """
        > puzzle_game.xǁPuzzleGameǁget_tile__mutmut_10
        tests/test_cobertura_dados.py::TestCoberturaDadosColumn::test_get_tile_All_c_uses_Some_p_use_path_1
        tests/test_cobertura_dados.py::TestCoberturaDadosColumn::test_get_tile_All_p_uses_path_1
        tests/test_cobertura_dados.py::TestCoberturaDadosColumn::test_get_tile_All_p_uses_path_2
        tests/test_cobertura_dados.py::TestCoberturaDadosColumn::test_get_tile_All_p_uses_path_3
        tests/test_cobertura_dados.py::TestCoberturaDadosLine::test_get_tile_All_c_uses_Some_p_use_path_1
        tests/test_cobertura_dados.py::TestCoberturaDadosLine::test_get_tile_All_p_uses_path_1
        tests/test_cobertura_dados.py::TestCoberturaDadosLine::test_get_tile_All_p_uses_path_2
        tests/test_cobertura_dados.py::TestCoberturaDadosLine::test_get_tile_All_p_uses_path_3

        Em nenhum desses testes o 1 é testado com limite para a coluna

        if (
            line > 0
            and line <= self.board.number_of_lines
            and column > 0
            and column <= self.board.number_of_columns
        ):

        if (
            line > 0
            and line <= self.board.number_of_lines
            and column > 1
            and column <= self.board.number_of_columns
        ):
        """

        game = PuzzleGame(3)

        result = game.get_tile(2, 1)

        self.assertEqual(result, 4)

    def test_get_tile_for_line_one(self):
        """
        > puzzle_game.xǁPuzzleGameǁget_tile__mutmut_7
        tests/test_cobertura_dados.py::TestCoberturaDadosColumn::test_get_tile_All_c_uses_Some_p_use_path_1
        tests/test_cobertura_dados.py::TestCoberturaDadosColumn::test_get_tile_All_p_uses_path_1
        tests/test_cobertura_dados.py::TestCoberturaDadosColumn::test_get_tile_All_p_uses_path_2
        tests/test_cobertura_dados.py::TestCoberturaDadosColumn::test_get_tile_All_p_uses_path_3
        tests/test_cobertura_dados.py::TestCoberturaDadosLine::test_get_tile_All_c_uses_Some_p_use_path_1
        tests/test_cobertura_dados.py::TestCoberturaDadosLine::test_get_tile_All_p_uses_path_1
        tests/test_cobertura_dados.py::TestCoberturaDadosLine::test_get_tile_All_p_uses_path_2
        tests/test_cobertura_dados.py::TestCoberturaDadosLine::test_get_tile_All_p_uses_path_3

        Em nenhum desses testes o 1 é testado com limite para a linha

        if (
            line > 0
            and line <= self.board.number_of_lines
            and column > 0
            and column <= self.board.number_of_columns
        ):

        if (
            line > 1
            and line <= self.board.number_of_lines
            and column > 0
            and column <= self.board.number_of_columns
        ):
        """

        game = PuzzleGame(3)

        result = game.get_tile(1, 2)

        self.assertEqual(result, 2)

    def test_generate_list_of_files_return_expected_number_of_tiles(self):
        """
        Não havia teste para essa função. Testando o tamanho da lista de tiles geradas abriga o teste sobre a mutação

        Mutação 1:
        puzzle_game.xǁPuzzleGameǁ__generate_list_of_tiles____mutmut_3

        quantity_of_tiles = self.dimension * self.dimension - 1
        for tile in range(1, quantity_of_tiles + 1):
            list_of_tiles.append(tile)

        quantity_of_tiles = self.dimension * self.dimension + 1
        for tile in range(1, quantity_of_tiles + 1):
            list_of_tiles.append(tile)

        Mutação 2:
        puzzle_game.xǁPuzzleGameǁ__generate_list_of_tiles____mutmut_12

        quantity_of_tiles = self.dimension * self.dimension - 1
        for tile in range(1, quantity_of_tiles + 1):
            list_of_tiles.append(tile)

        quantity_of_tiles = self.dimension * self.dimension - 1
        for tile in range(1, quantity_of_tiles + 2):
            list_of_tiles.append(tile)
        """
        game = PuzzleGame(3)
        result_list = game.__generate_list_of_tiles__()
        self.assertEqual(len(result_list), 8)
