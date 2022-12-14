from game.game_components.helpers.random.random_num_matrix_generator import Random_Num_Matrix_Generator
from game.game_components.helpers.random.random_bool_matrix_generator import Random_Bool_Matrix_Generator
from game.game_components.game_difficulty import Game_Difficulty
from game.game_components.game_state import Game_State
from game.game_components.game_interface import Game_Interface


class Game_Process_Manager:
  def __init__(self, diff_lvl):
    self._random_num_matrix_generator = Random_Num_Matrix_Generator()
    self._random_bool_matrix_generator = Random_Bool_Matrix_Generator()
    self.diff_lvl = diff_lvl
    self._game_diff_manager = Game_Difficulty(diff_lvl)

    init_hidden_nums_count = self._game_diff_manager.get_init_diff_values()
    init_tries = self._game_diff_manager.get_init_tries()

    self._game_num_matrix = self._random_num_matrix_generator.get_rand(9)
    self._game_hidden_matrix = self._random_bool_matrix_generator.get_rand(init_hidden_nums_count)
    self._game_state = Game_State(init_tries, init_hidden_nums_count)

    self.ui = Game_Interface(self._game_num_matrix, self._game_hidden_matrix, self._game_state)

  # public

  def check_is_hidden(self, row, col):
    return self._game_hidden_matrix[row][col]

  def input_number(self, row, col, num):
    is_hidden = self._game_hidden_matrix[row][col]
    is_correct = self._game_num_matrix[row][col] == num
    if not is_hidden:
      return
    if is_correct:
        self._game_hidden_matrix[row][col] = False
        self._game_state.add_correct_num()
    else:
        self._game_state.add_wrong_num()

  def check_state(self):
    is_lost = self._game_state.check_is_lost()
    is_won = self._game_state.check_is_won()
    if is_lost:
      return 'lost'
    elif is_won:
      return 'won'
    else:
      return 'resume'

  # private
