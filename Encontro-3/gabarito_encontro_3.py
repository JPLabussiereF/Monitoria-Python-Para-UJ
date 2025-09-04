# GABARITO - ENCONTRO 3: Operadores aritméticos, comparação e lógicos
# Monitoria de Python - Engenharia da Computação

"""
GABARITO COMPLETO
Soluções comentadas focando nos 3 tipos de operadores
"""

print("=== GABARITO - ENCONTRO 3 ===")
print()

# ======================================
# EXERCÍCIO 1 - CALCULADORA BÁSICA
# ======================================
print("1. CALCULADORA BÁSICA")
print("=" * 30)

# Solução:
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print(f"\n=== TODOS OS OPERADORES ARITMÉTICOS ===")
print(f"{num1} + {num2} = {num1 + num2}")      # Adição
print(f"{num1} - {num2} = {num1 - num2}")      # Subtração  
print(f"{num1} * {num2} = {num1 * num2}")      # Multiplicação
print(f"{num1} / {num2} = {num1 / num2}")      # Divisão real
print(f"{num1} // {num2} = {num1 // num2}")    # Divisão inteira
print(f"{num1} % {num2} = {num1 % num2}")      # Resto (módulo)
print(f"{num1} ** {num2} = {num1 ** num2}")    # Potenciação

print("\n💡 EXPLICAÇÃO:")
print("- / sempre retorna float, mesmo com números inteiros")
print("- // descarta a parte decimal (floor division)")
print("- % retorna o resto da divisão inteira")
print("- ** é o operador de potenciação (não ^)")
print("- Cuidado com divisão por zero!")
print()

print("-" * 50)

# ======================================
# EXERCÍCIO 2 - DETECTOR DE PAR/ÍMPAR  
# ======================================
print("2. DETECTOR DE PAR/ÍMPAR")
print("=" * 30)

# Solução:
numero = int(input("Digite um número inteiro: "))

# Usando operador módulo
resto = numero % 2
eh_par = resto == 0
eh_impar = not eh_par  # Alternativa: resto != 0

print(f"\nNúmero: {numero}")
print(f"Resto da divisão por 2: {resto}")
print(f"É par: {eh_par}")
print(f"É ímpar: {eh_impar}")

# Versão mais direta
if numero % 2 == 0:
    print("✅ Confirmação: Número PAR")
else:
    print("✅ Confirmação: Número ÍMPAR")

print("\n💡 EXPLICAÇÃO:")
print("- numero % 2 calcula resto da divisão por 2")
print("- Se resto = 0, o número é par")
print("- Se resto = 1, o número é ímpar") 
print("- Usamos operador == para comparar com 0")
print("- not inverte o valor boolean")
print()

print("-" * 50)

# ======================================
# EXERCÍCIO 3 - COMPARADOR DE IDADES
# ======================================
print("3. COMPARADOR DE IDADES")
print("=" * 30)

# Solução:
print("=== COLETANDO IDADES ===")
idade1 = int(input("Primeira idade: "))
idade2 = int(input("Segunda idade: "))
idade3 = int(input("Terceira idade: "))

print(f"\nIdades coletadas: {idade1}, {idade2}, {idade3}")

# Usando operadores de comparação
maior_idade = max(idade1, idade2, idade3)  # Função auxiliar
menor_idade = min(idade1, idade2, idade3)  # Função auxiliar

# Versão manual com comparadores
if idade1 >= idade2 and idade1 >= idade3:
    maior_manual = idade1
elif idade2 >= idade1 and idade2 >= idade3:
    maior_manual = idade2
else:
    maior_manual = idade3

# Contando maiores de idade usando operadores lógicos
maiores_18 = 0
if idade1 >= 18:
    maiores_18 += 1
if idade2 >= 18:
    maiores_18 += 1  
if idade3 >= 18:
    maiores_18 += 1

# Verificando idades iguais
todas_iguais = idade1 == idade2 == idade3
pelo_menos_duas_iguais = idade1 == idade2 or idade1 == idade3 or idade2 == idade3

print("\n=== ANÁLISE DAS IDADES ===")
print(f"Maior idade: {maior_idade}")
print(f"Menor idade: {menor_idade}")
print(f"Maiores de idade (>=18): {maiores_18} pessoa(s)")
print(f"Todas iguais: {todas_iguais}")
print(f"Pelo menos duas iguais: {pelo_menos_duas_iguais}")

print("\n💡 EXPLICAÇÃO:")
print("- Usamos >= para 'maior ou igual' (inclusive)")
print("- == compara se valores são exatamente iguais")
print("- Operadores podem ser encadeados: a == b == c")
print("- or retorna True se pelo menos uma condição for verdadeira")
print()

print("-" * 50)

# ======================================
# EXERCÍCIO 4 - TABELA-VERDADE PERSONALIZADA
# ======================================
print("4. TABELA-VERDADE PERSONALIZADA")
print("=" * 40)

# Solução:
print("Digite valores boolean (True ou False)")
valor_a_str = input("Primeiro valor: ")
valor_b_str = input("Segundo valor: ")

# Convertendo strings para boolean
valor_a = valor_a_str.lower() == "true"
valor_b = valor_b_str.lower() == "true"

print(f"\nValores: A = {valor_a}, B = {valor_b}")

# Construindo tabela-verdade completa
print("\n" + "=" * 40)
print("       TABELA-VERDADE COMPLETA")
print("=" * 40)
print(f"A = {valor_a} | B = {valor_b}")
print("-" * 40)
print(f"A and B  = {valor_a} and {valor_b}  = {valor_a and valor_b}")
print(f"A or B   = {valor_a} or {valor_b}   = {valor_a or valor_b}")
print(f"not A    = not {valor_a}            = {not valor_a}")
print(f"not B    = not {valor_b}            = {not valor_b}")
print(f"A and not B = {valor_a} and not {valor_b} = {valor_a and not valor_b}")
print(f"not A or B  = not {valor_a} or {valor_b}  = {not valor_a or valor_b}")
print("=" * 40)

# Explicações dos resultados
print("\n=== EXPLICAÇÃO DOS RESULTADOS ===")
if valor_a and valor_b:
    print("✅ AND: Ambos são verdadeiros")
elif valor_a or valor_b:
    print("⚠️ AND: Pelo menos um é falso, então AND = False")
    print("✅ OR: Pelo menos um é verdadeiro")
else:
    print("❌ AND e OR: Ambos são falsos")

print("\n💡 EXPLICAÇÃO:")
print("- AND só é True quando AMBOS são True")
print("- OR é True quando PELO MENOS UM é True")  
print("- NOT inverte: True vira False, False vira True")
print("- Precedência: not > and > or")
print()

print("-" * 50)

# ======================================
# EXERCÍCIO 5 - CALCULADORA DE MÉDIA COM VALIDAÇÃO
# ======================================
print("5. CALCULADORA DE MÉDIA COM VALIDAÇÃO")
print("=" * 45)

# Solução:
print("=== SISTEMA DE NOTAS (0-10) ===")
nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))  
nota3 = float(input("Terceira nota: "))
nota4 = float(input("Quarta nota: "))

# Validação usando operadores lógicos e de comparação
nota1_valida = 0 <= nota1 <= 10
nota2_valida = 0 <= nota2 <= 10
nota3_valida = 0 <= nota3 <= 10
nota4_valida = 0 <= nota4 <= 10

todas_notas_validas = nota1_valida and nota2_valida and nota3_valida and nota4_valida

print("\n=== VALIDAÇÃO DAS NOTAS ===")
print(f"Nota 1 válida (0-10): {nota1_valida}")
print(f"Nota 2 válida (0-10): {nota2_valida}")
print(f"Nota 3 válida (0-10): {nota3_valida}")
print(f"Nota 4 válida (0-10): {nota4_valida}")
print(f"Todas válidas: {todas_notas_validas}")

if todas_notas_validas:
    # Cálculos usando operadores aritméticos
    media = (nota1 + nota2 + nota3 + nota4) / 4
    
    # Determinando status com operadores de comparação
    aprovado = media >= 7.0
    exame = 5.0 <= media < 7.0  # Combinando comparadores
    reprovado = media < 5.0
    
    print(f"\n=== RESULTADO ===")
    print(f"Média: {round(media, 2)}")
    print(f"Aprovado (>=7.0): {aprovado}")
    print(f"Exame (5.0-6.9): {exame}")
    print(f"Reprovado (<5.0): {reprovado}")
    
    # Status final usando operadores lógicos
    if aprovado:
        print("🎉 STATUS: APROVADO DIRETO!")
    elif exame:
        print("📚 STATUS: EXAME FINAL")
    else:
        print("❌ STATUS: REPROVADO")
else:
    print("❌ ERRO: Corrija as notas inválidas!")

print("\n💡 EXPLICAÇÃO:")
print("- Usamos <= e >= para intervalos inclusivos")
print("- Combinamos comparadores: 5.0 <= media < 7.0")
print("- and garante que TODAS as condições sejam verdadeiras")
print("- elif evita verificações desnecessárias (lógica exclusiva)")
print()

print("-" * 50)

# ======================================
# EXERCÍCIO 6 - ANALISADOR DE NÚMEROS
# ======================================
print("6. ANALISADOR DE NÚMEROS")
print("=" * 30)

# Solução:
numero = int(input("Digite um número para análise: "))

# Análises usando operadores de comparação
eh_positivo = numero > 0
eh_negativo = numero < 0  
eh_zero = numero == 0

# Análises usando módulo
eh_par = numero % 2 == 0
eh_impar = not eh_par

# Múltiplos usando operadores lógicos
multiplo_3 = numero % 3 == 0
multiplo_5 = numero % 5 == 0
multiplo_3_e_5 = multiplo_3 and multiplo_5  # Múltiplo de 15
multiplo_3_ou_5 = multiplo_3 or multiplo_5

print(f"\n=== ANÁLISE DO NÚMERO {numero} ===")
print(f"É positivo: {eh_positivo}")
print(f"É negativo: {eh_negativo}")
print(f"É zero: {eh_zero}")
print(f"É par: {eh_par}")
print(f"É ímpar: {eh_impar}")
print(f"Múltiplo de 3: {multiplo_3}")
print(f"Múltiplo de 5: {multiplo_5}")
print(f"Múltiplo de 3 E 5 (15): {multiplo_3_e_5}")
print(f"Múltiplo de 3 OU 5: {multiplo_3_ou_5}")

# Classificação especial (tipo FizzBuzz)
print(f"\n=== CLASSIFICAÇÃO ESPECIAL ===")
if multiplo_3_e_5:
    print("FizzBuzz! (múltiplo de 3 e 5)")
elif multiplo_3:
    print("Fizz! (múltiplo de 3)")
elif multiplo_5:
    print("Buzz! (múltiplo de 5)")
else:
    print("Número normal")

print("\n💡 EXPLICAÇÃO:")
print("- % 3 == 0 verifica se é múltiplo de 3")
print("- and combina condições (AMBAS verdadeiras)")
print("- or verifica pelo menos uma (QUALQUER verdadeira)")
print("- elif cria lógica mutuamente exclusiva")
print("- Múltiplo de 3 E 5 = múltiplo de 15")
print()

print("-" * 50)

# ======================================
# EXERCÍCIO 7 - SISTEMA DE LOGIN SIMPLES
# ======================================
print("7. SISTEMA DE LOGIN SIMPLES")
print("=" * 35)

# Solução:
print("=== SISTEMA DE LOGIN ===")
usuario = input("Nome de usuário: ")
senha = input("Senha: ")

# Validações usando operadores de comparação e lógicos
usuario_valido = len(usuario) >= 5
senha_comprimento_ok = len(senha) >= 8

# Verificando se senha contém números
senha_tem_numero = any(char.isdigit() for char in senha)  # Avançado
# Versão alternativa mais básica:
senha_tem_numero_basico = False
for char in senha:
    if char.isdigit():
        senha_tem_numero_basico = True
        break

senha_valida = senha_comprimento_ok and senha_tem_numero

# Acesso final usando operadores lógicos
acesso_liberado = usuario_valido and senha_valida

print(f"\n=== VALIDAÇÕES ===")
print(f"Usuário (>= 5 chars): {usuario_valido}")
print(f"Senha comprimento (>= 8): {senha_comprimento_ok}")
print(f"Senha tem número: {senha_tem_numero}")
print(f"Senha válida: {senha_valida}")
print(f"ACESSO LIBERADO: {acesso_liberado}")

print(f"\n=== RESULTADO ===")
if acesso_liberado:
    print("🔓 ACESSO PERMITIDO!")
    print(f"Bem-vindo, {usuario}!")
else:
    print("🔒 ACESSO NEGADO!")
    if not usuario_valido:
        print("- Usuário deve ter pelo menos 5 caracteres")
    if not senha_comprimento_ok:
        print("- Senha deve ter pelo menos 8 caracteres")
    if not senha_tem_numero:
        print("- Senha deve conter pelo menos um número")

print("\n💡 EXPLICAÇÃO:")
print("- len() retorna quantidade de caracteres")
print("- >= compara se comprimento é suficiente")
print("- any() verifica se pelo menos um char atende critério")
print("- and garante que TODOS os critérios sejam atendidos")
print("- not inverte resultado para mostrar o que está errado")
print()

print("-" * 50)

# ======================================
# EXERCÍCIO 8 - CALCULADORA DE DESCONTO INTELIGENTE
# ======================================
print("8. CALCULADORA DE DESCONTO INTELIGENTE")
print("=" * 50)

# Solução:
print("=== SISTEMA E-COMMERCE ===")
preco_unitario = float(input("Preço unitário do produto: R$ "))
quantidade = int(input("Quantidade: "))

# Cálculos básicos com operadores aritméticos
subtotal = preco_unitario * quantidade

# Desconto progressivo usando operadores de comparação
desconto_percentual = 0
if subtotal > 1000:
    desconto_percentual = 15
elif subtotal > 500:
    desconto_percentual = 10  
elif subtotal > 100:
    desconto_percentual = 5

# Cálculo do desconto
desconto_valor = subtotal * desconto_percentual / 100
total_com_desconto = subtotal - desconto_valor

# Frete usando operador de comparação
frete = 0 if total_com_desconto > 200 else 15
total_final = total_com_desconto + frete

# Análises usando operadores lógicos
frete_gratis = total_com_desconto > 200
tem_desconto = desconto_percentual > 0
compra_vantajosa = tem_desconto and frete_gratis

print(f"\n=== CÁLCULO DO PEDIDO ===")
print(f"Subtotal: R$ {round(subtotal, 2)}")
print(f"Desconto: {desconto_percentual}% = R$ {round(desconto_valor, 2)}")
print(f"Total com desconto: R$ {round(total_com_desconto, 2)}")
print(f"Frete: R$ {frete} {'(GRÁTIS!)' if frete == 0 else ''}")
print(f"TOTAL FINAL: R$ {round(total_final, 2)}")

print(f"\n=== ANÁLISE DA COMPRA ===")
print(f"Tem desconto: {tem_desconto}")
print(f"Frete grátis: {frete_gratis}")
print(f"Compra vantajosa: {compra_vantajosa}")

# Recomendações usando operadores
if not frete_gratis and total_com_desconto > 150:
    faltam = 200 - total_com_desconto
    print(f"💡 Dica: Adicione R$ {round(faltam, 2)} para frete grátis!")

if subtotal > 90 and subtotal <= 100:
    print("💡 Dica: Adicione R$ 10+ para 5% de desconto!")

print("\n💡 EXPLICAÇÃO:")
print("- elif cria condições mutuamente exclusivas")
print("- Operador ternário: valor_se_verdadeiro if condição else valor_se_falso") 
print("- and combina múltiplas condições positivas")
print("- Comparações podem ser usadas em cálculos")
print("- <= inclui o valor limite na comparação")
print()

print("-" * 50)

# ======================================
# DESAFIO EXTRA 🚀
# ======================================
print("DESAFIO EXTRA 🚀")
print("=" * 30)

# Solução:
print("=== JOGO DE ADIVINHAÇÃO MATEMÁTICA ===")
print("Vou apresentar expressões matemáticas.")
print("Você deve adivinhar se o resultado é True ou False!")

# Lista de expressões para testar
expressoes = [
    ("5 > 3 and 2 == 2", 5 > 3 and 2 == 2),
    ("10 % 3 == 1", 10 % 3 == 1),
    ("not (False or True)", not (False or True)),
    ("15 // 4 >= 3", 15 // 4 >= 3),
    ("'Python' != 'python'", 'Python' != 'python'),
]

pontuacao = 0
total_questoes = len(expressoes)

for i, (expressao_str, resultado_real) in enumerate(expressoes, 1):
    print(f"\nQuestão {i}: {expressao_str}")
    resposta_usuario = input("True ou False? ").lower() == "true"
    
    if resposta_usuario == resultado_real:
        print(f"✅ CORRETO! {expressao_str} = {resultado_real}")
        pontuacao += 1
    else:
        print(f"❌ ERRADO! {expressao_str} = {resultado_real}")

# Resultado final usando operadores
percentual = (pontuacao / total_questoes) * 100
passou = pontuacao >= total_questoes * 0.6  # 60% para passar
performance_excelente = pontuacao == total_questoes

print(f"\n=== RESULTADO FINAL ===")
print(f"Acertos: {pontuacao}/{total_questoes}")
print(f"Percentual: {round(percentual, 1)}%")
print(f"Passou (>=60%): {passou}")
print(f"Performance excelente: {performance_excelente}")

if performance_excelente:
    print("🏆 PARABÉNS! Você domina operadores!")
elif passou:
    print("👍 BOM TRABALHO! Continue praticando!")
else:
    print("📚 ESTUDE MAIS! Revise operadores lógicos!")

print("\n💡 EXPLICAÇÃO:")
print("- Expressões são avaliadas seguindo precedência")
print("- Parênteses alteram ordem de avaliação")
print("- Strings são case-sensitive ('Python' != 'python')")
print("- // retorna resultado da divisão inteira")
print("- % retorna resto da divisão")
print("- Operadores lógicos seguem precedência: not > and > or")
print()

print("=" * 60)

# ======================================
# RESUMO FINAL DO GABARITO
# ======================================
print("\n🎯 RESUMO DOS OPERADORES DOMINADOS:")

print("\n📊 ARITMÉTICOS:")
print("✅ + (adição), - (subtração), * (multiplicação)")
print("✅ / (divisão real), // (divisão inteira), % (resto)")  
print("✅ ** (potenciação)")

print("\n🔍 COMPARAÇÃO:")
print("✅ == (igual), != (diferente)")
print("✅ < (menor), > (maior)")
print("✅ <= (menor igual), >= (maior igual)")

print("\n🧠 LÓGICOS:")
print("✅ and (E lógico - ambos verdadeiros)")
print("✅ or (OU lógico - pelo menos um verdadeiro)")
print("✅ not (NÃO lógico - inverte)")

print("\n⚡ PRECEDÊNCIA (maior → menor):")
print("1. ** (potenciação)")
print("2. *, /, //, % (multiplicação e divisões)")
print("3. +, - (adição e subtração)")
print("4. <, >, <=, >=, ==, != (comparações)")
print("5. not (negação)")
print("6. and (E lógico)")
print("7. or (OU lógico)")

print("\n🚀 PRÓXIMOS PASSOS:")
print("- Pratiquem combinações complexas de operadores")
print("- Usem parênteses para deixar intenções claras")
print("- No Encontro 4: usaremos esses operadores em estruturas condicionais!")

print("\n=== FIM DO GABARITO ===")