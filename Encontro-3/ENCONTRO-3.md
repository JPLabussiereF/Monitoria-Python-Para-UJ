# Encontro 3 - Operadores aritméticos, comparação e lógicos
## Monitoria de Python - Engenharia da Computação

---

## 🎯 Objetivos de Aprendizagem

- Dominar operadores aritméticos: `+`, `-`, `*`, `/`, `//`, `%`, `**` e suas precedências
- Aplicar operadores de comparação: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Compreender operadores lógicos: `and`, `or`, `not`
- Construir e interpretar tabelas-verdade práticas
- Resolver problemas com combinações de operadores (par/ímpar, médias, validações)

---

## ⏰ Cronograma Detalhado (120 minutos)

| Tempo | Duração | Atividade | Descrição |
|-------|---------|-----------|-----------|
| 0-10 min | 10 min | **Abertura & Revisão** | Review tipos/conversões, objetivos de hoje |
| 10-30 min | 20 min | **Teoria Enxuta** | 3 tipos de operadores + precedência |
| 30-50 min | 20 min | **Demonstrações** | Calculadora científica + tabela-verdade |
| 50-85 min | 35 min | **Prática Guiada** | Validador de dados passo a passo |
| 85-115 min | 30 min | **Lista de Exercícios** | 8 exercícios + correção colaborativa |
| 115-120 min | 5 min | **Revisão Relâmpago** | 5 perguntas sobre operadores |

---

## 📚 Resumo Teórico

### Operadores Aritméticos

- **`+`** : Adição (5 + 3 = 8)
- **`-`** : Subtração (5 - 3 = 2)  
- **`*`** : Multiplicação (5 * 3 = 15)
- **`/`** : Divisão real (5 / 2 = 2.5)
- **`//`** : Divisão inteira (5 // 2 = 2)
- **`%`** : Resto da divisão - módulo (5 % 2 = 1)
- **`**`** : Potenciação (5 ** 2 = 25)
- **Precedência**: `**` > `*, /, //, %` > `+, -` > comparação > lógicos
- **Parênteses**: Alteram precedência (2 + 3 * 4 = 14, mas (2 + 3) * 4 = 20)
- **Associatividade**: Operações da esquerda para direita (exceto `**`)

### Operadores de Comparação

- **`==`** : Igual a (5 == 5 → True)
- **`!=`** : Diferente de (5 != 3 → True)
- **`<`** : Menor que (3 < 5 → True)
- **`>`** : Maior que (5 > 3 → True)
- **`<=`** : Menor ou igual (3 <= 3 → True)
- **`>=`** : Maior ou igual (5 >= 5 → True)
- **Resultado**: Sempre retorna `True` ou `False` (boolean)

### Operadores Lógicos

- **`and`** : E lógico (True and True = True)
- **`or`** : OU lógico (True or False = True)
- **`not`** : NÃO lógico (not True = False)
- **Precedência**: `not` > `and` > `or`
- **Avaliação preguiçosa**: Para na primeira condição que define o resultado

### 🗣️ Glossário
- **Módulo (%)**: Resto da divisão inteira
- **Floor division (//)**: Divisão que descarta a parte decimal
- **Boolean**: Resultado das comparações e operações lógicas
- **Expressão**: Combinação de valores e operadores que produz um resultado
- **Precedência**: Ordem de execução dos operadores

---

## 💻 Exemplos de Código

### Exemplo 1: Operadores Aritméticos na Prática
```python
# Calculadora de despesas
preco_produto = 29.90
quantidade = 3
desconto_percent = 10

# Usando diferentes operadores
subtotal = preco_produto * quantidade
desconto = subtotal * desconto_percent / 100
total = subtotal - desconto

print("Preço unitário: R$", preco_produto)
print("Quantidade:", quantidade)
print("Subtotal: R$", round(subtotal, 2))
print("Desconto:", desconto_percent, "% = R$", round(desconto, 2))
print("Total final: R$", round(total, 2))

# Operadores especiais
print("\n=== OPERADORES ESPECIAIS ===")
print("Divisão real:", 10 / 3)      # 3.3333...
print("Divisão inteira:", 10 // 3)   # 3
print("Resto:", 10 % 3)              # 1
print("Potência:", 2 ** 8)           # 256
```

### Exemplo 2: Comparações em Ação
```python
# Sistema de notas
nota = float(input("Digite sua nota (0-10): "))

# Comparações básicas
passou = nota >= 7.0
ficou_exame = 5.0 <= nota < 7.0
reprovou = nota < 5.0

print("Nota digitada:", nota)
print("Passou direto:", passou)
print("Ficou de exame:", ficou_exame)
print("Reprovou:", reprovou)

# Comparações múltiplas
print("Nota máxima?", nota == 10.0)
print("Nota válida?", 0.0 <= nota <= 10.0)
```

### Exemplo 3: Tabela-Verdade Interativa
```python
# Construindo tabela-verdade para AND
print("=== TABELA-VERDADE: AND ===")
print("A     | B     | A and B")
print("------|-------|--------")
print("True  | True  |", True and True)
print("True  | False |", True and False)  
print("False | True  |", False and True)
print("False | False |", False and False)

print("\n=== TABELA-VERDADE: OR ===")
print("A     | B     | A or B")
print("------|-------|-------")
print("True  | True  |", True or True)
print("True  | False |", True or False)
print("False | True  |", False or True)
print("False | False |", False or False)

print("\n=== TABELA-VERDADE: NOT ===")
print("A     | not A")
print("------|------")
print("True  |", not True)
print("False |", not False)
```

---

## 👥 Prática Guiada (35 minutos)

### Passo a passo: "Validador de Dados Pessoais"

**Objetivo**: Criar um sistema que coleta e valida dados usando todos os tipos de operadores.

#### Passo 1 (10 min): Estrutura e coleta
```python
# Validador de dados pessoais
print("=== VALIDADOR DE DADOS ===")

# Coletando informações
nome = input("Nome completo: ")
idade = int(input("Idade: "))
salario = float(input("Salário: "))
tem_experiencia = input("Tem experiência? (sim/não): ").lower() == "sim"
```

#### Passo 2 (10 min): Validações com comparadores
```python
# Validações básicas usando comparadores
nome_valido = len(nome) >= 2 and len(nome) <= 50
idade_valida = idade >= 16 and idade <= 65
salario_valido = salario > 0
dados_obrigatorios = nome_valido and idade_valida and salario_valido

print("\n=== VALIDAÇÕES BÁSICAS ===")
print("Nome válido (2-50 chars):", nome_valido)
print("Idade válida (16-65 anos):", idade_valida)  
print("Salário válido (> 0):", salario_valido)
print("Dados obrigatórios OK:", dados_obrigatorios)
```

#### Passo 3 (10 min): Cálculos e classificações
```python
# Cálculos usando operadores aritméticos
salario_anual = salario * 12
imposto = salario_anual * 0.15 if salario_anual > 20000 else 0
salario_liquido = salario_anual - imposto

# Classificações usando operadores lógicos
eh_jovem = idade < 25
eh_senior = idade >= 45
faixa_salarial_boa = salario >= 3000
perfil_ideal = tem_experiencia and faixa_salarial_boa and not eh_senior

print("\n=== CÁLCULOS E ANÁLISES ===")
print("Salário anual: R$", round(salario_anual, 2))
print("Imposto estimado: R$", round(imposto, 2))
print("Salário líquido: R$", round(salario_liquido, 2))
print("É jovem profissional:", eh_jovem)
print("Perfil ideal para vaga:", perfil_ideal)
```

#### Passo 4 (5 min): Relatório final
```python
# Relatório usando operadores mistos
print("\n=== RELATÓRIO FINAL ===")
if dados_obrigatorios and perfil_ideal:
    print("✅ APROVADO: Todos os critérios atendidos!")
elif dados_obrigatorios:
    print("⚠️ PENDENTE: Dados válidos, mas perfil não ideal")
else:
    print("❌ REJEITADO: Dados inválidos")

# Sugestões usando operadores
if not nome_valido:
    print("- Corrija o nome (mínimo 2, máximo 50 caracteres)")
if not (16 <= idade <= 65):
    print("- Idade deve estar entre 16 e 65 anos")
if salario <= 0:
    print("- Salário deve ser maior que zero")
```

---

## 📝 Lista de Exercícios

### Exercício 1 - Calculadora Básica (Básico)
Programa que:
- Pede dois números
- Exibe TODOS os operadores aritméticos entre eles
- Inclua divisão real, inteira, resto e potência

**Exemplo**: Para 10 e 3:
```
10 + 3 = 13
10 - 3 = 7
10 * 3 = 30
10 / 3 = 3.33
10 // 3 = 3
10 % 3 = 1
10 ** 3 = 1000
```

### Exercício 2 - Detector de Par/Ímpar (Básico)
Crie um programa que:
- Pede um número inteiro
- Usa o operador módulo (%) para determinar se é par ou ímpar
- Exibe o resultado como boolean

**Dica**: Um número é par quando `numero % 2 == 0`

### Exercício 3 - Comparador de Idades (Intermediário)
Colete idades de 3 pessoas e:
- Use comparadores para encontrar quem é mais velho/novo
- Determine quantas são maiores de idade (>= 18)
- Verifique se todas têm a mesma idade

### Exercício 4 - Tabela-Verdade Personalizada (Intermediário)
Peça dois valores boolean (True/False) ao usuário e:
- Construa uma tabela-verdade mostrando AND, OR e NOT
- Use formatação organizada
- Explique o resultado de cada operação

### Exercício 5 - Calculadora de Média com Validação (Intermediário)
Sistema que:
- Coleta 4 notas (0-10)
- Valida se cada nota está no intervalo correto
- Calcula média usando operadores aritméticos
- Determina status: aprovado (>=7), exame (5-6.9), reprovado (<5)

### Exercício 6 - Analisador de Números (Avançado)
Para um número fornecido, determine:
- Se é positivo, negativo ou zero
- Se é par ou ímpar  
- Se é múltiplo de 3, 5 ou ambos (como FizzBuzz)
- Se é um número "perfeito" (quando soma dos divisores = número)

### Exercício 7 - Sistema de Login Simples (Avançado)
Simule um sistema que:
- Pede usuário e senha
- Valida se usuário tem pelo menos 5 caracteres
- Valida se senha tem pelo menos 8 caracteres E contém números
- Use operadores lógicos para determinar acesso liberado

### Exercício 8 - Calculadora de Desconto Inteligente (Avançado)
Sistema de e-commerce que:
- Pede preço do produto e quantidade
- Aplica desconto progressivo: 5% (>100), 10% (>500), 15% (>1000)
- Calcula frete: grátis se total > 200, senão R$ 15
- Use todos os tipos de operadores

**Desafio Extra**: Crie um "Jogo de Adivinhação Matemática" onde o usuário deve descobrir se uma expressão matemática é verdadeira ou falsa!

---

## 🎯 Revisão Relâmpago (5 minutos)

1. **Qual operador calcula o resto da divisão?**
2. **Qual a diferença entre `/` e `//`?**
3. **Como verificar se um número é par?**
4. **`True and False` resulta em quê?**
5. **Qual tem maior precedência: `+` ou `*`?**

---

## ❌ Erros Comuns e Como Depurar

### 1. **Confundir atribuição (=) com comparação (==)**
```python
# ❌ Erro comum
idade = 18
if idade = 18:  # SyntaxError!
    print("Maior de idade")

# ✅ Correto
if idade == 18:  # Comparação
    print("Tem exatamente 18 anos")
```

### 2. **Precedência de operadores**
```python
# ❌ Resultado inesperado
resultado = 2 + 3 * 4  # 14, não 20!
print("2 + 3 * 4 =", resultado)

# ✅ Use parênteses para clareza
resultado = (2 + 3) * 4  # 20
print("(2 + 3) * 4 =", resultado)
```

### 3. **Divisão por zero**
```python
# ❌ Runtime error
numero = 0
resultado = 10 / numero  # ZeroDivisionError!

# ✅ Sempre validar antes
if numero != 0:
    resultado = 10 / numero
    print("Resultado:", resultado)
else:
    print("Não é possível dividir por zero!")
```

### 4. **Confundir operadores lógicos com bitwise**
```python
# ❌ Operadores bitwise por acidente
condicao1 = True
condicao2 = False
resultado = condicao1 & condicao2  # Bitwise AND, não lógico!

# ✅ Operadores lógicos
resultado = condicao1 and condicao2  # Lógico AND
```

### 5. **Não entender avaliação preguiçosa**
```python
# Exemplo de avaliação preguiçosa
idade = 15
tem_permissao = False

# Se idade < 18 for True, nem verifica tem_permissao
pode_dirigir = idade >= 18 and tem_permissao
print("Pode dirigir:", pode_dirigir)  # False

# `or` para quando a primeira condição já determina o resultado
eh_vip = idade >= 65 or tem_permissao  
```

### 6. **Problemas com números decimais**
```python
# ⚠️ Cuidado com precisão de float
print(0.1 + 0.2 == 0.3)  # False! (problema de precisão)

# ✅ Para comparações de float, use round()
resultado = 0.1 + 0.2
print(round(resultado, 1) == 0.3)  # True
```

---

## 🏠 Tarefa de Casa (15-20 minutos)

### "Calculadora Científica com Validação"

Crie um programa completo que:

1. **Menu de operações**:
   - Mostre opções: +, -, *, /, //, %, **
   - Peça dois números e a operação desejada

2. **Validações usando operadores**:
   - Números devem ser válidos (não vazios)
   - Não permitir divisão por zero (/ e //)
   - Operação deve estar no menu

3. **Cálculos com todos os operadores**:
   - Execute a operação escolhida
   - Mostre resultado formatado
   - Para divisão, mostre real E inteira

4. **Análises extras com operadores lógicos**:
   - Determine se o resultado é par/ímpar
   - Verifique se é positivo, negativo ou zero
   - Classifique como "pequeno" (<100), "médio" (100-1000) ou "grande" (>1000)

5. **Tabela-verdade bônus**:
   - Compare se ambos os números são positivos
   - Use AND, OR e NOT para análises

**Exemplo de execução:**
```
=== CALCULADORA CIENTÍFICA ===
Operações: +, -, *, /, //, %, **

Primeiro número: 15
Segundo número: 4
Operação: **

Resultado: 15 ** 4 = 50625

=== ANÁLISE DO RESULTADO ===
É par: False
É positivo: True  
Classificação: grande (> 1000)

=== ANÁLISE DOS NÚMEROS ===
Ambos positivos: True and True = True
Pelo menos um positivo: True or True = True
```

---

## 📊 Rubrica de Avaliação

| Critério | Insuficiente | Básico | Bom | Ótimo |
|----------|--------------|--------|-----|-------|
| **Operadores Aritméticos** | Usa poucos ou incorretamente | Usa básicos (+, -, *, /) | Usa todos corretamente | Usa todos + precedência |
| **Comparações** | Confunde = e == | Usa comparações simples | Usa variados comparadores | Usa comparações complexas |
| **Lógicos** | Não usa ou usa errado | Usa and/or básico | Usa and/or/not correto | Combina lógicos complexos |
| **Validações** | Sem validações | Validações simples | Validações adequadas | Validações robustas |
| **Formatação** | Saída confusa | Saída funcional | Saída organizada | Saída profissional |

---

## 🚀 Sugestões de Extensão

### Para alunos mais rápidos:

1. **Operadores de comparação encadeados**:
   ```python
   idade = 25
   if 18 <= idade <= 65:
       print("Idade trabalhista válida")
   ```

2. **Operador ternário (condicional)**:
   ```python
   status = "maior" if idade >= 18 else "menor"
   ```

3. **Operadores bitwise** (avançado):
   ```python
   print(5 & 3)  # AND bitwise
   print(5 | 3)  # OR bitwise  
   print(5 ^ 3)  # XOR bitwise
   ```

4. **Verificador de números primos**:
   ```python
   numero = 17
   eh_primo = numero > 1 and all(numero % i != 0 for i in range(2, int(numero**0.5) + 1))
   ```

5. **Calculadora de expressões**:
   - Use `eval()` com cuidado para avaliar expressões matemáticas
   - Validate entrada antes de usar eval()

---

## 🔗 Próximo Encontro

**Encontro 4: Estruturas condicionais (if / elif / else)**
- **if simples e compostos**
- **elif para múltiplas condições**  
- **else como fallback**
- **Indentação e blocos**
- **Aninhamento de condicionais**
- **Projeto**: Sistema de classificação de notas completo

**Dica**: Os operadores de hoje serão a base das condições! Pratiquem bastante comparações e operadores lógicos! 🎯

---

## 💡 Dica Final

**Operadores são as ferramentas para criar lógica!**

- **Aritméticos**: Fazem os cálculos
- **Comparação**: Testam condições  
- **Lógicos**: Combinam decisões

Dominem esses 3 grupos e terão superpoderes para resolver qualquer problema lógico! 🧮⚡