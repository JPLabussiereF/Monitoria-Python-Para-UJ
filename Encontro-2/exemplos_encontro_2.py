# EXEMPLOS DE CÓDIGO - ENCONTRO 2
# Sintaxe, tipos e variáveis

"""
Exemplos prontos para demonstração em aula
Cada exemplo é independente e pode ser executado separadamente
"""

print("=== EXEMPLOS DE CÓDIGO - ENCONTRO 2 ===")
print()

# ==========================================
# EXEMPLO 1: DESCOBRINDO E CONVERTENDO TIPOS
# ==========================================
print("EXEMPLO 1: Descobrindo e Convertendo Tipos")
print("=" * 45)

# Simulando entrada de dados
print("# Coletando dados como string")
idade_texto = "25"  # Simulando input("Sua idade: ")
altura_texto = "1.75"  # Simulando input("Sua altura: ")

print(f"idade_texto = '{idade_texto}'")
print(f"altura_texto = '{altura_texto}'")

# Mostrando tipos originais
print("\n# Tipos ANTES da conversão:")
print("Idade como texto:", idade_texto, "- Tipo:", type(idade_texto))
print("Altura como texto:", altura_texto, "- Tipo:", type(altura_texto))

# Convertendo para números
idade = int(idade_texto)
altura = float(altura_texto)

print("\n# Tipos DEPOIS da conversão:")
print("Idade:", idade, "- Tipo:", type(idade))
print("Altura:", altura, "- Tipo:", type(altura))

# Fazendo cálculos (agora é possível!)
print("\n# Agora podemos fazer cálculos:")
print("Daqui a 10 anos você terá:", idade + 10, "anos")
print("Sua altura em cm:", altura * 100)

print("\n" + "-" * 60)

# ==========================================
# EXEMPLO 2: TRABALHANDO COM BOOLEANS
# ==========================================
print("\nEXEMPLO 2: Trabalhando com Booleans")
print("=" * 40)

# Diferentes formas de criar booleans
print("# Valores boolean diretos:")
maior_idade = True
tem_carteira = False
print("maior_idade =", maior_idade, "- Tipo:", type(maior_idade))
print("tem_carteira =", tem_carteira, "- Tipo:", type(tem_carteira))

# Conversões interessantes
print("\n# Conversões com bool():")
print("bool('Python') =", bool("Python"))     # True (string não vazia)
print("bool('') =", bool(""))                 # False (string vazia)
print("bool(42) =", bool(42))                 # True (número diferente de zero)
print("bool(0) =", bool(0))                   # False (zero é falso)
print("bool(-5) =", bool(-5))                 # True (qualquer número ≠ 0)

# Criando boolean com comparação
print("\n# Boolean criado com comparação:")
idade = 20
eh_adulto = idade >= 18
print(f"idade = {idade}")
print(f"eh_adulto = idade >= 18 = {eh_adulto}")

print("\n" + "-" * 60)

# ==========================================
# EXEMPLO 3: CONCATENAÇÃO vs VÍRGULAS
# ==========================================
print("\nEXEMPLO 3: Concatenação vs Vírgulas")
print("=" * 40)

nome = "Ana"
idade = 20

print("# Dados:")
print(f"nome = '{nome}' - Tipo: {type(nome)}")
print(f"idade = {idade} - Tipo: {type(idade)}")

print("\n# ❌ ERRO comum: misturar tipos na concatenação")
print("# print('Olá ' + nome + ', você tem ' + idade + ' anos')  # TypeError!")

print("\n# ✅ SOLUÇÕES que funcionam:")

print("\n## Método 1: Conversão manual")
resultado1 = "Olá " + nome + ", você tem " + str(idade) + " anos"
print("Resultado:", resultado1)

print("\n## Método 2: Vírgulas (mais fácil)")
print("Resultado:", "Olá", nome, ", você tem", idade, "anos")

print("\n## Método 3: f-strings (mais avançado)")
resultado3 = f"Olá {nome}, você tem {idade} anos"
print("Resultado:", resultado3)

print("\n💡 Dica: Vírgulas no print() são mais práticas!")

print("\n" + "-" * 60)

# ==========================================
# EXEMPLO 4: CALCULADORA DE IMC COMPLETA
# ==========================================
print("\nEXEMPLO 4: Calculadora de IMC Completa")
print("=" * 45)

print("# Simulando entrada de dados:")
nome = "João"
peso_str = "75.5"
altura_str = "1.80"

print(f"nome = '{nome}'")
print(f"peso_str = '{peso_str}'")
print(f"altura_str = '{altura_str}'")

print("\n# Convertendo para tipos apropriados:")
peso = float(peso_str)      # Aceita decimais
altura = float(altura_str)  # Aceita decimais

print(f"peso = {peso} - Tipo: {type(peso)}")
print(f"altura = {altura} - Tipo: {type(altura)}")

print("\n# Calculando IMC:")
imc = peso / (altura * altura)
print(f"imc = peso / (altura * altura) = {imc}")

print("\n# Formatando resultado:")
print(f"IMC bruto: {imc}")
print(f"IMC com 2 casas: {round(imc, 2)}")

print("\n# Resultado final formatado:")
print(f"{nome}, seu IMC é: {round(imc, 2)}")

# Classificação simples
print("\n# Bônus: Classificação (usando boolean)")
peso_normal = 18.5 <= imc < 25
print(f"Peso normal (18.5 ≤ IMC < 25): {peso_normal}")

print("\n" + "-" * 60)

# ==========================================
# EXEMPLO 5: TRATANDO ERROS DE CONVERSÃO
# ==========================================
print("\nEXEMPLO 5: Tratando Erros de Conversão")
print("=" * 45)

print("# Testando conversões que podem falhar:")

# Valores para testar
valores_teste = ["123", "45.67", "abc", "", "12.5.3", "-10"]

for valor in valores_teste:
    print(f"\nTestando: '{valor}'")
    
    # Teste int()
    try:
        resultado_int = int(valor)
        print(f"  int('{valor}') = {resultado_int} ✅")
    except ValueError:
        print(f"  int('{valor}') = ERRO ❌")
    
    # Teste float()  
    try:
        resultado_float = float(valor)
        print(f"  float('{valor}') = {resultado_float} ✅")
    except ValueError:
        print(f"  float('{valor}') = ERRO ❌")
    
    # Boolean sempre funciona
    resultado_bool = bool(valor)
    print(f"  bool('{valor}') = {resultado_bool}")

print("\n💡 Dica: use try/except para capturar erros!")

print("\n" + "-" * 60)

# ==========================================
# EXEMPLO 6: COMPARAÇÃO COMPLETA DE MÉTODOS
# ==========================================
print("\nEXEMPLO 6: Comparação de Métodos de Formatação")
print("=" * 55)

# Dados de exemplo
produto = "Notebook"
preco = 2499.99
desconto = 15
disponivel = True

print("# Dados:")
print(f"produto = '{produto}'")
print(f"preco = {preco}")
print(f"desconto = {desconto}")
print(f"disponivel = {disponivel}")

print("\n# Diferentes formas de exibir:")

print("\n## 1. Concatenação com str():")
msg1 = "Produto: " + produto + " - Preço: R$ " + str(preco) + " - Desconto: " + str(desconto) + "%"
print(msg1)

print("\n## 2. Vírgulas no print():")
print("Produto:", produto, "- Preço: R$", preco, "- Desconto:", desconto, "%")

print("\n## 3. f-strings (moderno):")
msg3 = f"Produto: {produto} - Preço: R$ {preco} - Desconto: {desconto}%"
print(msg3)

print("\n## 4. Formatação com round():")
print(f"Preço formatado: R$ {round(preco, 2)}")
print(f"Preço final: R$ {round(preco * (100-desconto)/100, 2)}")

print("\n💡 Comparação:")
print("- Concatenação: Mais trabalhosa, precisa de str()")
print("- Vírgulas: Fácil, conversão automática")
print("- f-strings: Mais limpo e poderoso")

print("\n" + "=" * 60)
print("🎯 TODOS OS EXEMPLOS EXECUTADOS COM SUCESSO!")
print("Pratique modificando os valores e testando!")
print("=" * 60)