# 13 EXERCÍCIOS - ESTRUTURAS CONDICIONAIS
**if / elif / else - Níveis Fácil e Médio**

---

## 🟢 NÍVEL FÁCIL (Exercícios 1-5)

### **EXERCÍCIO 1: Verificador de Maioridade**
**Objetivo:** Praticar if/else básico

Escreva um programa que:
- Peça a idade do usuário
- Verifique se é maior de idade (≥18)
- Exiba "Maior de idade" ou "Menor de idade"

**Exemplo de execução:**
```
Digite sua idade: 20
Resultado: Maior de idade
```

---

### **EXERCÍCIO 2: Classificador de Temperatura**
**Objetivo:** Usar if/elif/else para categorizar

Crie um programa que:
- Receba uma temperatura em Celsius
- Classifique como:
  - Frio: menor que 15°C
  - Agradável: entre 15°C e 25°C
  - Quente: maior que 25°C

**Exemplo de execução:**
```
Digite a temperatura: 22
Resultado: Temperatura agradável
```

---

### **EXERCÍCIO 3: Calculadora de Desconto**
**Objetivo:** Praticar comparações e cálculos

Desenvolva um programa que:
- Peça o valor de uma compra
- Aplique desconto:
  - 10% se compra ≥ R$ 100
  - Sem desconto se compra < R$ 100
- Mostre o valor final

**Exemplo de execução:**
```
Valor da compra: 150
Desconto aplicado: R$ 15.00
Valor final: R$ 135.00
```

---

### **EXERCÍCIO 4: Par ou Ímpar**
**Objetivo:** Usar operador % (módulo)

Crie um programa que:
- Receba um número inteiro
- Verifique se é par ou ímpar
- Exiba o resultado

**Exemplo de execução:**
```
Digite um número: 7
Resultado: 7 é ÍMPAR
```

---

### **EXERCÍCIO 5: Positivo, Negativo ou Zero**
**Objetivo:** Múltiplas condições simples

Escreva um programa que:
- Receba um número
- Identifique se é:
  - Positivo (> 0)
  - Negativo (< 0)
  - Zero (= 0)

**Exemplo de execução:**
```
Digite um número: -5
Resultado: Número negativo
```

---

## 🟡 NÍVEL MÉDIO (Exercícios 6-11)

### **EXERCÍCIO 6: Calculadora de IMC Completa**
**Objetivo:** Múltiplas faixas de classificação

Crie um programa que:
- Peça peso (kg) e altura (m)
- Calcule o IMC: `IMC = peso / (altura ** 2)`
- Classifique em:
  - Abaixo do peso: IMC < 18.5
  - Peso normal: 18.5 ≤ IMC < 25
  - Sobrepeso: 25 ≤ IMC < 30
  - Obesidade: IMC ≥ 30

**Exemplo de execução:**
```
Digite seu peso (kg): 70
Digite sua altura (m): 1.75
Seu IMC: 22.86
Classificação: Peso normal
```

---

### **EXERCÍCIO 7: Sistema de Notas**
**Objetivo:** Validação + classificação

Desenvolva um programa que:
- Receba uma nota de 0 a 10
- Valide se está entre 0 e 10
- Classifique em:
  - A: nota ≥ 9
  - B: 7 ≤ nota < 9
  - C: 5 ≤ nota < 7
  - D: nota < 5

**Exemplo de execução:**
```
Digite a nota: 8.5
Conceito: B
```

---

### **EXERCÍCIO 8: Verificador de Triângulo**
**Objetivo:** Condições compostas (and)

Crie um programa que:
- Receba 3 lados (a, b, c)
- Verifique se formam um triângulo válido:
  - `a + b > c` AND `a + c > b` AND `b + c > a`
- Classifique o tipo:
  - Equilátero: todos os lados iguais
  - Isósceles: dois lados iguais
  - Escaleno: todos os lados diferentes

**Exemplo de execução:**
```
Lado 1: 5
Lado 2: 5
Lado 3: 5
Resultado: Triângulo Equilátero válido
```

---

### **EXERCÍCIO 9: Sistema de Login Simples**
**Objetivo:** Comparação de strings + condições compostas

Desenvolva um programa que:
- Defina usuário correto: "admin"
- Defina senha correta: "1234"
- Peça usuário e senha
- Verifique se ambos estão corretos
- Dê feedback específico:
  - Usuário incorreto
  - Senha incorreta
  - Login bem-sucedido

**Exemplo de execução:**
```
Usuário: admin
Senha: 1234
✅ Login realizado com sucesso!
```

---

### **EXERCÍCIO 10: Calculadora de Aposentadoria**
**Objetivo:** Múltiplas condições com and/or

Crie um programa que:
- Peça idade e tempo de contribuição (anos)
- Regras para aposentar:
  - Idade ≥ 65 anos, OU
  - Tempo de contribuição ≥ 35 anos, OU
  - Idade ≥ 60 E tempo ≥ 30
- Informe se pode aposentar

**Exemplo de execução:**
```
Idade: 62
Tempo de contribuição: 32
Resultado: ✅ Pode se aposentar!
```

---

### **EXERCÍCIO 11: Classificador de Faixa Etária**
**Objetivo:** Múltiplas categorias

Escreva um programa que:
- Receba a idade
- Classifique em:
  - Criança: 0-12 anos
  - Adolescente: 13-17 anos
  - Adulto: 18-59 anos
  - Idoso: 60+ anos
- Valide se idade é positiva

**Exemplo de execução:**
```
Digite a idade: 45
Classificação: Adulto
```

---

## 🟠 NÍVEL MÉDIO+ (Exercícios 12-13)

### **EXERCÍCIO 12: Sistema de Aprovação Escolar**
**Objetivo:** Múltiplas validações + lógica composta

Desenvolva um programa que:
- Peça nota (0-10) e frequência (0-100%)
- Valide ambos os valores
- Regras de aprovação:
  - Nota ≥ 7 E frequência ≥ 75%: APROVADO
  - Nota ≥ 5 E < 7 E frequência ≥ 75%: RECUPERAÇÃO
  - Qualquer outro caso: REPROVADO

**Exemplo de execução:**
```
Digite a nota (0-10): 8.5
Digite a frequência (%): 80
Status: APROVADO ✅
```

---

### **EXERCÍCIO 13: Recomendador de Filmes**
**Objetivo:** Múltiplas condições aninhadas

Crie um programa que:
- Peça a idade do usuário
- Pergunte o gênero preferido (ação, comédia, terror)
- Recomende filmes baseado em:
  - **Ação:**
    - < 13 anos: "Homem-Aranha"
    - 13-17 anos: "Vingadores"
    - 18+ anos: "John Wick"
  - **Comédia:**
    - < 13 anos: "Divertida Mente"
    - 13+ anos: "Deadpool"
  - **Terror:**
    - < 16 anos: "Não recomendado para sua idade"
    - 16+ anos: "Invocação do Mal"

**Exemplo de execução:**
```
Digite sua idade: 20
Escolha o gênero (ação/comédia/terror): ação
Recomendação: John Wick 🎬
```

---

## 📝 DICAS PARA RESOLVER:

1. **Sempre valide a entrada** antes de processar
2. **Use variáveis descritivas** (idade, nota, peso)
3. **Teste casos extremos** (valores mínimos e máximos)
4. **Indente corretamente** (4 espaços)
5. **Não esqueça os dois pontos** após if/elif/else
6. **Use f-strings** para saída formatada: `print(f"Resultado: {valor}")`

---

## 🎯 SUGESTÃO DE PRÁTICA:

- **Exercícios 1-3:** Aquecer conceitos básicos
- **Exercícios 4-7:** Consolidar if/elif/else
- **Exercícios 8-11:** Dominar condições compostas
- **Exercícios 12-13:** Desafio final

**Meta:** Complete pelo menos 8 exercícios para dominar condicionais! 💪

---

## 📚 RECURSOS ADICIONAIS:

- [Documentação Python - Estruturas de Controle](https://docs.python.org/pt-br/3/tutorial/controlflow.html)
- Pratique online: [Python Tutor](http://pythontutor.com/)
- Teste seus códigos: [Repl.it](https://replit.com/)

---

**Bons estudos! 🚀**