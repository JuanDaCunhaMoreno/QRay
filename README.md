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

# 🧪 Exemplo de uso

1. Escolha "1" no menu e digite:

   - Texto: https://example.com

   - Nome do arquivo: meuqrcode.png

2. Abra novamente e escolha "2", digite:

   - Nome do arquivo: meuqrcode.png

O texto original será exibido no terminal.
