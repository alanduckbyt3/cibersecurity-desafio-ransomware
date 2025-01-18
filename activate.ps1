if (Test-Path ".\venv\Scripts\Activate.ps1") {
  Write-Host "Ativando o ambiente virtual..."
  . .\venv\Scripts\Activate.ps1
} else {
  Write-Host "Ambiente virtual não encontrado."
  Write-Host "Crie um ambiente virtual com 'python -m venv venv'"
}
