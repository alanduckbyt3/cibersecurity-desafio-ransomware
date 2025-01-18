import os

def clear():
  """
  Limpa terminal
  """

  system = os.name
  if system == 'nt':
    os.system('cls') # Para Windows
  else:
    os.system('clear') # Para Unix (Linux, macOS)
