import os
from Crypto.Cipher import AES
from tqdm import tqdm
from .file_management import clear_term
from .file_management import check_permissions
from .logging import log

def decryption(file_path, crypto_key, suffix):
  """
  Descriptografa um arquivo e salva com o sufixo especificado.

  :param file_path: Caminho do arquivo a ser criptografado.
  :param crypto_key: Chave para descriptografar.
  :param suffix: Sufixo adicionado ao nome do arquivo durante a criptografia.
  """

  try:
    # Abrir o arquivo criptogafado
    with open(file_path, 'rb') as f:
      nonce = f.read(8)
      encrypted_data = f.read()

    # Criar uma Cifra AES com o mesmo nonce
    cipher = AES.new(crypto_key, AES.MODE_CTR, nonce=nonce)
    # Descriptografar os dados
    decrypted_data = cipher.decrypt(encrypted_data)

    # Remover o sufixo do nome do arquivo par criar o nome original
    original_file_name = file_path.replace(suffix, '')

    # Salvar os arquivos descriptografados no arquivo original
    with open(original_file_name, 'wb') as f:
      f.write(decrypted_data)

    # Remover o arquivo criptografado
    if os.path.exists(original_file_name):
      os.remove(file_path)
  except Exception as e:
    log(f"Error decrypting the file '{file_path}': {e}", level="error")


def decrypt_files(directory, crypto_key, suffix, valid_extensions):
  """
  Descriptografa todos os arquivos no diretorio atual com o sufixo especificado.

  :param dir: Caminho do diretorio a ser definido.
  :param crypto_key: Chave para criptografar.
  :param suffix: Sufixo para adicionar ao final do nome do arquivo a ser criptografado.
  :param valid_extensions: Lista de extenções de arquivos válidos.
  """

  clear_term()
  files = [
    file for file in os.listdir(directory)
    if file.endswith(suffix) and any(file.endswith(ext + suffix) for ext in valid_extensions)
    ]

  if not files:
    log("No files found to decrypt.", level="info")
    return
  
  log("Processing file decryption:", level="processing")
  for file in tqdm(files, desc="Decrypting files"):
    file_path = os.path.join(directory, file)

    if check_permissions(file_path):
      decryption(file_path, crypto_key, suffix)
    else:
      log(f"Skipping file due to insufficient permissions: {file}", level="error")
  
  log(f"All files have been successfully decrypted.", level="success")
