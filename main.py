import os
from dotenv import load_dotenv
from utils.logging import log
from utils.decryptUtils import decrypt_files
from utils.encryptUtils import encrypt_files

def display_menu():
  print("\n" + "=" * 60)
  print("""
    ███████╗ █████╗ ███████╗███████╗                      
    ██╔════╝██╔══██╗██╔════╝██╔════╝                      
    ███████╗███████║█████╗  █████╗                        
    ╚════██║██╔══██║██╔══╝  ██╔══╝                          
    ███████║██║  ██║██║     ███████╗                      
    ╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝                      
    ██████╗  █████╗ ███╗   ██╗███████╗ ██████╗ ███╗   ███╗
    ██╔══██╗██╔══██╗████╗  ██║██╔════╝██╔═══██╗████╗ ████║
    ██████╔╝███████║██╔██╗ ██║███████╗██║   ██║██╔████╔██║
    ██╔══██╗██╔══██║██║╚██╗██║╚════██║██║   ██║██║╚██╔╝██║
    ██║  ██║██║  ██║██║ ╚████║███████║╚██████╔╝██║ ╚═╝ ██║
    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝     ╚═╝                                                   
  """)
  print("=" * 60)
  print("              FILE ENCRYPTION & DESCRYPTION TOOL")
  print("=" * 60)
  print("\n[1] Encrypt Files")
  print("[2] Decrypt Files")
  print("[3] Exit\n")
  print("=" * 60)

  while True:
    choice = input(">> Select an option: ").strip() 
    if choice.isdigit():
      num = int(choice)
      if 1 <= num <= 3:
        return num
    else:
      print("\nSelect numbers only ( 1, 2, or 3. )\n")


def main():
  """
  Script principal para carregar as configurações e iniciar o processo da criptografia dos arquivos.
  """
  
  load_dotenv()

  try:
    # Carrega a chave de criptografia do .env
    crypto_key = os.getenv('CRYPTO_KEY')
    if not crypto_key or len(crypto_key) not  in [16, 24, 32]:
      raise ValueError("'CRYPTO_KEY' must be between 16, 24 or 32 characters.")
    
    # Converte a chave em bytes
    crypto_key = bytes(crypto_key.encode())
    suffix = os.getenv('SUFFIX', '.ransomwaretroll')
    valid_extensions = [ext.lstrip('.') for ext in os.getenv('VALID_EXTENSIONS', '.txt,.pdf').split(',')]

    # Define o diretório atual como alvo
    directory = os.getcwd()

    # Exibe o menu e executa a ação selecionada pelo usuário
    choice = display_menu()
    if choice == 1:
      encrypt_files(directory, crypto_key, suffix, valid_extensions)
    elif choice == 2:
      decrypt_files(directory, crypto_key, suffix, valid_extensions)
    else:
      print("\nGoodbye, Neo. I hope you find what you're looking for.")
      exit()

  except Exception as e:
    # Registra erros de configuração ou execução
    log(f"Execution or configuration error: {e.__class__.__name__} - {e}", level="error")


if __name__ == "__main__":
  main()
