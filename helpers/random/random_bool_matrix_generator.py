from random import randrange

class Random_Bool_Matrix_Generator:
  def __init__(self):
    self._pairs = None
    
  def get_rand(self, pairs_count, max_value):
    if self._pairs is None:
      self._pairs = [[False for x in range(10)] for y in range(10)]
      self._generate_random_pairs(pairs_count, max_value)
    return self._pairs

  def get_rand_regenerate(self, pairs_count, max_value):
    if self._pairs is None:
      self._pairs = [[False for x in range(10)] for y in range(10)]
    self._generate_random_pairs(pairs_count, max_value)
    return self._pairs

  def _generate_random_pairs(self, pairs_count, max_value):
    generated = []
    for i in range(self._count_to_hide):
      col = randrange(0, 9)
      row = randrange(0, 9)
      string_to_check = f'col:{col}row{row}'
      if string_to_check in generated:
        i -= 1
        continue
      generated.append(string_to_check)
      self._hidden_coordinates[row][col] = True