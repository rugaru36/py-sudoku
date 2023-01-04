class Num_Input:
  def simple_num_input(self, message, min, max, special_value = None):
    while True:
      print(message)
      value = int(input())
      if special_value != None and value == special_value:
        return value
      if value > max: print(f'{value} > {max}')
      elif value < min: print(f'{value} < {min}')
      else: return value
      


