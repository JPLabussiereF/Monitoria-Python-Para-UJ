# GABARITO - ENCONTRO 2: Sintaxe, tipos e variáveis
# Monitoria de Python - Engenharia da Computação

"""
GABARITO COMPLETO
Soluções comentadas com foco em tipos e conversões
"""

print("=== GABARITO - ENCONTRO 2 ===")
print()

# ======================================
# EXERCÍCIO 1 - CONVERSOR DE IDADE
# ======================================
print("1. CONVERSOR DE IDADE")
print("=" * 30)

# Solução:
ano_atual_str = input("Digite o ano atual: ")
ano_nasc_str = input("Digite seu ano de nascimento: ")

# Convertendo strings para inteiros
ano_atual = int(ano_atual_str)
ano_nascimento = int(ano_nasc_str)

# Calculando idade
idade = ano_atual - ano_nascimento

print("Sua idade é:", idade, "anos")

print("\n💡 EXPLICAÇÃO:")
print("- input() sempre retorna string")
print("- int() converte string para número inteiro")
print("- Agora podemos fazer subtração matemática")
print("- Se não convertesse, faria concatenação: '2025' + '2003' = '20252003'")
print()

print("-" * 50)

# ======================================
# EXERCÍCIO 2 - CALCULADORA SIMPLES  
# ======================================
print("2. CALCULADORA SIMPLES")
print("=" * 30)

# Solução:
print("=== COLETANDO NÚMEROS ===")
num1_str = input("Digite o primeiro número: ")
num2_str = input("Digite o segundo número: ")

print("\nTipos ANTES da conversão:")
print("Número 1:", num1_str, "- Tipo:", type(num1_str))
print("Número 2:", num2_str, "- Tipo:", type(num2_str))

# Convertendo para float (aceita decimais)
num1 = float(num1_str)
num2 = float(num2_str)

print("\nTipos DEPOIS da conversão:")
print("Número 1:", num1, "- Tipo:", type(num1))
print("Número 2:", num2, "- Tipo:", type(num2))

# Calculando soma
soma = num1 + num2
print("\nSoma:", soma)

print("\n💡 EXPLICAÇÃO:")
print("- Usamos float() para aceitar números decimais")
print("- int() só funcionaria com números inteiros")
print("- Agora + faz soma matemática, não concatenação")
print()

print("-" * 50)

# ======================================
# EXERCÍCIO 3 - FORMATADOR DE DADOS
# ======================================
print("3. FORMATADOR DE DADOS")
print("=" * 30)

# Solução:
print("=== COLETANDO INFORMAÇÕES ===")
nome = input("Nome: ")
idade_str = input("Idade: ")
altura_str = input("Altura (ex: 1.75): ")
estudante_str = input("É estudante? (sim/não): ")

# Conversões apropriadas
idade = int(idade_str)           # Idade é número inteiro
altura = float(altura_str)       # Altura aceita decimais
estudante = estudante_str.lower() == "sim"  # Converte para boolean

print("\n=== DADOS FORMATADOS ===")
print("Nome:", nome, "- Tipo:", type(nome))
print("Idade:", idade, "anos - Tipo:", type(idade))
print("Altura:", altura, "m - Tipo:", type(altura))
print("É estudante:", estudante, "- Tipo:", type(estudante))

print("\n💡 EXPLICAÇÃO:")
print("- nome: permanece string (texto)")
print("- idade: int (números inteiros para idade)")
print("- altura: float (aceita 1.75, 1.8, etc)")
print("- estudante: boolean criado comparando com 'sim'")
print("- .lower() deixa tudo minúsculo para comparar")
print()

print("-" * 50)

# ======================================
# EXERCÍCIO 4 - CONVERSOR DE TEMPERATURA
# ======================================
print("4. CONVERSOR DE TEMPERATURA")
print("=" * 30)

# Solução:
celsius_str = input("Temperatura em Celsius: ")
celsius = float(celsius_str)

# Aplicando fórmula: F = C × 9/5 + 32
fahrenheit = celsius * 9/5 + 32

print(f"Conversão: {celsius}°C = {fahrenheit}°F")

# Alternativa sem f-string:
print("Conversão:", celsius, "°C =", fahrenheit, "°F")

print("\n💡 EXPLICAÇÃO:")
print("- Usamos float() para aceitar decimais (25.5°C)")
print("- Fórmula matemática: multiplicação e soma")
print("- f-string facilita formatação (veremos mais no futuro)")
print("- Resultado em float preserva precisão")
print()

print("-" * 50)

# ======================================
# EXERCÍCIO 5 - ANALISADOR DE TEXTO vs NÚMERO
# ======================================
print("5. ANALISADOR DE TEXTO vs NÚMERO")
print("=" * 30)

# Solução:
valor_str = input("Digite um valor qualquer: ")

print("\n=== ANÁLISE DO VALOR ===")
print("Como string:", valor_str, "- Tipo:", type(valor_str))

# Tentando converter para int
print("\n--- Tentando converter para int ---")
if valor_str.isdigit() or (valor_str.startswith('-') and valor_str[1:].isdigit()):
    valor_int = int(valor_str)
    print("Como int:", valor_int, "- Tipo:", type(valor_int))
    print("✅ Conversão para int: SUCESSO")
else:
    print("❌ Conversão para int: IMPOSSÍVEL (não é número inteiro)")

# Tentando converter para float  
print("\n--- Tentando converter para float ---")
try:
    valor_float = float(valor_str)
    print("Como float:", valor_float, "- Tipo:", type(valor_float))
    print("✅ Conversão para float: SUCESSO")
except ValueError:
    print("❌ Conversão para float: IMPOSSÍVEL (não é número)")

# Boolean
valor_bool = bool(valor_str)
print("\n--- Convertendo para bool ---")
print("Como bool:", valor_bool, "- Tipo:", type(valor_bool))
print("(Lembre: só strings vazias '' são False)")

print("\n💡 EXPLICAÇÃO:")
print("- isdigit() verifica se contém só números")
print("- try/except captura erros de conversão")
print("- float() é mais flexível que int()")
print("- bool() só é False para valores 'vazios'")
print()

print("-" * 50)

# ======================================
# EXERCÍCIO 6 - CALCULADORA DE MÉDIA
# ======================================
print("6. CALCULADORA DE MÉDIA")
print("=" * 30)

# Solução:
print("=== CALCULADORA DE NOTAS ===")
nota1_str = input("Primeira nota: ")
nota2_str = input("Segunda nota: ")
nota3_str = input("Terceira nota: ")

# Convertendo todas para float
nota1 = float(nota1_str)
nota2 = float(nota2_str)
nota3 = float(nota3_str)

# Calculando média
media = (nota1 + nota2 + nota3) / 3

# Determinando aprovação (boolean)
aprovado = media >= 7.0

# Exibindo resultados formatados
print("\n=== RESULTADO ===")
print("Notas:", nota1, ",", nota2, ",", nota3)
print("Média:", round(media, 2))  # Arredondando para 2 casas
print("Aprovado:", aprovado, "- Tipo:", type(aprovado))

# Mensagem condicional simples
if aprovado:
    print("🎉 Parabéns! Você foi aprovado!")
else:
    print("📚 Continue estudando para a próxima!")

print("\n💡 EXPLICAÇÃO:")
print("- float() para aceitar notas decimais (7.5, 8.2, etc)")
print("- Comparação (>=) retorna boolean automaticamente")
print("- round(media, 2) arredonda para 2 casas decimais")
print("- Boolean pode ser usado em condições (if)")
print()

print("-" * 50)

# ======================================
# EXERCÍCIO 7 - CONSTRUTOR DE FRASE
# ======================================
print("7. CONSTRUTOR DE FRASE")
print("=" * 30)

# Solução:
print("=== COLETANDO INFORMAÇÕES ===")
nome = input("Nome: ")
idade_str = input("Idade: ")
cidade = input("Cidade: ")
salario_str = input("Salário desejado: ")

# Conversões apropriadas
idade = int(idade_str)
salario = float(salario_str)

print("\n=== CONSTRUINDO FRASES ===")

# Método 1: Concatenação com +
frase1 = "Olá, meu nome é " + nome + ", tenho " + str(idade) + " anos, moro em " + cidade + " e quero ganhar R$ " + str(salario) + "."
print("Com concatenação (+):")
print(frase1)

# Método 2: Vírgulas no print
print("\nCom vírgulas:")
print("Olá, meu nome é", nome, ", tenho", idade, "anos, moro em", cidade, "e quero ganhar R$", salario, ".")

# Método 3: f-string (bônus)
print("\nCom f-string (avançado):")
print(f"Olá, meu nome é {nome}, tenho {idade} anos, moro em {cidade} e quero ganhar R$ {salario}.")

print("\n=== COMPARAÇÃO DOS MÉTODOS ===")
print("Concatenação (+): Precisa converter tudo para string")
print("Vírgulas: Python faz conversão automática")  
print("F-string: Mais limpo e moderno")

print("\n💡 EXPLICAÇÃO:")
print("- Concatenação (+) só funciona entre strings")
print("- str() converte números para texto")
print("- Vírgulas no print() são mais práticas")
print("- f-strings são o futuro do Python!")
print()

print("-" * 50)

# ======================================
# DESAFIO EXTRA 🚀
# ======================================
print("DESAFIO EXTRA 🚀")
print("=" * 30)

# Solução completa:
print("=== CARTÃO DE DADOS PROFISSIONAL ===")

# Coletando informações variadas
nome = input("Nome completo: ")
idade_str = input("Idade: ")
altura_str = input("Altura (m): ")
peso_str = input("Peso (kg): ")
ativo_str = input("Está ativo no mercado? (sim/não): ")

# Conversões para tipos apropriados
idade = int(idade_str)              # int: número inteiro
altura = float(altura_str)          # float: aceita decimais
peso = float(peso_str)             # float: aceita decimais  
ativo = ativo_str.lower() == "sim" # bool: verdadeiro/falso

# Cálculo bônus: IMC
imc = peso / (altura * altura)

# Exibindo cartão profissional
print("\n" + "=" * 50)
print("           CARTÃO DE DADOS")
print("=" * 50)
print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
print(f"Altura: {altura} m")
print(f"Peso: {peso} kg")
print(f"IMC: {round(imc, 1)}")
print(f"Ativo no mercado: {ativo}")
print("=" * 50)

print("\n=== ANÁLISE DOS TIPOS ===")
# O .__name__ é um atributo especial que retorna o nome do tipo/classe como string:
# print(type(nome))           # → <class 'str'>
# print(type(nome).__name__)  # → str
print("Nome:", nome, "→", type(nome).__name__)
print("Idade:", idade, "→", type(idade).__name__)
print("Altura:", altura, "→", type(altura).__name__)
print("Peso:", peso, "→", type(peso).__name__)
print("Ativo:", ativo, "→", type(ativo).__name__)

# A função round() é usada para arredondar números → round(numero, casas_decimais)
print("IMC:", round(imc, 1), "→", type(imc).__name__)

print("\n🎯 RESUMO DOS TIPOS USADOS:")
print("✅ str: Nome (texto)")
print("✅ int: Idade (número inteiro)")  
print("✅ float: Altura, peso, IMC (decimais)")
print("✅ bool: Status ativo (True/False)")

print("\n💡 EXPLICAÇÃO AVANÇADA:")
print("- type().__name__ mostra só o nome do tipo")
print("- Usamos todos os 4 tipos básicos do Python")
print("- Cálculos matemáticos só funcionam após conversão")
print("- Formatação profissional melhora apresentação")
print("- round() controla casas decimais do resultado")
print()

print("=" * 60)

# ======================================
# DICAS FINAIS DO GABARITO
# ======================================
print("\n🎯 DICAS IMPORTANTES PARA DOMINAR TIPOS:")
print("\n1. CONVERSÕES BÁSICAS:")
print("   int('123') → 123")
print("   float('12.5') → 12.5") 
print("   str(123) → '123'")
print("   bool('texto') → True")

print("\n2. PEGADINHAS:")
print("   int(12.9) → 12 (corta, não arredonda!)")
print("   bool('0') → True (string não vazia)")
print("   bool('') → False (string vazia)")
print("   float('12,5') → ERRO (use ponto: '12.5')")

print("\n3. BOAS PRÁTICAS:")
print("   - Use int() para idades, anos, contadores")
print("   - Use float() para medidas, preços, cálculos")
print("   - Use str() quando precisar de texto")
print("   - Use bool() para flags verdadeiro/falso")

print("\n4. FORMATAÇÃO:")
print("   - round(numero, 2) para 2 casas decimais")
print("   - Vírgulas no print() são mais fáceis que +")
print("   - f-strings são o futuro: f'Olá {nome}!'")

print("\n🚀 PRÓXIMOS PASSOS:")
print("- Pratiquem conversões até virar automático")
print("- Testem valores que quebram (letras em int())")
print("- No Encontro 3: usaremos esses tipos com operadores!")

print("\n=== FIM DO GABARITO ===")