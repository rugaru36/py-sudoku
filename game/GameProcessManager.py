from game.game_components.GameDifficulty import Game_Difficulty
from game.game_data.RandomGameFieldGenerator import RandomGameFieldGenerator
from game.io.UIOutputManager import UIOutputManager
from game.game_components.GameStateManagerSingleton import GameStateManagerSingleton


class GameProcessManager:

    def __init__(self, diff_lvl):
        self._game_diff_manager = Game_Difficulty(diff_lvl)
        nums_to_input = self._game_diff_manager.get_init_hidden_nums_count()
        tries = self._game_diff_manager.get_init_tries()

        random_game_field_generator = RandomGameFieldGenerator(9, nums_to_input)

        self.game_state = GameStateManagerSingleton()
        self.game_state.init_data(
            tries,
            nums_to_input,
            random_game_field_generator.get_rand_num_matrix(),
            random_game_field_generator.get_rand_bool_matrix()
        )
        self._ui = UIOutputManager()

    def show(self):
        self._ui.show_interface()

    def _input_number(self, row, col, num):
        is_hidden = self._game_bool_hidden_matrix[row][col]
        is_correct = self._game_num_matrix[row][col] == num
        if not is_hidden:
            return None
        if is_correct:
            # self._game_bool_hidden_matrix[row][col] = False
            self.game_state.add_correct_num()
        else:
            self.game_state.add_wrong_num()
        # self._game_state.get_current_state()

