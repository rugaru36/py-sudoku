from game_random_field_generator import Game_Field_Generator
from game.game_state import Game_State
from game.game_diff import Game_Diff
from random import randrange

class Game_Rule_Manager:
  def __init__(self, diff_lvl):
    self._random_field_generator = Game_Field_Generator()
    self._diff_manager = Game_Diff(diff_lvl)
    self._game_field = self._random_field_generator.get_field()
    self._game_state = Game_State(
      self._diff_manager.get_init_tries(), 
      self._diff_manager.get_init_nums_to_input()
    )
    self._nums_count_to_hide = self._diff_manager.get_init_nums_to_input()
    self._hidden_coordinates = [[False for x in range(self._random_field_generator.get_size())] for y in range(self._random_field_generator.get_size())] 
    self._generate_hidden_coordinates()
    self.show_field_with_hidden_nums()

  def show_field_with_hidden_nums(self):
    size = self._random_field_generator.get_size()
    print('------------field with hidden------------')
    for row in range(size):
      line = ''
      for col in range(size):
        value = '_' if self._hidden_coordinates[row][col] else self._game_field[row][col]
        line += f' {value} '
      print(line)

  def _generate_hidden_coordinates(self):
    generated = []
    for i in range(self._nums_count_to_hide):
      col = randrange(0, 9)
      row = randrange(0, 9)
      string_to_check = f'col:{col}row{row}'
      if string_to_check in generated:
        i -= 1
        continue
      generated.append(string_to_check)
      self._hidden_coordinates[row][col] = True
      # self._hidden_coordinates.append({'row': row, 'col': col})
      
