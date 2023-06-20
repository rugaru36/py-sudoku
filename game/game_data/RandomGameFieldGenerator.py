from random import randrange


class RandomGameFieldGenerator:
    def __init__(self, matrix_size, num_of_hidden_values):
        self._curr_size = matrix_size
        self._num_of_hidden_values = num_of_hidden_values
        self._num_matrix = [[0 for x in range(self._curr_size)] for y in range(self._curr_size)]
        self._bool_matrix = [[False for x in range(self._curr_size)] for y in range(self._curr_size)]
        self.generate_all()

    # public
    def generate_all(self):
        self._generate_random_num_matrix()
        self._generate_random_bool_matrix()

    def get_current_size(self):
        return self._curr_size

    def get_rand_num_matrix(self):
        if self._num_matrix is None:
            self._generate_random_num_matrix()
        return self._num_matrix

    def get_rand_bool_matrix(self):
        if self._bool_matrix is None:
            self._generate_random_bool_matrix()
        return self._bool_matrix

    # private

    def _generate_random_bool_matrix(self):
        generated = []
        for i in range(self._num_of_hidden_values):
            col = randrange(0, self._curr_size - 1)
            row = randrange(0, self._curr_size - 1)
            string_to_check = f'col:{col}row{row}'
            if string_to_check in generated:
                i -= 1
                continue
            generated.append(string_to_check)
            self._bool_matrix[row][col] = True

    def _generate_random_num_matrix(self):
        self._generate_base_num_matrix()
        self._randomize_num_matrix()

    def _generate_base_num_matrix(self):
        value = 0
        for row in range(self._curr_size):
            value += 1
            for col in range(self._curr_size):
                if value > self._curr_size:
                    value -= self._curr_size
                self._num_matrix[row][col] = value
                value += 1

    def _randomize_num_matrix(self):
        # rows
        for target_row in range(self._curr_size):
            row_to_swap_with = randrange(0, self._curr_size)
            for col in range(self._curr_size):
                buff = self._num_matrix[target_row][col]
                self._num_matrix[target_row][col] = self._num_matrix[row_to_swap_with][col]
                self._num_matrix[row_to_swap_with][col] = buff
        # cols
        for target_col in range(self._curr_size):
            col_to_swap_with = randrange(0, self._curr_size)
            for row in range(self._curr_size):
                buff = self._num_matrix[row][target_col]
                self._num_matrix[row][target_col] = self._num_matrix[row][col_to_swap_with]
                self._num_matrix[row][col_to_swap_with] = buff


