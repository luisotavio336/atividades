usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")

if (usuario == "procopio" and senha == "12345") or \
   (usuario == "paiva" and senha == "54321"):
    print("Seja bem vindo!")
else:
    print("Usuário e senha não conferem")