# GABARITO - ENCONTRO 1: Algoritmos + Hello, World!
# Monitoria de Python - Engenharia da Computação

"""
GABARITO COMPLETO
Soluções comentadas para todos os exercícios
"""

print("=== GABARITO - ENCONTRO 1 ===")
print()

# ======================================
# EXERCÍCIO 1 - SAUDAÇÃO SIMPLES
# ======================================
print("1. SAUDAÇÃO SIMPLES")
print("=" * 30)

# Solução:
nome = input("Digite seu nome: ")
print("Bom dia,", nome, "!")

print("\n💡 EXPLICAÇÃO:")
print("- input() coleta o nome como string")
print("- print() exibe com vírgulas para separar os elementos")
print("- Alternativa: print('Bom dia, ' + nome + '!')")
print()

print("-" * 50)

# ======================================
# EXERCÍCIO 2 - APRESENTAÇÃO COMPLETA  
# ======================================
print("2. APRESENTAÇÃO COMPLETA")
print("=" * 30)

# Solução:
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")  
cidade = input("Digite sua cidade: ")

print("Meu nome é", nome, ", tenho", idade, "anos e moro em", cidade, ".")

print("\n💡 EXPLICAÇÃO:")
print("- Coletamos três informações em variáveis separadas")
print("- Usamos vírgulas no print() para juntar tudo")
print("- Cuidado com espaços e pontuação na saída")
print()

print("-" * 50)

# ======================================
# EXERCÍCIO 3 - EXPLORADOR DE TIPOS
# ======================================
print("3. EXPLORADOR DE TIPOS")
print("=" * 30)

# Solução:
# Coletando três valores diferentes
valor1 = input("Digite um texto qualquer: ")
valor2 = input("Digite um número: ")
valor3 = input("Digite sua idade: ")

# Mostrando valores e tipos
print("Valor 1:", valor1, "- Tipo:", type(valor1))
print("Valor 2:", valor2, "- Tipo:", type(valor2))  
print("Valor 3:", valor3, "- Tipo:", type(valor3))

print("\n💡 EXPLICAÇÃO:")
print("- Todos os valores do input() são strings (str)")
print("- Mesmo números digitados ficam como texto")
print("- type() sempre mostra <class 'str'> para input()")
print()

print("-" * 50)

# ======================================
# EXERCÍCIO 4 - MÚLTIPLAS SAÍDAS
# ======================================
print("4. MÚLTIPLAS SAÍDAS")
print("=" * 30)

# Solução:
comida = input("Digite sua comida favorita: ")

# Três formas diferentes de exibir
print("Eu gosto de", comida)
print("Minha comida favorita é:", comida)
print("Comida:", comida)

print("\n💡 EXPLICAÇÃO:")
print("- Podemos usar a mesma variável em prints diferentes")
print("- Cada print() gera uma linha nova")
print("- Varie as frases para ficar mais interessante")
print()

print("-" * 50)

# ======================================
# EXERCÍCIO 5 - CALCULADORA DE APRESENTAÇÃO
# ======================================
print("5. CALCULADORA DE APRESENTAÇÃO")
print("=" * 30)

# Solução:
nome = input("Digite seu nome: ")
ano_nascimento = input("Digite seu ano de nascimento: ")
ano_atual = input("Digite o ano atual: ")

# Convertendo para números para calcular
# (Conceito que veremos melhor no próximo encontro)
nascimento_num = int(ano_nascimento)
atual_num = int(ano_atual)
idade_aprox = atual_num - nascimento_num

print("Olá", nome, "!")
print("Você nasceu em", ano_nascimento)
print("Sua idade aproximada é", idade_aprox, "anos")

print("\n💡 EXPLICAÇÃO:")
print("- Usamos int() para converter strings em números")
print("- Fazemos a subtração para calcular a idade")
print("- É aproximada porque não consideramos mês/dia")
print("- int() será explicado em detalhes no Encontro 2")
print()

print("-" * 50)

# ======================================
# EXERCÍCIO 6 - INVESTIGADOR DE DADOS
# ======================================
print("6. INVESTIGADOR DE DADOS")
print("=" * 30)

# Solução:
print("=== COLETANDO INFORMAÇÕES ===")
nome = input("Nome: ")
idade = input("Idade: ")
altura = input("Altura (ex: 1.75): ")
tem_irmao = input("Tem irmão? (sim/não): ")

print("\n=== RELATÓRIO DE DADOS ===")
print("Nome:", nome, "| Tipo:", type(nome))
print("Idade:", idade, "| Tipo:", type(idade))
print("Altura:", altura, "| Tipo:", type(altura))
print("Tem irmão:", tem_irmao, "| Tipo:", type(tem_irmao))

print("\n💡 EXPLICAÇÃO:")
print("- Organizamos as informações de forma clara")
print("- Todos os tipos são <class 'str'> (string)")
print("- Usamos | para separar valor e tipo visualmente")
print()

print("-" * 50)

# ======================================
# DESAFIO EXTRA 🚀
# ======================================
print("DESAFIO EXTRA 🚀")
print("=" * 30)

# Solução:
nome = input("Nome: ")
tem_irmao_texto = input("Tem irmão? Digite 'True' ou 'False': ")

print("Nome:", nome, "- Tipo:", type(nome))
print("Tem irmão:", tem_irmao_texto, "- Tipo:", type(tem_irmao_texto))

# Descoberta interessante:
print("\n🔍 DESCOBERTA:")
print("Mesmo digitando 'True' ou 'False', o tipo ainda é string!")
print("Para ser boolean de verdade, precisaríamos converter")
print("Isso será visto em encontros futuros!")

print("\n💡 EXPLICAÇÃO:")
print("- input() SEMPRE retorna string, mesmo que pareça boolean")
print("- 'True' (texto) ≠ True (boolean)")
print("- Para converter, usaríamos eval() ou comparações")
print("- Mas isso é tópico avançado para mais tarde!")
print()

print("=" * 50)

# ======================================
# DICAS GERAIS DO GABARITO
# ======================================
print("\n🎯 DICAS IMPORTANTES:")
print("1. Todos os inputs retornam strings")
print("2. Use vírgulas no print() para separar elementos") 
print("3. Comentários ajudam a entender o código")
print("4. Teste sempre seus programas")
print("5. Organize a saída para ficar legível")

print("\n🚀 PRÓXIMOS PASSOS:")
print("- Pratique modificando esses códigos")
print("- Tente combinar exercícios")
print("- No Encontro 2: aprenderemos conversões de tipos!")

print("\n=== FIM DO GABARITO ===")