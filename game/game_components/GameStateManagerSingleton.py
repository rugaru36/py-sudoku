class GameStateManagerSingleton:
    instance = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(GameStateManagerSingleton, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        self._is_data_initialized = False
        self._current_state = None
        self._left_tries = None
        self._left_nums_to_input = None
        self._hidden_bool_matrix = None
        self._num_matrix = None
        self._init_tries = None
        self._init_nums_to_input = None

    def get_num_matrix(self):
        return self._num_matrix

    def get_bool_matrix(self):
        return self._hidden_bool_matrix

    def get_left_tries(self):
        return self._left_tries

    def get_init_tries(self):
        return self._init_tries

    def get_left_nums_to_input(self):
        return self._left_nums_to_input

    def get_init_nums_to_input(self):
        return self._init_nums_to_input

    def init_data(self, init_tries, init_nums_to_input, num_matrix, hidden_bool_matrix):
        self._is_data_initialized = True
        self._current_state = "row_num"
        self._init_tries = init_tries
        self._left_tries = init_tries
        self._left_nums_to_input = init_nums_to_input
        self._init_nums_to_input = init_nums_to_input
        self._hidden_bool_matrix = hidden_bool_matrix
        self._num_matrix = num_matrix

    # public

    def check_is_lost(self):
        is_lost = self._left_tries == 0
        if is_lost:
            self._current_state = 'lost'
        return is_lost

    def check_is_won(self):
        is_won = self._left_tries > 0 and self._left_nums_to_input == 0
        if is_won:
            self._current_state = "won"
        return is_won

    def add_wrong_num(self):
        self._left_tries -= 1

    def add_correct_num(self):
        self._left_nums_to_input -= 1

    # "row_num" | "col_num" | "num_value" | "won" | "lost"
    def get_current_state(self):
        self.check_is_won()
        self.check_is_lost()
        return self._current_state

    def after_row_provided(self):
        self._current_state = "col_num"

    def after_col_provided(self):
        self._current_state = "num_value"

    def after_num_provided(self):
        self._current_state = "row_num"
