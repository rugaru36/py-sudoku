from helpers.random.random_num_matrix_generator import Random_Num_Matrix_Generator
from helpers.random.random_bool_matrix_generator import Random_Bool_Matrix_Generator
from game.game_components.game_difficulty import Game_Difficulty
from game.game_components.game_state_manager import Game_State_Manager


class Game_Process_Manager:
    def __init__(self, diff_lvl):
        self._random_num_matrix_generator = Random_Num_Matrix_Generator()
        self._random_bool_matrix_generator = Random_Bool_Matrix_Generator()
        self._game_diff_manager = Game_Difficulty(diff_lvl)

        nums_to_input = self._game_diff_manager.get_init_nums_to_input()
        tries = self._game_diff_manager.get_init_tries()

        self._game_num_matrix = self._random_num_matrix_generator.get_rand(9)
        self._game_hidden_matrix = self._random_bool_matrix_generator.get_rand(nums_to_input)
        self._game_state = Game_State_Manager(tries, nums_to_input)

    # private

    def _input_number(self, row, col, num):
        is_hidden = self._game_hidden_matrix[row][col]
        is_correct = self._game_num_matrix[row][col] == num
        if not is_hidden:
            return
        if is_correct:
            self._game_hidden_matrix[row][col] = False
            self._game_state.add_correct_num()
        else:
            self._game_state.add_wrong_num()

    def _check_state(self):
        is_lost = self._game_state.check_is_lost()
        is_won = self._game_state.check_is_won()
        if is_lost:
            return 'lost'
        elif is_won:
            return 'won'
        else:
            return 'continue'
