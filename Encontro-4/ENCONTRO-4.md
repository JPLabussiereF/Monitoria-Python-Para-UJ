# Encontro 4 - Estruturas condicionais (if / elif / else)
## Monitoria de Python - Engenharia da Computação

---

## 🎯 Objetivos de Aprendizagem

- Dominar a estrutura `if` para execução condicional
- Aplicar `elif` para múltiplas condições mutuamente exclusivas  
- Usar `else` como alternativa padrão (fallback)
- Compreender indentação e blocos de código em Python
- Implementar condicionais aninhadas (if dentro de if)
- Validar entradas de usuário com estruturas condicionais
- Criar sistemas de classificação e tomada de decisão

---

## ⏰ Cronograma Detalhado (120 minutos)

| Tempo | Duração | Atividade | Descrição |
|-------|---------|-----------|-----------|
| 0-10 min | 10 min | **Abertura & Revisão** | Review operadores, introdução às condicionais |
| 10-30 min | 20 min | **Teoria Enxuta** | if/elif/else, indentação, blocos |
| 30-50 min | 20 min | **Demonstrações** | Classificador de notas + validações |
| 50-85 min | 35 min | **Prática Guiada** | Sistema de aprovação acadêmica |
| 85-115 min | 30 min | **Lista de Exercícios** | 8 exercícios + correção em duplas |
| 115-120 min | 5 min | **Revisão Relâmpago** | 5 perguntas sobre condicionais |

---

## 📚 Resumo Teórico

### Estruturas Condicionais Básicas

- **`if`**: Executa bloco SE condição for True
- **`elif`**: "Senão se" - condição adicional mutuamente exclusiva 
- **`else`**: "Senão" - executado se nenhuma condição anterior for True
- **Indentação**: 4 espaços ou 1 tab para definir blocos (OBRIGATÓRIA!)
- **Bloco**: Conjunto de linhas com mesma indentação
- **Condição**: Expressão que resulta em True ou False
- **Aninhamento**: if dentro de if (níveis de decisão)
- **Condições compostas**: Usando and, or, not
- **Validação**: Verificar se dados estão corretos antes de processar
- **Fluxo de execução**: Ordem que o código é executado
- **Mutuamente exclusivo**: Apenas uma condição pode ser executada
- **Fallback**: Alternativa padrão quando nenhuma condição é atendida

### 🗣️ Glossário
- **Indentação**: Espaços/tabs no início da linha que definem hierarquia
- **Bloco de código**: Linhas agrupadas pela mesma indentação  
- **Condição booleana**: Expressão que retorna True ou False
- **Ramificação**: Divisão do fluxo do programa em diferentes caminhos

---

## 💻 Exemplos de Código

### Exemplo 1: if Básico - Maioridade
```python
# Verificação simples de maioridade
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você é maior de idade!")
    print("Pode dirigir e votar.")
    
print("Este print sempre executa")  # Fora do bloco if
```

### Exemplo 2: if/else - Classificação Binária
```python
# Classificação par ou ímpar
numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print(f"{numero} é PAR")
    print("Divisível por 2")
else:
    print(f"{numero} é ÍMPAR")
    print("Não é divisível por 2")
    
print("Análise concluída!")
```

### Exemplo 3: if/elif/else - Classificação Múltipla
```python
# Sistema de notas
nota = float(input("Digite sua nota (0-10): "))

if nota >= 9.0:
    print("Conceito A - Excelente!")
    print("Parabéns pelo desempenho!")
elif nota >= 7.0:
    print("Conceito B - Bom!")
    print("Aprovado com mérito!")
elif nota >= 5.0:
    print("Conceito C - Regular")
    print("Aprovado por média")
else:
    print("Conceito D - Insuficiente")
    print("Reprovado - estude mais!")
    
# Validação adicional
if 0 <= nota <= 10:
    print("Nota válida registrada")
else:
    print("⚠️ Atenção: Nota fora do intervalo 0-10")
```

---

## 👥 Prática Guiada (35 minutos)

### Passo a passo: "Sistema de Aprovação Acadêmica"

**Objetivo**: Criar sistema completo que avalia estudante considerando notas, frequência e atividades extras.

#### Passo 1 (10 min): Coleta e validação básica
```python
# Sistema de Aprovação Acadêmica
print("=== SISTEMA DE APROVAÇÃO ===")

# Coletando dados
nome = input("Nome do estudante: ")
nota1 = float(input("Primeira nota (0-10): "))
nota2 = float(input("Segunda nota (0-10): "))
frequencia = float(input("Frequência (%): "))
atividades_extras = input("Participou de atividades extras? (sim/não): ").lower()

# Validação de dados
dados_validos = True

if nota1 < 0 or nota1 > 10:
    print("❌ Primeira nota inválida!")
    dados_validos = False
    
if nota2 < 0 or nota2 > 10:
    print("❌ Segunda nota inválida!")
    dados_validos = False
    
if frequencia < 0 or frequencia > 100:
    print("❌ Frequência inválida!")
    dados_validos = False
```

#### Passo 2 (15 min): Lógica de aprovação
```python
if dados_validos:
    # Cálculos
    media = (nota1 + nota2) / 2
    tem_extras = atividades_extras == "sim"
    
    print(f"\n=== ANÁLISE DE {nome.upper()} ===")
    print(f"Média: {media:.1f}")
    print(f"Frequência: {frequencia}%")
    print(f"Atividades extras: {tem_extras}")
    
    # Critérios de aprovação
    media_suficiente = media >= 7.0
    frequencia_ok = frequencia >= 75.0
    
    # Decisão principal
    if media_suficiente and frequencia_ok:
        print("\n🎉 STATUS: APROVADO DIRETO")
        if tem_extras:
            print("💫 Com menção de destaque!")
            
    elif media >= 5.0 and frequencia_ok:
        print("\n📚 STATUS: APROVADO COM RECUPERAÇÃO")
        print("Realize prova final")
        
    elif media >= 5.0 and frequencia >= 50.0:
        print("\n⚠️ STATUS: RECUPERAÇÃO TOTAL") 
        print("Prova final + frequência extra")
        
    else:
        print("\n❌ STATUS: REPROVADO")
        if media < 5.0:
            print("- Média insuficiente")
        if frequencia < 50.0:
            print("- Frequência insuficiente")
```

#### Passo 3 (10 min): Recomendações e relatório
```python
    # Recomendações personalizadas
    print(f"\n=== RECOMENDAÇÕES ===")
    
    if media < 6.0:
        print("📖 Foque nos estudos teóricos")
        if not tem_extras:
            print("📋 Participe de atividades extras")
    
    if frequencia < 80.0:
        print("📅 Melhore sua assiduidade")
        
    if media >= 9.0 and frequencia >= 90.0:
        print("🏆 Candidato a bolsa de estudos!")
        
    # Relatório final
    print(f"\n=== RELATÓRIO FINAL ===")
    print(f"Estudante: {nome}")
    print(f"Média final: {media:.2f}")
    print(f"Frequência: {frequencia:.1f}%")
    print(f"Situação: ", end="")
    
    if media_suficiente and frequencia_ok:
        print("APROVADO ✅")
    else:
        print("EM RECUPERAÇÃO ⚠️")
        
else:
    print("\n❌ Corrija os dados e tente novamente!")
```

**💡 Conceitos trabalhados:**
- Validação com múltiplos `if`
- Condições compostas (`and`, `or`)
- Aninhamento de decisões
- `elif` para classificação
- Personalização baseada em condições

---

## 📝 Lista de Exercícios

### Exercício 1 - Verificador de Maioridade (Básico)
Programa que:
- Pede idade do usuário
- Usa `if/else` para determinar se é maior de idade
- Exibe mensagens diferentes para cada caso

**Exemplo**: Idade 17 → "Menor de idade, aguarde X anos para ser maior"

### Exercício 2 - Calculadora de IMC com Classificação (Básico)
Sistema que:
- Calcula IMC (peso/altura²)
- Classifica usando `if/elif/else`:
  - Abaixo de 18.5: Abaixo do peso
  - 18.5-24.9: Peso normal
  - 25-29.9: Sobrepeso
  - 30+: Obesidade

### Exercício 3 - Sistema de Login (Intermediário)
Crie um sistema que:
- Pede usuário e senha
- Valida credenciais (defina usuário/senha fixos)
- Use condições aninhadas para diferentes tipos de erro
- Dê mensagens específicas para cada problema

### Exercício 4 - Classificador de Triângulos (Intermediário)
Programa que:
- Pede 3 lados de um triângulo
- Valida se formam um triângulo válido
- Classifica como: Equilátero, Isósceles ou Escaleno
- Use múltiplas condições e validações

### Exercício 5 - Sistema de Desconto Progressivo (Intermediário)
E-commerce que:
- Pede valor da compra e se é cliente VIP
- Aplica descontos baseados em valor E status
- Use condições aninhadas para combinações
- Calcule valor final e economia

### Exercício 6 - Aprovação de Empréstimo (Avançado)
Sistema bancário que:
- Coleta: renda, idade, score, tempo de trabalho
- Aplica múltiplos critérios com `if/elif/else` aninhados
- Determina aprovação, valor limite e taxa de juros
- Dê explicações para recusa

### Exercício 7 - Jogo de Pedra, Papel, Tesoura (Avançado)
Implemente o jogo clássico:
- Jogador escolhe pedra/papel/tesoura
- Computador escolhe aleatoriamente
- Use condições para determinar vencedor
- Valide entrada do usuário

### Exercício 8 - Analisador de Senha Complexo (Avançado)
Sistema que:
- Pede senha do usuário
- Valida múltiplos critérios:
  - Comprimento mínimo
  - Letras maiúsculas e minúsculas
  - Números e símbolos
- Use condições aninhadas para dar feedback específico
- Classifique força: fraca/média/forte

**Desafio Extra**: Crie um "Quiz Inteligente" que faz perguntas diferentes baseadas nas respostas anteriores!

---

## 🎯 Revisão Relâmpago (5 minutos)

1. **Qual a diferença entre `if` e `elif`?**
2. **Quando usar `else`?**
3. **Por que a indentação é obrigatória?**
4. **Como fazer condições compostas?**
5. **O que acontece quando nenhuma condição é True?**

---

## ❌ Erros Comuns e Como Depurar

### 1. **IndentationError - Erro de indentação**
```python
# ❌ Erro comum
if idade >= 18:
print("Maior de idade")  # Sem indentação!

# ✅ Correto
if idade >= 18:
    print("Maior de idade")  # 4 espaços ou 1 tab
```

### 2. **Misturar espaços e tabs**
```python
# ❌ Inconsistente
if condicao:
    print("Linha 1")    # 4 espaços
	print("Linha 2")    # 1 tab - ERRO!

# ✅ Consistente - sempre use a mesma
if condicao:
    print("Linha 1")    # 4 espaços
    print("Linha 2")    # 4 espaços
```

### 3. **Condições que nunca executam**
```python
# ❌ Lógica incorreta
nota = 8.5
if nota >= 9:
    print("Excelente")
elif nota >= 7:    # Esta condição nunca será testada se nota >= 9
    print("Bom")
elif nota >= 8:    # ❌ NUNCA executará! 8.5 já foi capturado acima
    print("Muito bom")

# ✅ Ordem correta
if nota >= 9:
    print("Excelente") 
elif nota >= 8:      # ✅ Testará 8-8.9
    print("Muito bom")
elif nota >= 7:      # ✅ Testará 7-7.9
    print("Bom")
```

### 4. **Esquecer dois pontos (:)**
```python
# ❌ Erro de sintaxe
if idade >= 18  # Sem os dois pontos!
    print("Maior de idade")

# ✅ Correto
if idade >= 18:  # Dois pontos obrigatórios
    print("Maior de idade")
```

### 5. **Condições sempre True ou False**
```python
# ❌ Condição sempre True
if 5 > 3:  # Sempre verdadeiro!
    print("Sempre executa")

# ❌ Comparação com atribuição
nome = "João"
if nome = "João":  # ❌ Erro! Deveria ser ==
    print("É o João")

# ✅ Correto
if nome == "João":  # Comparação correta
    print("É o João")
```

### 6. **Blocos vazios**
```python
# ❌ Bloco vazio causa erro
if condicao:
# Sem nada aqui causa IndentationError

# ✅ Use pass para bloco temporariamente vazio
if condicao:
    pass  # Placeholder - sem ação por enquanto
```

---

## 🏠 Tarefa de Casa (20-25 minutos)

### "Sistema de Classificação de Filmes"

Crie um sistema completo que:

1. **Coleta informações**:
   - Nome do filme
   - Gênero (ação, comédia, drama, terror, ficção)
   - Nota do usuário (0-10)
   - Idade do usuário
   - É assinante premium? (sim/não)

2. **Validações com condicionais**:
   - Nota deve estar entre 0-10
   - Idade deve ser positiva
   - Gênero deve ser válido

3. **Sistema de recomendação usando if/elif/else**:
   - Terror: só para idade >= 16
   - Ação: recomendado para >= 13  
   - Drama: qualquer idade
   - Comédia: +14 para alguns tipos
   - Ficção: +12

4. **Classificação da avaliação**:
   - 9-10: Obra-prima
   - 7-8.9: Muito bom
   - 5-6.9: Regular
   - 3-4.9: Ruim
   - 0-2.9: Péssimo

5. **Benefícios de assinante premium**:
   - Acesso antecipado (qualquer nota)
   - Desconto em ingressos (nota >= 7)
   - Conteúdo exclusivo (nota >= 8)

**Exemplo de saída:**
```
=== SISTEMA DE CLASSIFICAÇÃO DE FILMES ===
Nome: Vingadores
Gênero: ação
Nota: 8.5
Idade: 17
Premium: sim

=== ANÁLISE ===
✅ Filme adequado para sua idade
⭐ Classificação: Muito bom (8.5/10)
🎬 Recomendação: Altamente recomendado!

=== BENEFÍCIOS PREMIUM ===
✅ Acesso antecipado liberado
✅ Desconto em ingressos: 20%
❌ Conteúdo exclusivo (precisa nota >= 8)

Deseja assistir? Acesso liberado! 🍿
```

---

## 📊 Rubrica de Avaliação

| Critério | Insuficiente | Básico | Bom | Ótimo |
|----------|--------------|--------|-----|-------|
| **Uso do if** | Não usa ou usa errado | if simples correto | if com else | if aninhados complexos |
| **elif/else** | Não usa | elif básico | elif múltiplo | elif bem estruturado |
| **Indentação** | Erros constantes | Algumas inconsistências | Consistente | Perfeita organização |
| **Validações** | Sem validações | Validações básicas | Validações adequadas | Validações robustas |
| **Lógica** | Fluxo confuso | Lógica simples | Lógica clara | Lógica sofisticada |

---

## 🚀 Sugestões de Extensão

### Para alunos mais rápidos:

1. **Operador ternário** (condicional inline):
   ```python
   status = "maior" if idade >= 18 else "menor"
   ```

2. **Múltiplas condições encadeadas**:
   ```python
   if 0 <= nota <= 10 and idade > 0 and genero in generos_validos:
       # Processo principal
   ```

3. **Match/case (Python 3.10+)**:
   ```python
   match genero:
       case "ação":
           print("Adrenalina pura!")
       case "comédia":
           print("Prepare-se para rir!")
       case _:
           print("Gênero interessante!")
   ```

4. **Condicionais com funções**:
   ```python
   def pode_assistir(idade, genero):
       if genero == "terror":
           return idade >= 16
       return idade >= 0
   ```

5. **Sistema de menu interativo**:
   ```python
   opcao = input("Escolha (1/2/3): ")
   if opcao == "1":
       # Ação 1
   elif opcao == "2":
       # Ação 2
   else:
       print("Opção inválida!")
   ```

---

## 📋 Checklist da Aula

**Para o monitor:**
- [ ] Testei todos os exemplos de indentação
- [ ] Preparei casos de IndentationError para mostrar
- [ ] Revisei diferenças entre if/elif/else
- [ ] Tenho exemplos de condições aninhadas
- [ ] Preparei validações de entrada realistas

**Para o aluno:**
- [ ] Entendo quando usar if vs elif vs else
- [ ] Sei indentar corretamente (4 espaços)
- [ ] Consigo criar condições compostas
- [ ] Faço validação de entrada
- [ ] Implementei pelo menos 2 condicionais aninhadas
- [ ] Completei pelo menos 6 exercícios

---

## 🔗 Próximo Encontro

**Encontro 5: Laços de repetição (for in, range, while, break/continue)**
- **for in range()**: Repetições controladas
- **while**: Repetições baseadas em condição
- **break/continue**: Controle de fluxo
- **Aninhamento**: Laços dentro de laços
- **Projeto final**: Jogo de adivinhação com contador

**Dica**: As condicionais de hoje serão fundamentais dentro dos laços! Pratiquem `if/elif/else` até ficar automático! 🔄

---

## 💡 Dica Final

**Estruturas condicionais são o cérebro do programa!**

Elas transformam dados em decisões:
- **if**: "Se isso, então aquilo"
- **elif**: "Senão se isso, então aquilo outro"  
- **else**: "Nos demais casos, faça isso"

**A indentação não é decoração - é sintaxe obrigatória!** 

Dominem condicionais e terão o poder de criar programas que "pensam" e tomam decisões inteligentes! 🧠✨