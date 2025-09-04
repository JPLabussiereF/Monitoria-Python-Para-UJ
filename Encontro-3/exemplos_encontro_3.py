# EXEMPLOS DE CÓDIGO - ENCONTRO 3
# Operadores aritméticos, comparação e lógicos

"""
Exemplos prontos para demonstração em aula
Cada exemplo pode ser executado independentemente
"""

print("=== EXEMPLOS DE CÓDIGO - ENCONTRO 3 ===")
print()

# ==========================================
# EXEMPLO 1: OPERADORES ARITMÉTICOS BÁSICOS
# ==========================================
print("EXEMPLO 1: Operadores Aritméticos")
print("=" * 40)

a, b = 15, 4
print(f"Números: a = {a}, b = {b}")
print()

print("=== TODOS OS OPERADORES ARITMÉTICOS ===")
print(f"{a} + {b} = {a + b}")      # 19
print(f"{a} - {b} = {a - b}")      # 11  
print(f"{a} * {b} = {a * b}")      # 60
print(f"{a} / {b} = {a / b}")      # 3.75 (divisão real)
print(f"{a} // {b} = {a // b}")    # 3 (divisão inteira)
print(f"{a} % {b} = {a % b}")      # 3 (resto)
print(f"{a} ** {b} = {a ** b}")    # 50625 (potência)

print(f"\n💡 Observe que:")
print(f"- / sempre resulta em float: {type(a / b)}")
print(f"- // descarta decimais: {a / b} → {a // b}")
print(f"- % útil para detectar múltiplos: 15 é múltiplo de 4? {a % b == 0}")

print("\n" + "-" * 60)

# ==========================================
# EXEMPLO 2: OPERADORES DE COMPARAÇÃO  
# ==========================================
print("\nEXEMPLO 2: Operadores de Comparação")
print("=" * 40)

idade1, idade2 = 25, 18
print(f"Idades: {idade1} e {idade2}")
print()

print("=== COMPARAÇÕES BÁSICAS ===")
print(f"{idade1} == {idade2} : {idade1 == idade2}")  # False
print(f"{idade1} != {idade2} : {idade1 != idade2}")  # True
print(f"{idade1} > {idade2}  : {idade1 > idade2}")   # True
print(f"{idade1} < {idade2}  : {idade1 < idade2}")   # False
print(f"{idade1} >= 18 : {idade1 >= 18}")            # True
print(f"{idade2} <= 25 : {idade2 <= 25}")            # True

# Comparações encadeadas (Python permite!)
print(f"\n=== COMPARAÇÕES ENCADEADAS ===")
print(f"18 <= {idade1} <= 65 : {18 <= idade1 <= 65}")
print(f"0 <= {idade2} < 18 : {0 <= idade2 < 18}")

print(f"\n💡 Resultado das comparações:")
print(f"- Sempre boolean: {type(idade1 > idade2)}")
print(f"- Útil para validações e condições")

print("\n" + "-" * 60)

# ==========================================
# EXEMPLO 3: OPERADORES LÓGICOS FUNDAMENTAIS
# ==========================================
print("\nEXEMPLO 3: Operadores Lógicos")
print("=" * 35)

tem_idade = True
tem_documento = False
tem_experiencia = True

print(f"Dados: idade={tem_idade}, documento={tem_documento}, experiência={tem_experiencia}")
print()

print("=== OPERADORES LÓGICOS ===")
print(f"tem_idade and tem_documento : {tem_idade and tem_documento}")
print(f"tem_idade or tem_documento  : {tem_idade or tem_documento}")
print(f"not tem_documento           : {not tem_documento}")

# Combinações mais complexas
print(f"\n=== COMBINAÇÕES COMPLEXAS ===")
pode_trabalhar = tem_idade and (tem_documento or tem_experiencia)
situacao_ideal = tem_idade and tem_documento and tem_experiencia
precisa_melhorar = not (tem_documento and tem_experiencia)

print(f"Pode trabalhar: {pode_trabalhar}")
print(f"Situação ideal: {situacao_ideal}")
print(f"Precisa melhorar: {precisa_melhorar}")

print(f"\n💡 Precedência: not > and > or")
print(f"Use parênteses para clareza!")

print("\n" + "-" * 60)

# ==========================================
# EXEMPLO 4: TABELA-VERDADE INTERATIVA
# ==========================================
print("\nEXEMPLO 4: Tabela-Verdade Completa")
print("=" * 40)

# Testando todas as combinações
valores = [(True, True), (True, False), (False, True), (False, False)]

print("A     | B     | A and B | A or B | not A | not B")
print("------|-------|---------|--------|-------|-------")

for a, b in valores:
    print(f"{str(a):5} | {str(b):5} | {str(a and b):7} | {str(a or b):6} | {str(not a):5} | {str(not b):5}")

print(f"\n💡 Padrões importantes:")
print(f"- AND só é True quando AMBOS são True")
print(f"- OR só é False quando AMBOS são False")  
print(f"- NOT sempre inverte o valor")

print("\n" + "-" * 60)

# ==========================================
# EXEMPLO 5: PRECEDÊNCIA DE OPERADORES
# ==========================================
print("\nEXEMPLO 5: Precedência de Operadores")
print("=" * 40)

print("=== TESTANDO PRECEDÊNCIA ===")
resultado1 = 2 + 3 * 4
resultado2 = (2 + 3) * 4
resultado3 = 2 ** 3 ** 2  # Associativo à direita!
resultado4 = (2 ** 3) ** 2

print(f"2 + 3 * 4 = {resultado1} (multiplicação primeiro)")
print(f"(2 + 3) * 4 = {resultado2} (parênteses alteram)")
print(f"2 ** 3 ** 2 = {resultado3} (potência: direita→esquerda)")
print(f"(2 ** 3) ** 2 = {resultado4} (forçando ordem)")

# Exemplo com lógicos
print(f"\n=== PRECEDÊNCIA COM LÓGICOS ===")
x, y, z = True, False, True
resultado5 = not x and y or z
resultado6 = not (x and y) or z
resultado7 = not x and (y or z)

print(f"not True and False or True = {resultado5}")
print(f"not (True and False) or True = {resultado6}")
print(f"not True and (False or True) = {resultado7}")

print(f"\n💡 Ordem: ** → *, /, %, // → +, - → comparação → not → and → or")

print("\n" + "-" * 60)

# ==========================================
# EXEMPLO 6: VALIDAÇÃO PRÁTICA COM OPERADORES
# ==========================================
print("\nEXEMPLO 6: Sistema de Validação")
print("=" * 35)

# Simulando dados de entrada
nome = "João"
idade = 22
salario = 3500.0
tem_diploma = True
anos_experiencia = 3

print(f"Candidato: {nome}, {idade} anos, R${salario}, diploma: {tem_diploma}, {anos_experiencia} anos exp.")
print()

# Validações usando operadores
nome_ok = len(nome) >= 2 and len(nome) <= 50
idade_ok = 18 <= idade <= 65
salario_ok = salario > 0
experiencia_ok = anos_experiencia >= 0

# Critérios usando lógicos
idade_ideal = 25 <= idade <= 45
salario_compativel = 2000 <= salario <= 10000
perfil_junior = not tem_diploma and anos_experiencia <= 2
perfil_senior = tem_diploma and anos_experiencia >= 5
perfil_pleno = not perfil_junior and not perfil_senior

print("=== VALIDAÇÕES BÁSICAS ===")
print(f"Nome válido: {nome_ok}")
print(f"Idade válida: {idade_ok}")
print(f"Salário válido: {salario_ok}")
print(f"Experiência válida: {experiencia_ok}")

dados_validos = nome_ok and idade_ok and salario_ok and experiencia_ok
print(f"Todos os dados OK: {dados_validos}")

print(f"\n=== ANÁLISE DE PERFIL ===")
print(f"Idade ideal (25-45): {idade_ideal}")
print(f"Salário compatível: {salario_compativel}")
print(f"Perfil junior: {perfil_junior}")
print(f"Perfil pleno: {perfil_pleno}")
print(f"Perfil senior: {perfil_senior}")

# Decisão final
aprovado = dados_validos and (perfil_junior or perfil_pleno or perfil_senior)
print(f"\nDECISÃO FINAL: {'✅ APROVADO' if aprovado else '❌ REJEITADO'}")

print("\n" + "-" * 60)

# ==========================================
# EXEMPLO 7: NÚMEROS - ANÁLISE COMPLETA
# ==========================================
print("\nEXEMPLO 7: Analisador de Números")
print("=" * 35)

numero = 42

print(f"Analisando o número: {numero}")
print()

# Análises básicas
eh_positivo = numero > 0
eh_negativo = numero < 0
eh_zero = numero == 0
eh_par = numero % 2 == 0
eh_impar = not eh_par

print("=== ANÁLISES BÁSICAS ===")
print(f"Positivo: {eh_positivo}")
print(f"Negativo: {eh_negativo}")  
print(f"Zero: {eh_zero}")
print(f"Par: {eh_par}")
print(f"Ímpar: {eh_impar}")

# Múltiplos
multiplo_2 = numero % 2 == 0
multiplo_3 = numero % 3 == 0
multiplo_5 = numero % 5 == 0
multiplo_10 = numero % 10 == 0

print(f"\n=== MÚLTIPLOS ===")
print(f"Múltiplo de 2: {multiplo_2}")
print(f"Múltiplo de 3: {multiplo_3}")
print(f"Múltiplo de 5: {multiplo_5}")
print(f"Múltiplo de 10: {multiplo_10}")

# Combinações lógicas
fizz = multiplo_3 and not multiplo_5
buzz = multiplo_5 and not multiplo_3  
fizzbuzz = multiplo_3 and multiplo_5
especial = fizz or buzz or fizzbuzz

print(f"\n=== CLASSIFICAÇÃO ESPECIAL ===")
print(f"Fizz (múltiplo só de 3): {fizz}")
print(f"Buzz (múltiplo só de 5): {buzz}")
print(f"FizzBuzz (múltiplo de 3 e 5): {fizzbuzz}")
print(f"Número especial: {especial}")

# Faixas
pequeno = numero < 100
medio = 100 <= numero < 1000
grande = numero >= 1000

print(f"\n=== CLASSIFICAÇÃO POR TAMANHO ===")
print(f"Pequeno (<100): {pequeno}")
print(f"Médio (100-999): {medio}")
print(f"Grande (>=1000): {grande}")

print("\n" + "-" * 60)

# ==========================================
# EXEMPLO 8: CALCULADORA COM VALIDAÇÃO
# ==========================================
print("\nEXEMPLO 8: Calculadora com Validação")
print("=" * 45)

# Simulando entradas
num1, num2 = 12, 5
operacao = "*"

print(f"Operação: {num1} {operacao} {num2}")
print()

# Validações
operacoes_validas = ['+', '-', '*', '/', '//', '%', '**']
operacao_ok = operacao in operacoes_validas
divisao_por_zero = (operacao in ['/', '//', '%']) and num2 == 0

print("=== VALIDAÇÕES ===")
print(f"Operação válida: {operacao_ok}")
print(f"Divisão por zero: {divisao_por_zero}")

pode_calcular = operacao_ok and not divisao_por_zero
print(f"Pode calcular: {pode_calcular}")

if pode_calcular:
    # Executando operação
    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2  
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        resultado = num1 / num2
    elif operacao == '//':
        resultado = num1 // num2
    elif operacao == '%':
        resultado = num1 % num2
    elif operacao == '**':
        resultado = num1 ** num2
    
    print(f"\n=== RESULTADO ===")
    print(f"{num1} {operacao} {num2} = {resultado}")
    
    # Análise do resultado
    if isinstance(resultado, int):
        eh_par = resultado % 2 == 0
        print(f"Resultado é par: {eh_par}")
    
    resultado_positivo = resultado > 0
    resultado_inteiro = resultado == int(resultado)
    
    print(f"Resultado positivo: {resultado_positivo}")
    print(f"Resultado inteiro: {resultado_inteiro}")
    
else:
    print("\n❌ Não foi possível calcular!")

print("\n" + "=" * 60)
print("🎯 TODOS OS EXEMPLOS EXECUTADOS!")
print("Conceitos demonstrados:")
print("✅ Operadores aritméticos: +, -, *, /, //, %, **")
print("✅ Operadores de comparação: ==, !=, <, >, <=, >=")
print("✅ Operadores lógicos: and, or, not") 
print("✅ Precedência e parênteses")
print("✅ Tabelas-verdade")
print("✅ Validações práticas")
print("✅ Análises numéricas")
print("=" * 60)