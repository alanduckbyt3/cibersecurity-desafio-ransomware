import os
from dotenv import load_dotenv
from ..logging import log

def list_files(directory, valid_extensions):
  """
  Lista os arquivos no diretorio com as extenções válidas especificadas em .env.

  :param dir: Caminho do diretorio a ser definido.
  :param valid_extensions: Lista de extenções de arquivos válidos.
  :return Lista de caminho completos dos arquivos encontrados.
  """

  load_dotenv()

  ignored_files = os.getenv('IGNORED_FILES', 'requirements.txt').split(',')
  files = []
  if not os.path.exists(directory):
    log(f"The directory '{directory}' does not exist.", level="error")
    return files
  
  log(f"Processing files in directory: {directory}", level="processing")

  valid_extensions = [ext if ext.startswith('.') else f".{ext}" for ext in valid_extensions]

  for file in os.listdir(directory):
    file_path = os.path.join(directory, file)
    if os.path.isfile(file_path):
      extension = os.path.splitext(file)[-1]
      if os.path.basename(file) in ignored_files:
        continue
      if extension in valid_extensions:
        files.append(file)

  if not files:
    log(f"No files with {valid_extensions} extension found.", level="info")
  else:
    for file in files:
      log(f"File found: {os.path.basename(file)}", level="done")

  return files


def check_permissions(path):
  """
  Verifica as permissoes de leitura, escrita e execução de um caminho (arquivo ou diretorio).

  :param path: Caminho para verificar permissoes.
  :return: True se todas as permissoes necessárias existirem, False caso contrário.
  """

  permissions = {
    "readable": os.access(path, os.R_OK),
    "writable": os.access(path, os.W_OK),
  }
  
  # Retorna True se leitura e escrita forem permitidas para o usuario atual
  return permissions["readable"] and permissions["writable"]
