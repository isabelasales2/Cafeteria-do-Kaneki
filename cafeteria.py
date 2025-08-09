# Cafeteria do Kaneki - Tokyo Ghoul

# Informações da cafeteria
nome_cafeteria = "Anteiku"

# Menu com preços
menu = {
    "Café preto": 5,
    "Cappuccino": 8,
    "Matchá latte": 6
}

# Lista para guardar os valores das vendas
vendas = []

print(f"Bem-vindo à {nome_cafeteria}!")

while True:
    print("\nMenu:")
    for i, item in enumerate(menu, 1):
        print(f"{i} - {item}: R${menu[item]}")

    pedido = input("Digite o número do item que deseja pedir (ou 'sair' para encerrar): ")

    if pedido.lower() == "sair":
        break

    if pedido.isdigit():
        numero = int(pedido)
        if 1 <= numero <= len(menu):
            # Pegando o item e preço pelo número digitado
            item = list(menu.keys())[numero - 1]
            preco = menu[item]
            vendas.append(preco)
            print(f"Você pediu {item}. Total: R${preco}")
        else:
            print("Número inválido. Tente novamente.")
    else:
        print("Por favor, digite um número válido.")

# Mostrar total do caixa
total = sum(vendas)
print(f"\nTotal arrecadado: R${total}")
print("Obrigado pela visita!")