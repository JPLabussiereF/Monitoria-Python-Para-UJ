# TAREFA DE CASA - ENCONTRO 3
# "Calculadora Científica com Validação"

"""
ENUNCIADO:
Crie uma calculadora científica completa que:

1. MENU DE OPERAÇÕES:
   - Mostre todas as opções: +, -, *, /, //, %, **
   - Peça dois números e a operação desejada

2. VALIDAÇÕES COM OPERADORES:
   - Números devem ser válidos (não vazios)
   - Não permitir divisão por zero (/ e //)
   - Operação deve estar no menu

3. CÁLCULOS COM TODOS OS OPERADORES:
   - Execute a operação escolhida
   - Mostre resultado formatado
   - Para divisão, mostre real E inteira

4. ANÁLISES COM OPERADORES LÓGICOS:
   - Determine se resultado é par/ímpar
   - Classifique como positivo/negativo/zero
   - Determine tamanho: pequeno (<100), médio (100-1000), grande (>1000)

5. TABELA-VERDADE BÔNUS:
   - Compare se ambos os números são positivos
   - Use AND, OR, NOT para análises extras

Tempo estimado: 15-20 minutos

EXEMPLO DE EXECUÇÃO:
=== CALCULADORA CIENTÍFICA ===
Operações disponíveis: +, -, *, /, //, %, **

Primeiro número: 15
Segundo número: 4
Operação: **

=== CÁLCULO ===
15 ** 4 = 50625

=== ANÁLISE DO RESULTADO ===
É par: False
É positivo: True
Classificação: grande (> 1000)

=== ANÁLISE DOS NÚMEROS ===
Ambos positivos: True and True = True
Pelo menos um positivo: True or True = True
Nenhum negativo: not False = True
"""

# ==========================================
# ESCREVA SEU CÓDIGO AQUI:
# ==========================================

print("=== CALCULADORA CIENTÍFICA COM VALIDAÇÃO ===")

# 1. Menu e coleta de dados


# 2. Validações usando operadores


# 3. Cálculos com operadores aritméticos


# 4. Análises com operadores de comparação e lógicos


# 5. Tabela-verdade bônus


# ==========================================
# GABARITO (não olhe antes de tentar!)
# ==========================================

"""
# GABARITO DA TAREFA DE CASA - ENCONTRO 3

print("=== CALCULADORA CIENTÍFICA COM VALIDAÇÃO ===")

# 1. Menu e coleta de dados
print("Operações disponíveis: +, -, *, /, //, %, **")
print()

try:
    num1 = float(input("Primeiro número: "))
    num2 = float(input("Segundo número: "))
    operacao = input("Operação: ").strip()
    
    # 2. Validações usando operadores
    operacoes_validas = ['+', '-', '*', '/', '//', '%', '**']
    operacao_valida = operacao in operacoes_validas
    divisao_por_zero = (operacao == '/' or operacao == '//' or operacao == '%') and num2 == 0
    
    print(f"\n=== VALIDAÇÕES ===")
    print(f"Operação válida: {operacao_valida}")
    print(f"Divisão por zero: {divisao_por_zero}")
    
    # Validação combinada com operadores lógicos
    pode_calcular = operacao_valida and not divisao_por_zero
    print(f"Pode calcular: {pode_calcular}")
    
    if pode_calcular:
        # 3. Cálculos com operadores aritméticos
        print(f"\n=== CÁLCULO ===")
        
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
        
        print(f"{num1} {operacao} {num2} = {resultado}")
        
        # Para operações de divisão, mostrar diferentes tipos
        if operacao == '/':
            print(f"Divisão inteira: {num1} // {num2} = {num1 // num2}")
            print(f"Resto: {num1} % {num2} = {num1 % num2}")
        
        # 4. Análises com operadores de comparação e lógicos
        print(f"\n=== ANÁLISE DO RESULTADO ===")
        
        # Convertendo para int se for número inteiro para análise de par/ímpar
        if resultado == int(resultado):
            resultado_int = int(resultado)
            eh_par = resultado_int % 2 == 0
            print(f"É par: {eh_par}")
        else:
            print("É par: N/A (número decimal)")
        
        # Análises com operadores de comparação
        eh_positivo = resultado > 0
        eh_negativo = resultado < 0
        eh_zero = resultado == 0
        
        print(f"É positivo: {eh_positivo}")
        print(f"É negativo: {eh_negativo}")
        print(f"É zero: {eh_zero}")
        
        # Classificação de tamanho usando operadores lógicos
        eh_pequeno = abs(resultado) < 100
        eh_medio = 100 <= abs(resultado) <= 1000
        eh_grande = abs(resultado) > 1000
        
        if eh_pequeno:
            classificacao = "pequeno (< 100)"
        elif eh_medio:
            classificacao = "médio (100-1000)"
        else:
            classificacao = "grande (> 1000)"
        
        print(f"Classificação: {classificacao}")
        
        # 5. Tabela-verdade e análises com operadores lógicos
        print(f"\n=== ANÁLISE DOS NÚMEROS ===")
        
        num1_positivo = num1 > 0
        num2_positivo = num2 > 0
        num1_negativo = num1 < 0
        num2_negativo = num2 < 0
        
        print(f"Primeiro número positivo: {num1_positivo}")
        print(f"Segundo número positivo: {num2_positivo}")
        
        # Operações lógicas
        ambos_positivos = num1_positivo and num2_positivo
        pelo_menos_um_positivo = num1_positivo or num2_positivo
        nenhum_negativo = not (num1_negativo or num2_negativo)
        ambos_diferentes_de_zero = num1 != 0 and num2 != 0
        
        print(f"\n=== TABELA-VERDADE ===")
        print(f"Ambos positivos: {num1_positivo} and {num2_positivo} = {ambos_positivos}")
        print(f"Pelo menos um positivo: {num1_positivo} or {num2_positivo} = {pelo_menos_um_positivo}")
        print(f"Nenhum negativo: not ({num1_negativo} or {num2_negativo}) = {nenhum_negativo}")
        print(f"Ambos ≠ 0: {num1 != 0} and {num2 != 0} = {ambos_diferentes_de_zero}")
        
        # Análise final combinada
        print(f"\n=== ANÁLISE COMBINADA ===")
        calculo_seguro = ambos_diferentes_de_zero and operacao_valida
        resultado_interessante = abs(resultado) > 10 and resultado != int(resultado)
        
        print(f"Cálculo seguro: {calculo_seguro}")
        print(f"Resultado interessante: {resultado_interessante}")
        
    else:
        # Mensagens de erro usando operadores
        print(f"\n❌ ERRO NO CÁLCULO:")
        if not operacao_valida:
            print(f"- Operação '{operacao}' inválida. Use: {', '.join(operacoes_validas)}")
        if divisao_por_zero:
            print("- Não é possível dividir por zero!")

except ValueError:
    print("❌ ERRO: Digite apenas números válidos!")

print(f"\n🎉 CALCULADORA CONCLUÍDA!")
print("Você dominou todos os operadores:")
print("✅ Aritméticos: +, -, *, /, //, %, **")  
print("✅ Comparação: ==, !=, <, >, <=, >=")
print("✅ Lógicos: and, or, not")

# OBSERVAÇÕES DO GABARITO:
# 1. Usamos try/except para validar entrada de números
# 2. Operadores lógicos combinam múltiplas condições
# 3. abs() pega valor absoluto para classificação
# 4. Convertemos float para int quando necessário
# 5. Operadores in verifica se valor está em lista
# 6. strip() remove espaços extras da operação
# 7. Combinamos todos os tipos de operadores
# 8. Validações robustas usando operadores lógicos

# VARIAÇÕES POSSÍVEIS:
# - Adicionar mais operações (raiz quadrada, log)
# - Histórico de cálculos  
# - Interface mais bonita com loops
# - Validação mais rigorosa de entrada
# - Operações com mais de 2 números
"""

print("\n💡 DICAS PARA DESENVOLVER:")
print("- Teste todos os operadores aritméticos")
print("- Valide divisão por zero usando comparação")
print("- Use operadores lógicos para combinar condições")
print("- Construa pelo menos uma tabela-verdade")
print("- Organize a saída de forma legível")

print("\n🚀 DESAFIOS EXTRAS:")
print("1. Adicione validação para operações inválidas")
print("2. Mostre resultado em notação científica se muito grande")
print("3. Calcule raiz quadrada usando ** 0.5")
print("4. Crie menu interativo com while (próximo encontro!)")
print("5. Adicione histórico dos últimos 3 cálculos")

print("\n⚡ CRITÉRIOS DE AVALIAÇÃO:")
print("✅ Usa todos os 7 operadores aritméticos")
print("✅ Aplica operadores de comparação para validações") 
print("✅ Combina condições com operadores lógicos")
print("✅ Constrói pelo menos uma análise boolean")
print("✅ Trata caso de divisão por zero")
print("✅ Organiza saída de forma profissional")