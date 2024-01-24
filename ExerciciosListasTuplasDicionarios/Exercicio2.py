# Inicializa uma lista para armazenar as médias dos alunos
medias_alunos = []

# Loop para coletar as notas de cada aluno
for i in range(5):
    notas = []
    
    # Solicita ao usuário as quatro notas do aluno
    for j in range(4):
        nota = float(input(f"Digite a nota {j + 1} do aluno {i + 1}: "))
        notas.append(nota)
    
    # Calcula a média e armazena na lista de médias
    media = sum(notas) / len(notas)
    medias_alunos.append(media)

# Cria um dicionário para armazenar o número do aluno e sua média
alunos_dict = {i + 1: media for i, media in enumerate(medias_alunos)}

# Encontra o número do aluno com média maior ou igual a 7.0
alunos_aprovados = [num for num, media in alunos_dict.items() if media >= 7.0]

# Imprime o número do(s) aluno(s) aprovado(s)
if alunos_aprovados:
    print(f"O(s) aluno(s) {', '.join(map(str, alunos_aprovados))} obteve(ram) média maior ou igual a 7.0.")
else:
    print("Nenhum aluno obteve média maior ou igual a 7.0.")
