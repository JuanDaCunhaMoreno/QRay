# QR Toolkit 🧩

Um simples gerador e leitor de QR Codes em Python usando `qrcode` e `OpenCV`.

## 📦 Requisitos

- Python 3.8 ou superior
- Bibliotecas:
  - qrcode[pil]
  - opencv-python

# 🚀 Como usar
Você verá um menu com 3 opções:

1. Gerar QR Code – digite um texto ou link e o programa salvará uma imagem com o código.
2. Ler QR Code – informe o nome da imagem contendo um QR code e o programa mostrará o conteúdo.
3. Sair

# 📁 Estrutura dos arquivos

qr_code_project/
├── main.py         # Programa principal com o menu
├── utils.py     # Funções para gerar e decodificar QR Codes
└── README.md       # Este arquivo
