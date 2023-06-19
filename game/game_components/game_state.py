class Game_State:
  def __init__(self, init_tries, init_nums_to_input) -> None:
    self._current_state = "row_num"
    self._left_tries = init_tries
    self._left_nums_to_input = init_nums_to_input

  # public

  def check_is_lost(self):
    is_lost = self._left_tries == 0
    if is_lost: self._current_state = 'lost'
    return is_lost

  def check_is_won(self):
    is_won = self._left_tries > 0 and self._left_nums_to_input == 0
    if is_won: self._current_state = "won"
    return is_won

  def add_wrong_num(self):
    self._left_tries -= 1

  def add_correct_num(self):
    self._left_nums_to_input -= 1

  # "row_num" | "col_num" | "num_value" | "won" | "lost"
  def get_current_state(self):
    return self._current_state

  def after_row_provided(self):
    self._current_state = "col_num"

  def after_col_provided(self):
    self._current_state = "num_value"

  def after_num_provided(self):
    self._current_state = "row_num"