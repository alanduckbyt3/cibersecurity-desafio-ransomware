#!/bin/bash
if [ -f "./venv/bin/activate" ]; then
  echo "Ativando o ambiente virtual..."
  source ./venv/bin/activate
else
  echo "Ambiente virtual não encontrado."
  echo "Crie um ambiente virtual com 'python3 -m venv venv'"
fi
