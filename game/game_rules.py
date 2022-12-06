from helpers.random.random_num_matrix_generator import Random_Num_Matrix_Generator
from helpers.random.random_bool_matrix_generator import Random_Bool_Matrix_Generator
from game.game_diff import Game_Diff
from game.game_state import Game_State
from random import randrange

class Game_Rule_Manager:
  def __init__(self, diff_lvl):
    self._random_num_matrix_generator = Random_Num_Matrix_Generator()
    self._random_bool_matrix_generator = Random_Bool_Matrix_Generator()
    self._game_diff_manager = Game_Diff(diff_lvl)

    nums_to_input = self._game_diff_manager.get_init_nums_to_input()
    tries = self._game_diff_manager.get_init_tries()

    self._game_num_matrix = self._random_num_matrix_generator.get_rand(9)
    self._game_hidden_matrix = self._random_bool_matrix_generator.get_rand(nums_to_input)
    self._game_state = Game_State(tries, nums_to_input)

  def show_field_with_hidden_nums(self):
    size = self._random_num_matrix_generator.get_size()
    print('------------field with hidden------------')
    for row in range(size):
      line = ''
      for col in range(size):
        value = '_' if self._hidden_coordinates[row][col] else self._game_field[row][col]
        line += f' {value} '
      print(line)