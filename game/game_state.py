class Game_State:
  def __init__(self, init_tries, init_nums_to_input) -> None:
    self._left_tries = init_tries
    self._left_nums_to_input = init_nums_to_input

  def check_is_lost(self):
    return self._left_tries == 0

  def check_is_won(self):
    return self._left_tries > 0 and self._left_nums_to_input == 0

  def add_wrong_num(self):
    self._left_tries -= 1

  def add_correct_num(self):
    self._left_nums_to_input -= 1
