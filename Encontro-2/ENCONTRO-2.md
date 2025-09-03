# Encontro 2 - Sintaxe, tipos e variáveis
## Monitoria de Python - Engenharia da Computação

---

## 🎯 Objetivos de Aprendizagem

- Dominar os 4 tipos básicos: `int`, `float`, `str`, `bool`
- Realizar conversões entre tipos usando `int()`, `float()`, `str()`, `bool()`
- Compreender quando usar concatenação (+) vs vírgulas no `print()`
- Aplicar formatação básica de saída de dados
- Resolver problemas práticos com entrada, conversão e saída formatada

---

## ⏰ Cronograma Detalhado (120 minutos)

| Tempo | Duração | Atividade | Descrição |
|-------|---------|-----------|-----------|
| 0-10 min | 10 min | **Abertura & Revisão** | Review do Encontro 1, objetivos de hoje |
| 10-30 min | 20 min | **Teoria Enxuta** | Tipos de dados e conversões |
| 30-50 min | 20 min | **Demonstrações** | Exemplos práticos de conversão |
| 50-85 min | 35 min | **Prática Guiada** | Calculadora de IMC passo a passo |
| 85-115 min | 30 min | **Lista de Exercícios** | 7 exercícios graduais + correção |
| 115-120 min | 5 min | **Revisão Relâmpago** | 5 perguntas de fixação |

---

## 📚 Resumo Teórico

### Tipos de Dados Fundamentais

- **`int` (Integer)**: Números inteiros (-2, 0, 15, 1000)
- **`float` (Float)**: Números com casas decimais (3.14, -0.5, 2.0)
- **`str` (String)**: Texto entre aspas ("João", "123", "")
- **`bool` (Boolean)**: Valores lógicos (True, False)
- **Conversão**: Transformar um tipo em outro
- **Concatenação**: Juntar strings com o operador +
- **Formatação**: Organizar a saída de dados de forma legível
- **Casting**: Outro nome para conversão de tipos
- **TypeError**: Erro quando tentamos operações incompatíveis entre tipos
- **ValueError**: Erro quando a conversão não é possível
- **Imutabilidade**: Strings não podem ser alteradas após criadas
- **Aspas simples vs duplas**: Ambas funcionam para strings ('text' ou "text")

### 🗣️ Glossário
- **`int()`**: Converte para número inteiro
- **`float()`**: Converte para número decimal
- **`str()`**: Converte para texto/string
- **`bool()`**: Converte para True/False
- **`.` (ponto)**: Separador decimal em Python (3.14, não 3,14)

---

## 💻 Exemplos de Código

### Exemplo 1: Descobrindo e Convertendo Tipos
```python
# Coletando dados como string
idade_texto = input("Sua idade: ")
altura_texto = input("Sua altura (ex: 1.75): ")

# Convertendo para números
idade = int(idade_texto)
altura = float(altura_texto)

print("Idade:", idade, "- Tipo:", type(idade))
print("Altura:", altura, "- Tipo:", type(altura))

# Fazendo cálculos (agora é possível!)
print("Daqui a 10 anos você terá:", idade + 10, "anos")
```

### Exemplo 2: Trabalhando com Booleans
```python
# Diferentes formas de criar booleans
maior_idade = True
tem_carteira = False

# Conversões interessantes
print(bool("Python"))     # True (string não vazia)
print(bool(""))           # False (string vazia)
print(bool(42))           # True (número diferente de zero)
print(bool(0))            # False (zero é falso)

# Usando em contexto
nome = input("Nome: ")
if nome:  # Se o nome não for vazio
    print("Nome válido!")
```

### Exemplo 3: Concatenação vs Vírgulas
```python
nome = "Ana"
idade = 20

# ❌ Erro comum: misturar tipos na concatenação
# print("Olá " + nome + ", você tem " + idade + " anos")  # TypeError!

# ✅ Método 1: Conversão manual  
print("Olá " + nome + ", você tem " + str(idade) + " anos")

# ✅ Método 2: Vírgulas (mais fácil)
print("Olá", nome, ", você tem", idade, "anos")

# ✅ Método 3: f-strings (mais avançado)
print(f"Olá {nome}, você tem {idade} anos")
```

---

## 👥 Prática Guiada (35 minutos)

### Passo a passo: "Calculadora de IMC"

**Objetivo**: Criar um programa que calcula o Índice de Massa Corporal, trabalhando com conversões e formatação.

#### Passo 1 (5 min): Estrutura e coleta
```python
# Calculadora de IMC
print("=== CALCULADORA DE IMC ===")

# Coletando dados (sempre strings!)
nome = input("Seu nome: ")
peso_str = input("Seu peso (kg): ")
altura_str = input("Sua altura (m, ex: 1.75): ")
```

#### Passo 2 (10 min): Conversões e validação
```python
# Convertendo para números
peso = float(peso_str)
altura = float(altura_str)

# Verificando os tipos
print("Peso:", peso, "- Tipo:", type(peso))
print("Altura:", altura, "- Tipo:", type(altura))
```

#### Passo 3 (10 min): Cálculos e formatação
```python
# Calculando IMC (peso / altura²)
imc = peso / (altura * altura)

# Exibindo resultado formatado
print("\n=== RESULTADO ===")
print("Nome:", nome)
print("IMC:", round(imc, 2))  # Arredondando para 2 casas decimais
```

#### Passo 4 (10 min): Melhorando a saída
```python
# Versão mais bonita
print(f"\n{nome}, seu IMC é: {imc:.2f}")

# Convertendo de volta para string se necessário
imc_texto = str(round(imc, 2))
print("IMC como texto:", imc_texto, "- Tipo:", type(imc_texto))
```

**💡 Pontos de discussão:**
- Por que precisamos converter?
- O que acontece sem conversão?
- Como escolher entre int() e float()?

---

## 📝 Lista de Exercícios

### Exercício 1 - Conversor de Idade (Básico)
Programa que:
- Pede o ano atual e ano de nascimento
- Converte para números
- Calcula e exibe a idade

**Exemplo:**
```
Ano atual: 2025
Ano de nascimento: 2003
Sua idade é: 22 anos
```

### Exercício 2 - Calculadora Simples (Básico)
Colete dois números e:
- Mostre os tipos antes da conversão
- Converta para float
- Exiba a soma dos dois números

**Dica**: Use float() para aceitar decimais

### Exercício 3 - Formatador de Dados (Intermediário)
Programa que coleta:
- Nome
- Idade (converter para int)
- Altura (converter para float)
- É estudante? (sim/não - converter para bool com lógica)

Exiba tudo formatado e com os tipos corretos.

### Exercício 4 - Conversor de Temperatura (Intermediário)
Converta Celsius para Fahrenheit:
- Cole temperatura em Celsius
- Converta para float
- Aplique a fórmula: F = C × 9/5 + 32
- Exiba o resultado formatado

**Exemplo**: 25°C = 77.0°F

### Exercício 5 - Analisador de Texto vs Número (Intermediário)
Peça um valor ao usuário e:
- Exiba como string
- Tente converter para int (se possível)
- Tente converter para float (se possível)
- Analise o que é possível fazer

**Dica**: Use try/except ou valide manualmente

### Exercício 6 - Calculadora de Média (Avançado)
Colete 3 notas:
- Converta todas para float
- Calcule a média
- Determine se é aprovado (média ≥ 7.0)
- Exiba resultado booleano e formatado

### Exercício 7 - Construtor de Frase (Avançado)
Colete:
- Nome, idade, cidade, salário_desejado
- Faça todas as conversões apropriadas
- Construa uma frase usando concatenação (+)
- Construa a mesma frase usando vírgulas
- Compare os métodos

**Desafio Extra**: Crie um "cartão de dados" que mostre cada informação com seu tipo, tudo organizadinho!

---

## 🎯 Revisão Relâmpago (5 minutos)

1. **Quais são os 4 tipos básicos em Python?**
2. **Como converter "25" (string) para número inteiro?**
3. **Qual a diferença entre int() e float()?**
4. **Por que print("Idade: " + 20) dá erro?**
5. **bool("") retorna True ou False?**

---

## ❌ Erros Comuns e Como Depurar

### 1. **TypeError na concatenação**
```python
# ❌ Erro comum
nome = "João"
idade = 20
print("Olá " + nome + ", idade: " + idade)  # TypeError!

# ✅ Soluções
print("Olá " + nome + ", idade: " + str(idade))  # Converte
print("Olá", nome, ", idade:", idade)             # Vírgulas
```

### 2. **ValueError na conversão**
```python
# ❌ Problema
texto = "abc"
numero = int(texto)  # ValueError: invalid literal

# ✅ Como verificar
texto = input("Digite um número: ")
if texto.isdigit():  # Só dígitos?
    numero = int(texto)
    print("Número:", numero)
else:
    print("Isso não é um número!")
```

### 3. **Confusão com decimais**
```python
# ❌ Formato brasileiro confunde
# altura = float("1,75")  # ValueError! Python usa ponto

# ✅ Correto
altura = float("1.75")  # Ponto é separador decimal
print("Altura:", altura)
```

### 4. **Perda de precisão com int()**
```python
# ⚠️ Cuidado: int() corta decimais
preco = 19.99
preco_int = int(preco)  # Vira 19, não 20!
print("Preço:", preco_int)  # 19 (perdeu .99)

# ✅ Para arredondar, use round()
preco_arred = round(preco)  # 20
```

### 5. **Bool() com valores inesperados**
```python
# Valores que são False:
print(bool(0))        # False
print(bool(""))       # False
print(bool(False))    # False

# Tudo mais é True:
print(bool("0"))      # True (string não vazia!)
print(bool(-5))       # True (número diferente de zero)
print(bool("False"))  # True (string não vazia!)
```

---

## 🏠 Tarefa de Casa (15-20 minutos)

### "Conversor Universal de Medidas"

Crie um programa que:

1. **Colete informações**:
   - Nome da pessoa
   - Peso em quilos (float)
   - Altura em metros (float) 
   - Idade em anos (int)

2. **Faça conversões**:
   - Peso para gramas (peso * 1000)
   - Altura para centímetros (altura * 100)
   - Calcule IMC (peso / altura²)

3. **Exiba um relatório organizado**:
   - Use concatenação para algumas linhas
   - Use vírgulas para outras linhas
   - Mostre pelo menos 3 tipos de dados diferentes

4. **Desafio**: Determine se a pessoa é maior de idade (18+) e exiba como boolean

**Exemplo de saída esperada:**
```
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
```

---

## 📊 Rubrica de Avaliação

| Critério | Insuficiente | Básico | Bom | Ótimo |
|----------|--------------|--------|-----|-------|
| **Conversões** | Não converte ou converte errado | Converte alguns tipos | Converte corretamente | Converte + valida entrada |
| **Uso dos tipos** | Mistura tipos incorretamente | Usa tipos básicos | Usa tipos apropriados | Escolhe tipos otimizados |
| **Formatação** | Saída confusa/incorreta | Saída básica | Saída organizada | Saída profissional |
| **Cálculos** | Não funciona | Cálculos simples | Cálculos corretos | Cálculos + tratamento |
| **Código** | Muito confuso | Funciona com erros | Código limpo | Código exemplar |

---

## 🚀 Sugestões de Extensão

### Para alunos mais rápidos:

1. **Validação de entrada**:
   ```python
   while True:
       try:
           idade = int(input("Idade: "))
           break  # Sai do loop se converteu
       except ValueError:
           print("Digite apenas números!")
   ```

2. **Formatação com f-strings**:
   ```python
   nome = "Ana"
   idade = 20
   print(f"Olá {nome}, você tem {idade} anos!")
   ```

3. **Experimentar com round()**:
   ```python
   pi = 3.14159265359
   print(f"Pi com 2 casas: {round(pi, 2)}")
   print(f"Pi com 4 casas: {round(pi, 4)}")
   ```

4. **Descobrir outros tipos**:
   ```python
   import datetime
   hoje = datetime.date.today()
   print("Hoje:", hoje, "- Tipo:", type(hoje))
   ```

5. **Mini-projeto**: Criar uma calculadora que aceita operações como texto e converte tudo apropriadamente.

---

## 🔗 Próximo Encontro

**Encontro 3: Operadores aritméticos, comparação e lógicos**
- **Aritméticos**: +, -, *, /, //, %, ** (precedência)
- **Comparação**: ==, !=, <, >, <=, >=
- **Lógicos**: and, or, not (tabela-verdade!)
- **Dica**: Pratiquem conversões - serão muito usadas com operadores!

---

## 💡 Dica Final

**Os tipos são a base de tudo em Python!** 

Dominando `int`, `float`, `str` e `bool` + suas conversões, vocês estarão preparados para qualquer desafio. No próximo encontro, vamos usar esses tipos com operadores para criar lógicas mais complexas! 🚀