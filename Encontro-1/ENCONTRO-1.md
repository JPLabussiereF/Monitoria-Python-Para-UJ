# Encontro 1 - Algoritmos + Hello, World!
## Monitoria de Python - Engenharia da Computação

---

## 🎯 Objetivos de Aprendizagem

- Entender o conceito de algoritmo e sua aplicação na programação
- Conhecer o que é Python e como executar código básico
- Usar as funções `print()` e `input()` para entrada e saída de dados
- Identificar tipos básicos de dados usando `type()`
- Criar e executar o primeiro programa Python

---

## ⏰ Cronograma Detalhado (120 minutos)

| Tempo | Duração | Atividade | Descrição |
|-------|---------|-----------|-----------|
| 0-10 min | 10 min | **Abertura & Objetivos** | Apresentação, objetivos do encontro, motivação |
| 10-30 min | 20 min | **Teoria Enxuta** | Algoritmos, pseudocódigo, Python básico |
| 30-50 min | 20 min | **Demonstrações** | Hello World, input/print, type() |
| 50-85 min | 35 min | **Prática Guiada** | Passo a passo: nome, idade e tipos |
| 85-115 min | 30 min | **Lista de Exercícios** | 6 exercícios graduais + correção |
| 115-120 min | 5 min | **Revisão Relâmpago** | 4 perguntas rápidas de fixação |

---

## 📚 Resumo Teórico

### Conceitos Fundamentais

- **Algoritmo**: Sequência de passos lógicos para resolver um problema
- **Linguagem de programação**: Forma de "conversar" com o computador
- **Python**: Linguagem simples, poderosa e muito usada na engenharia
- **Código-fonte**: Texto que escrevemos e o computador executa
- **Entrada (Input)**: Dados que o programa recebe do usuário
- **Saída (Output)**: Dados que o programa mostra na tela
- **Função**: Comando que executa uma ação específica
- **String**: Texto entre aspas ("texto aqui")
- **Variável**: "Caixinha" que guarda um valor na memória
- **Tipo de dado**: Categoria do valor (texto, número, etc.)
- **Comentário**: Texto explicativo que não é executado (usa #)
- **Console/Terminal**: Tela preta onde vemos os resultados

### 🗣️ Glossário
- **`print()`**: Função que exibe texto/valores na tela
- **`input()`**: Função que lê texto digitado pelo usuário
- **`type()`**: Função que mostra o tipo de um valor
- **`#`**: Símbolo para comentários (explicações no código)

---

## 💻 Exemplos de Código

### Exemplo 1: Hello, World! Clássico
```python
# Meu primeiro programa Python!
print("Hello, World!")
print("Bem-vindo à programação!")
```
**Saída esperada:**
```
Hello, World!
Bem-vindo à programação!
```

### Exemplo 2: Interação Básica
```python
# Programa que interage com o usuário
nome = input("Digite seu nome: ")
print("Olá,", nome)
print("Seja bem-vindo ao Python!")
```
**Execução:**
```
Digite seu nome: João
Olá, João
Seja bem-vindo ao Python!
```

### Exemplo 3: Explorando Tipos
```python
# Descobrindo tipos de dados
nome = "Maria"
idade = 20

print("Nome:", nome)
print("Tipo do nome:", type(nome))
print("Idade:", idade)  
print("Tipo da idade:", type(idade))
```
**Saída:**
```
Nome: Maria
Tipo do nome: <class 'str'>
Idade: 20
Tipo da idade: <class 'int'>
```

---

## 👥 Prática Guiada (35 minutos)

### Passo a passo: "Programa Apresentação"

**Objetivo**: Criar um programa que pede nome e idade, depois mostra informações e os tipos das variáveis.

#### Passo 1 (5 min): Estrutura básica
```python
# Vamos criar nosso programa juntos!
```

#### Passo 2 (10 min): Coletando dados
```python
# Pedindo informações do usuário
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
```

#### Passo 3 (10 min): Mostrando resultados  
```python
# Exibindo as informações
print("Olá,", nome)
print("Você tem", idade, "anos")
```

#### Passo 4 (10 min): Explorando tipos
```python
# Descobrindo os tipos
print("O nome é do tipo:", type(nome))
print("A idade é do tipo:", type(idade))
```

**💡 Observação importante**: Tudo que vem do `input()` é texto (string), mesmo números!

---

## 📝 Lista de Exercícios

### Exercício 1 - Saudação Simples (Básico)
Escreva um programa que:
- Peça o nome do usuário
- Exiba "Bom dia, [nome]!"

**Exemplo de execução:**
```
Digite seu nome: Ana
Bom dia, Ana!
```

### Exercício 2 - Apresentação Completa (Básico)
Faça um programa que colete:
- Nome
- Idade  
- Cidade

E exiba: "Meu nome é [nome], tenho [idade] anos e moro em [cidade]."

### Exercício 3 - Explorador de Tipos (Intermediário)
Crie um programa que:
- Peça três valores diferentes ao usuário
- Mostre cada valor e seu tipo
- Use pelo menos um comentário explicativo

### Exercício 4 - Múltiplas Saídas (Intermediário)
Faça um programa que:
- Peça o nome de uma comida favorita
- Exiba essa informação de 3 formas diferentes usando `print()`

**Exemplo:**
```
Comida favorita: pizza
Eu gosto de pizza
Minha comida favorita é: pizza  
Comida: pizza
```

### Exercício 5 - Calculadora de Apresentação (Intermediário)
Programa que coleta:
- Nome
- Ano de nascimento
- Ano atual

E calcula/exibe a idade aproximada (sem considerar mês/dia).

### Exercício 6 - Investigador de Dados (Avançado)
Crie um programa que:
- Peça 4 informações diferentes (nome, idade, altura, tem_irmao)
- Para cada uma, exiba o valor E o tipo
- Organize a saída de forma clara e bonita

**Desafio Extra**: Tente fazer o usuário digitar "True" ou "False" para tem_irmao e explore o que acontece com o tipo!

---

## 🎯 Revisão Relâmpago (5 minutos)

1. **Qual função usamos para exibir texto na tela?**
2. **Como coletamos dados do usuário?**
3. **O que faz a função `type()`?**
4. **Todo valor que vem do `input()` é de que tipo?**

---

## ❌ Erros Comuns e Como Depurar

### 1. **Esquecimento de aspas**
```python
# ❌ Erro
print(Hello, World!)

# ✅ Correto  
print("Hello, World!")
```

### 2. **Parênteses esquecidos**
```python
# ❌ Erro
print "Oi"

# ✅ Correto
print("Oi")
```

### 3. **Misturar vírgulas e + no print**
```python
# ❌ Confuso (funciona mas pode dar erro depois)
nome = "João"
print("Olá " + nome + " você tem " + idade + " anos")  # idade precisa ser string!

# ✅ Recomendado
print("Olá", nome, "você tem", idade, "anos")
```

### 4. **Não salvar a entrada do input()**
```python
# ❌ Erro - o valor se perde
input("Digite seu nome: ")
print("Olá", nome)  # nome não existe!

# ✅ Correto
nome = input("Digite seu nome: ")
print("Olá", nome)
```

### 5. **Caracteres especiais sem aspas**
```python
# ❌ Erro
print(João tem 20 anos)

# ✅ Correto
print("João tem 20 anos")
```

---

## 🏠 Tarefa de Casa (10-15 minutos)

### Programa "Cartão de Visita Digital"

Crie um programa que:
1. Colete as seguintes informações:
   - Nome completo
   - Curso (pode escrever "Engenharia da Computação")
   - Uma curiosidade sobre você
   - Linguagem de programação que quer aprender

2. Exiba tudo organizado como um "cartão de visita"

3. No final, mostre o tipo de cada variável coletada

**Exemplo de saída:**
```
=== MEU CARTÃO DE VISITA ===
Nome: Maria Silva Santos
Curso: Engenharia da Computação  
Curiosidade: Gosto de tocar violão
Quer aprender: JavaScript

=== TIPOS DE DADOS ===
Nome é: <class 'str'>
Curso é: <class 'str'>
Curiosidade é: <class 'str'>
Linguagem é: <class 'str'>
```

---

## 📊 Rubrica de Avaliação

| Critério | Insuficiente | Básico | Bom | Ótimo |
|----------|--------------|--------|-----|-------|
| **Funcionamento** | Não executa | Executa com erros | Executa corretamente | Executa + trata casos especiais |
| **Uso do input()** | Não usa ou usa errado | Usa minimamente | Usa corretamente | Usa de forma criativa |
| **Uso do print()** | Saída confusa/incorreta | Saída básica | Saída organizada | Saída bem formatada |
| **Comentários** | Sem comentários | Poucos comentários | Comentários adequados | Comentários excelentes |
| **Organização** | Código bagunçado | Código básico | Código limpo | Código exemplar |

---

## 🚀 Sugestões de Extensão

### Para alunos mais rápidos:

1. **Experimentar com emojis**: Use emojis nos prints (copie/cole: 😊 🎉 💻)

2. **Múltiplas entradas em uma linha**: 
   ```python
   nome, idade = input("Digite nome e idade separados por vírgula: ").split(",")
   ```

3. **Formatação avançada com f-strings** (não cobraremos ainda):
   ```python
   nome = input("Nome: ")
   idade = input("Idade: ")
   print(f"Olá {nome}, você tem {idade} anos!")
   ```

4. **Explorar o que acontece** se você não colocar nada no `input("")`

5. **Investigar**: O que acontece se você usar `print()` sem nada dentro?

## 🔗 Próximo Encontro

**Encontro 2: Sintaxe, tipos e variáveis**
- Vamos aprofundar nos tipos: int, float, str, bool
- Aprenderemos conversões entre tipos
- Trabalharemos com formatação de saída
- Dica: Pratiquem bastante `input()` e `print()` esta semana!