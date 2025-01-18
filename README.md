# SafeRansom 🔐💻

<p align="center"><b>SafeRansom</b> é um projeto educacional criado para demonstrar os princípios básicos de criptografia e descriptografia de arquivos, simulando de forma controlada o comportamento de um ransomware "entre aspas".</p>
<p align="center"><b>Atenção</b>: Este projeto é destinado apenas para fins educacionais, proposto pelo professor Cassiano da DIO Academy no Bootcamp de Cibersegurança do Santander. Não deve ser utilizado para fins maliciosos ou ilegais.
 O autor não se responsabiliza por qualquer uso indevido do código.</p>

---

## ⚙️ Funcionalidades
- Criptografa arquivos no diretório atual utilizando **AES (Advanced Encryption Standard)** no modo **CTR (Counter)**.
- Descriptografa arquivos previamente criptografados.
- Respeita configurações definidas pelo usuário no arquivo `.env`, como extensões de arquivos permitidos, sufixo ao encriptar um arquivo e arquivos ignorados.
- Permite o uso de uma chave personalizada definida pelo usuário.

---

## 🐱‍👤 Como o SafeRansom Funciona
O projeto utiliza o algoritmo **AES** no modo **CTR**, um método de criptografia amplamente seguro e eficiente:
- Durante a **criptografia**, cada arquivo recebe um **nonce** (Número Usado Uma Vez) único que, combinado com a chave, garante que cada arquivo criptografado seja único e seguro.
- Na **descriptografia**, o nonce armazenado no arquivo criptografado é utilizado para reverter o processo e restaurar os dados originais.
- **AES-CTR** é ideal para este propósito porque funciona como um cifrador de fluxo, permitindo criptografia sem necessidade de preenchimento (padding).

---

## 🛠 Requisitos
- **Python 3.8+**.
- **Ambiente virtual (venv)**:
  - Crie usando: `python -m venv venv` (Windows) ou `python3 -m venv venv` (Linux).
  - Ative com:
    - Windows (PowerShell): `.\venv\Scripts\Activate.ps1`
    - Linux: `source venv/bin/activate`
  - Desative com: `deactivate`
- **Bibliotecas necessárias**:
  - `pycryptodome`
  - `tqdm`
  - `python-dotenv`

Para instalar as dependências:
```bash
pip install -r requirements.txt
```

---

## 💡 Como Usar
1. Clone o repositório:
   ```bash
   git clone https://github.com/alanduckbyt3/cybersecurity-desafio-ransomware.git
   ```
2. Acesse o diretório do projeto:
   ```bash
   cd cybersecurity-desafio-ransomware
   ```
3. Configure o arquivo `.env`:
   ```env
   CRYPTO_KEY=chave_de_16_24_ou_32_caracteres
   IGNORED_FILES=requirements.txt
   SUFFIX=.ransomwaretroll
   VALID_EXTENSIONS=.txt,.pdf
   ```
4. Execute o script principal:
   ```bash
   python main.py
   ```

---

## ⚠ Avisos e Problemas Comuns
- Possui dois scripts auxiliares, caso você queira ativar o venv rapidamente: `activate.ps1` (PowerShell) para windows e `activate.sh` (Shell) para Linux.
- **Erro no PowerShell (Windows)**: Caso enfrente restrições de execução, use o comando:
  ```bash
  Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
  ```
  Isso permitirá executar scripts locais apenas na sessão atual, sem alterar a política global.
- Certifique-se de que os arquivos estejam no mesmo diretório do projeto antes de executar o script.

---

## 🔎 Limitações
- Funciona apenas no diretório atual, sem suporte a subdiretórios.
- A chave de criptografia deve ser fornecida manualmente pelo usuário.
- Projeto básico e intencionalmente limitado para fins educacionais.

---

## 🏗️ Estrutura do Projeto
- `main.py`: Ponto de entrada principal do projeto.
- `encrypt_main.py`: Script de exemplo completo para criptografia.
- `decrypt_main.py`: Script de exemplo completo para descriptografia.
- `utils/encryptUtils.py`: Funções para criptografia de arquivos.
- `utils/decryptUtils.py`: Funções para descriptografia de arquivos.
- `utils/file_management/file_utils.py`: Gerenciamento de arquivos e permissões.
- `utils/logging/log.py`: Sistema de logs no terminal.
- `utils/file_management/clear_term.py`: Função para limpar o terminal.

---

## ⚖️ Licença
Este projeto está licenciado sob a [Licença MIT](LICENSE). Consulte o arquivo para mais informações.

---

👉 **Nota**: Use este projeto com responsabilidade e sempre respeite as leis aplicáveis. Se você deseja fazer melhorias ou enviar sugestões e feedback, fique à vontade.
