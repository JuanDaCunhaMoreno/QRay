import qrcode, cv2

def gerar_qr(dados, nome_arquivo= "qrcode.png"):
#Gera um QR code com dados fornecidos e salva como PNG.
    qr = qrcode.QRCode(
        version=1, #Versão do QR Code (1 = menor, até 40 = maior)
        error_correction=qrcode.constants.ERROR_CORRECT_L, #Correção de erro (L = Low)
        box_size=10, #Tamanho de cada "caixa" do QR code
        border=4 #Margem ao redor do QR code
    )

    
    qr.add_data(dados) #Adiciona os dados (Texto ou URL)
    qr.make(fit=True) #Gera o QR code com base nos dados

    imagem = qr.make_image(fill_collor="black", black_color="white") #cria a imagem
    imagem.save(nome_arquivo) #Salva a imagem como arquino PNG
    print(f"✅QR Code salvo como: {nome_arquivo}")

def decodificar_qr(nome_arquivo):
# Lê imagem com QR code e imprime o conteúdo decodificado.
    imagem = cv2.imread(nome_arquivo) # Carrega a imagem com OpenCV
    detector = cv2.QRCodeDetector() #Cria o detector de QR code

    dados, pontos, _ = detector.detectAndDecode(imagem) #Detecta e decodifica
    if dados:
        print(f"🔍 Dados decodificados do QR Code: {dados}")
    else:
        print("❌ Nenhum QR Code detectado na imagem.")
