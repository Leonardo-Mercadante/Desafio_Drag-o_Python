# Solicitando ao usuário o número de casos de teste
C = int(input())

# Criando o loop pelos casos de teste
for _ in range(C):
    # Lendo o nível de energia do ser vivo
    N = int(input())
    
    # Verificando o nível de energia e imprime a saída correspondente
    if N <= 8000:
        print("Inseto!")
    else:
        print("Mais de 8000!")