from utils import gerar_qr, decodificar_qr

def menu():
    while True:
        print("\n=== QR Code Tool ===")
        print("[1] Gerar QR Code")
        print("[2] Ler QR Code")
        print("[3] Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            texto = input("Digite o texto ou URL para codificar: ")
            nome = input("Nome do arquivo para salvar: ")
            gerar_qr(texto, nome)
        elif opcao == "2":
            nome = input('Nome do arquivo da imagem com QR Code: ')
            decodificar_qr(nome)
        elif opcao == "3":
            print("Encerrando...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()
