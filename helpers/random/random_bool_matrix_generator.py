from random import randrange

class Random_Bool_Matrix_Generator:
    def __init__(self):
        self.matrix = None
        self._curr_size = 0
    
    def get_rand(self, size):
        self._curr_size = size
        if self.matrix is None:
            self.matrix = [[False for x in range(10)] for y in range(10)]
            self._generate()
        return self.matrix

    def get_rand_regenerate(self, size):
        self._curr_size = size
        if self.matrix is None:
            self.matrix = [[False for x in range(10)] for y in range(10)]
        self._generate()
        return self.matrix

    def _generate(self):
        generated = []
        for i in range(self._curr_size):
            col = randrange(0, 9)
            row = randrange(0, 9)
            string_to_check = f'col:{col}row{row}'
            if string_to_check in generated:
                i -= 1
                continue
            generated.append(string_to_check)
            self.matrix[row][col] = True