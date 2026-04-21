# Lista para armazenar doações
doacoes = []

# Cadastro de doação
for i in range(3):  # quantidade de usuários (pode mudar)
    print(f"\nCadastro {i+1}")
    
    nome = input("Nome do doador: ")
    alimento = input("Alimento doado: ")
    quantidade = int(input("Quantidade: "))
    
    doacao = {
        "nome": nome,
        "alimento": alimento,
        "quantidade": quantidade
    }
    
    doacoes.append(doacao)

# Mostrar doações cadastradas
print("\n=== Lista de Doações ===")
for d in doacoes:
    print(f"{d['nome']} doou {d['quantidade']} de {d['alimento']}")
