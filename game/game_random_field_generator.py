from random import randrange

class Game_Field_Generator:
  """generates game fiels"""

  def __init__(self):
    self._size = 9
    self._field = [[0 for x in range(self._size)] for y in range(self._size)] 
    self._generate_base_field()
    self._make_field_random()

  # public

  def get_field(self):
    return self._field

  def get_size(self):
    return self._size

  # private

  def _generate_base_field(self):
    value = 0
    for i in range(self._size):
      value += 1
      for j in range(self._size):
        if value > self._size:
          value -= self._size
        self._field[i][j] = value
        value += 1

  def _make_field_random(self):
    # rows
    for target_row in range(self._size):
      row_to_swap_with = randrange(0, self._size)
      for col in range(self._size):
        buff = self._field[target_row][col]
        self._field[target_row][col] = self._field[row_to_swap_with][col]
        self._field[row_to_swap_with][col] = buff
    # cols
    for target_col in range(self._size):
      col_to_swap_with = randrange(0, self._size)
      for row in range(self._size):
        buff = self._field[row][target_col]
        self._field[row][target_col] = self._field[row][col_to_swap_with]
        self._field[row][col_to_swap_with] = buff

