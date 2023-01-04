class Game_Interface:
  def __init__(self, num_matrix, curr_hidden_matrix, game_state):
    self.num_matrix = num_matrix
    self.curr_hidden_matrix = curr_hidden_matrix

  def show_interface(self, current_state, selected_row = None, selected_col = None):
    self._clear_console()
    self._show_matrix(selected_row, selected_col)

  # private

  def _show_matrix(self, selected_row = None, selected_col = None):
    for row in range(0, len(self.num_matrix)):
      is_selected_row = row == selected_row
      row_separator = "---" if is_selected_row else "  "
      nums_row_with_separators = ""

      for col in range(0, len(self.num_matrix[row])):
        is_selected_col = col == selected_col
        is_hidden = self.curr_hidden_matrix[row][col]
        element = '_'  if is_hidden else self.num_matrix[row][col]
        nums_row_with_separators = nums_row_with_separators + f'|{element}|' if is_selected_col else f'{element}'

      print(row_separator)
      print(nums_row_with_separators)
      print(row_separator)

  def _clear_console(self):
    print("\033c", end='')
  