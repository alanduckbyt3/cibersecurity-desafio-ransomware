from time import sleep

def log(message, level="info"):
  """
  Loga as menssagens no console com seus respectivos simbolos de acordo com o level.

  :param message: Menssagem a ser exibida.
  :param level: Nivel  da mensagem (info, success, error, processing).
  """

  symbols = {
    "info": "[ i ]",
    "success": "[ ✓ ]",
    "done": "[ + ]",
    "error": "[ × ]",
    "processing": "[ ~ ]",
  }
  print(f"\n{symbols.get(level, '[ ? ]')} {message}")
  sleep(0.5) # Atraso de 0.5s para prosseguir
