class Game_Difficulty:
    def __init__(self, diff_lvl) -> None:
        self._init_diff_data()
        self._init_tries = 0
        self._init_nums_count_to_input = 0
        print(self._diff_data[diff_lvl])
        self._init_tries = self._diff_data[diff_lvl]['init_tries']
        self._init_nums_count_to_input = self._diff_data[diff_lvl]['init_nums_to_input']

    def get_init_tries(self):
        return self._init_tries

    def get_init_hidden_nums_count(self):
        return self._init_nums_count_to_input

    def _check_if_diff_lvl_correct(self, diff_lvl):
        if not self._check_if_diff_lvl_correct(diff_lvl):
            raise ValueError(f'unknown diff_lvl {diff_lvl}')

    def _init_diff_data(self):
        self._diff_data = {
            'easy': {
                'init_tries': 5,
                'init_nums_to_input': 30
            },
            'mid': {
                'init_tries': 3,
                'init_nums_to_input': 40
            },
            'hard': {
                'init_tries': 1,
                'init_nums_to_input': 50
            }
        }
