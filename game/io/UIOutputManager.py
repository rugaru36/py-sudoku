from game.io.MatrixOutputManager import MatrixOutputManager
from game.io.helpers.consoleHelpers import clear_console
from game.game_components.GameStateManagerSingleton import game_state_instance


class UIOutputManager:
    def __init__(self):
        self._matrix_output = MatrixOutputManager()

    def show_interface(self):
        clear_console()
        print(f'current_state: {game_state_instance.get_current_state()}')
        print(f'tries: {game_state_instance.get_left_tries()}/{game_state_instance.get_init_tries()}')
        print(f'left nums: {game_state_instance.get_left_nums_to_input()}/{game_state_instance.get_init_nums_to_input}')
        self._matrix_output.output_matrix()
