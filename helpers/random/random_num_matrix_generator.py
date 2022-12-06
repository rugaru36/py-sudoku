from random import randrange

class Random_Num_Matrix_Generator:
  """generates game fiels"""

  def __init__(self, size = 9):
    self._size = size
    self._matrix = None
    self._generate_base_matrix()
    self._randomize_matrix()

  # public

  def get_rand(self, size):
    if self._matrix is None:
      self._matrix = [[0 for x in range(size)] for y in range(size)]
      self._generate_base_matrix()
      self._randomize_matrix()
    return self._matrix

  def get_rand_regenerate(self, size):
    if self._matrix is None:
      self._matrix = [[0 for x in range(size)] for y in range(size)]
    self._generate_base_matrix()
    self._randomize_matrix()
    return self._matrix

  def get_size(self):
    return self._size

  # private

  def _generate_base_matrix(self):
    value = 0
    for i in range(self._size):
      value += 1
      for j in range(self._size):
        if value > self._size:
          value -= self._size
        self._matrix[i][j] = value
        value += 1

  def _randomize_matrix(self):
    # rows
    for target_row in range(self._size):
      row_to_swap_with = randrange(0, self._size)
      for col in range(self._size):
        buff = self._matrix[target_row][col]
        self._matrix[target_row][col] = self._matrix[row_to_swap_with][col]
        self._matrix[row_to_swap_with][col] = buff
    # cols
    for target_col in range(self._size):
      col_to_swap_with = randrange(0, self._size)
      for row in range(self._size):
        buff = self._matrix[row][target_col]
        self._matrix[row][target_col] = self._matrix[row][col_to_swap_with]
        self._matrix[row][col_to_swap_with] = buff

