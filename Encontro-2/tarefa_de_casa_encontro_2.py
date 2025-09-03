# TAREFA DE CASA - ENCONTRO 2
# "Conversor Universal de Medidas"

"""
ENUNCIADO:
Crie um programa que:
1. Colete: nome, peso (kg), altura (m), idade (anos)
2. Faça conversões: peso→gramas, altura→cm, calcule IMC
3. Exiba relatório organizado usando concatenação E vírgulas
4. Determine se é maior de idade (18+) como boolean
5. Mostre pelo menos 3 tipos diferentes no final

Tempo estimado: 15-20 minutos

EXEMPLO DE SAÍDA ESPERADA:
=== RELATÓRIO DE MEDIDAS ===
Nome: João Silva
Peso: 70.5 kg (70500.0 gramas)
Altura: 1.75 m (175.0 cm)
Idade: 22 anos
IMC: 23.02
É maior de idade: True

=== TIPOS DOS DADOS ===
Nome: <class 'str'>
Peso: <class 'float'>
Idade: <class 'int'>
Maior de idade: <class 'bool'>
"""

# ==========================================
# ESCREVA SEU CÓDIGO AQUI:
# ==========================================

print("=== CONVERSOR UNIVERSAL DE MEDIDAS ===")

# 1. Coletando informações


# 2. Fazendo conversões apropriadas


# 3. Realizando cálculos


# 4. Exibindo relatório com formatação


# 5. Mostrando tipos dos dados


# ==========================================
# GABARITO (não olhe antes de tentar!)
# ==========================================

"""
# GABARITO DA TAREFA DE CASA - ENCONTRO 2
print("=== CONVERSOR UNIVERSAL DE MEDIDAS ===")

# 1. Coletando informações (sempre strings do input)
nome = input("Digite seu nome: ")
peso_str = input("Digite seu peso em kg: ")
altura_str = input("Digite sua altura em metros (ex: 1.75): ")
idade_str = input("Digite sua idade: ")

# 2. Fazendo conversões apropriadas
peso = float(peso_str)    # float para aceitar decimais (70.5)
altura = float(altura_str) # float para aceitar decimais (1.75)  
idade = int(idade_str)    # int porque idade é número inteiro

# 3. Realizando cálculos e conversões
peso_gramas = peso * 1000           # Convertendo kg para gramas
altura_cm = altura * 100            # Convertendo m para cm
imc = peso / (altura * altura)      # Calculando IMC
maior_idade = idade >= 18           # Boolean: True se >= 18

# 4. Exibindo relatório com formatação variada
print()
print("=" * 40)
print("       RELATÓRIO DE MEDIDAS")
print("=" * 40)

# Usando concatenação (+) em algumas linhas
print("Nome: " + nome)
print("Peso: " + str(peso) + " kg (" + str(peso_gramas) + " gramas)")

# Usando vírgulas em outras linhas  
print("Altura:", altura, "m (", altura_cm, "cm )")
print("Idade:", idade, "anos")
print("IMC:", round(imc, 2))

# Misturando os métodos
print("É maior de idade: " + str(maior_idade))

print("=" * 40)

# 5. Mostrando tipos dos dados
print()
print("=== ANÁLISE DOS TIPOS ===")
print("Nome:", nome, "- Tipo:", type(nome))
print("Peso:", peso, "- Tipo:", type(peso))
print("Altura:", altura, "- Tipo:", type(altura))
print("Idade:", idade, "- Tipo:", type(idade))
print("Maior idade:", maior_idade, "- Tipo:", type(maior_idade))
print("IMC:", round(imc, 2), "- Tipo:", type(imc))

print()
print("🎯 RESUMO DOS TIPOS USADOS:")
print("✅ str (string): Nome - texto")
print("✅ int (integer): Idade - número inteiro")
print("✅ float: Peso, altura, IMC - números decimais")
print("✅ bool (boolean): Maior idade - True/False")

print()
print("💡 OBSERVAÇÕES IMPORTANTES:")
print("- input() sempre retorna string")
print("- Conversões permitem cálculos matemáticos")
print("- Comparação (>=) gera boolean automaticamente")
print("- round(imc, 2) deixa 2 casas decimais")
print("- Concatenação (+) precisa de str() para números")
print("- Vírgulas no print() convertem automaticamente")

print()
print("🎉 Parabéns! Você dominou tipos e conversões!")

# VARIAÇÕES POSSÍVEIS PARA MELHORAR:
# 1. Usar f-strings: print(f"Nome: {nome}")
# 2. Validar se peso/altura são positivos
# 3. Adicionar classificação do IMC (baixo/normal/alto)
# 4. Criar bordas mais bonitas com caracteres especiais
# 5. Adicionar mais conversões (altura em pés/polegadas)

# CRITÉRIOS DE AVALIAÇÃO:
# ✅ Coletou 4 informações diferentes
# ✅ Fez conversões corretas (int, float)
# ✅ Realizou cálculos matemáticos
# ✅ Usou concatenação E vírgulas
# ✅ Criou boolean com comparação
# ✅ Mostrou tipos das variáveis
# ✅ Formatou saída de forma organizada
"""

print("\n💡 DICAS PARA MELHORAR:")
print("- Teste com valores decimais (70.5, 1.75)")
print("- Experimente idades diferentes (17, 18, 25)")
print("- Organize a saída com espaçamentos")
print("- Use nomes descritivos para as variáveis")
print("- Adicione comentários explicativos")

print("\n🚀 DESAFIOS EXTRAS:")
print("1. Adicione validação: peso/altura devem ser positivos")
print("2. Classifique o IMC: baixo (<18.5), normal (18.5-24.9), alto (>25)")
print("3. Calcule idade em dias (idade * 365)")
print("4. Adicione conversão altura para pés/polegadas")
print("5. Use f-strings para formatação mais limpa")