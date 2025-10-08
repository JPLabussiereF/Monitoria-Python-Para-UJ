# Loops em Python — Guia Rápido

> Domine `for`, `while`, `range()`, `break`, `continue` e loops aninhados, com exemplos práticos e boas práticas.  
> Baseado no material apresentado em aula (slides).

## 1) O que são loops?
Loops permitem **repetir um bloco de código** várias vezes, de forma controlada, evitando duplicação e tornando seu programa mais **claro e eficiente**.  
Use loops para **processar listas**, **automatizar tarefas repetitivas** e **percorrer sequências**.

## 2) Tipos principais
- **`for`**: percorre cada item de uma sequência (lista, string, `range`, etc.).  
  Útil quando você **sabe** (ou consegue calcular) o número de iterações.
- **`while`**: repete **enquanto** uma condição for verdadeira.  
  Útil quando você **não sabe** quantas vezes vai repetir.

## 3) `for` — Estrutura e exemplo
```py
for variavel in sequencia:
    # bloco a executar

for numero in [1, 2, 3, 4, 5]:
    print(numero)
```

## 4) `while` — Estrutura e exemplo
```py
contador = 1
while contador <= 5:
    print(contador)
    contador = contador + 1  # evite loops infinitos!
```

## 5) `range()` — Gerando sequências numéricas
- `range(fim)`: 0 até `fim - 1`  
- `range(inicio, fim)`: `inicio` até `fim - 1`  
- `range(inicio, fim, passo)`: pula conforme `passo`
```py
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8
```

## 6) Percorrendo listas com `for`
```py
frutas = ['maçã', 'banana', 'laranja', 'uva']
for fruta in frutas:
    print(f'Eu gosto de {fruta}!')
```

## 7) `break` e `continue`
- **`break`**: **interrompe** o loop por completo.
- **`continue`**: **pula** a iteração atual e vai para a próxima.
```py
for n in range(1, 8):
    if n == 5:
        break       # para tudo aqui
    if n % 2 == 0:
        continue    # pula pares
    print(n)        # imprime 1, 3
```

## 8) Loops aninhados
Um loop **dentro** de outro loop. Cuidado com a complexidade!
```py
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
```

## 9) Boas práticas
- Dê **nomes claros** às variáveis (`for fruta in frutas`).
- Garanta término do `while` (atualize a condição).
- Use `break`/`continue` com **parcimônia** e motivo claro.
- Prefira **compreensões de lista** quando for só transformar/coletar dados:
```py
quadrados = [n*n for n in range(6)]  # [0,1,4,9,16,25]
```

## 10) Erros comuns
- **Loop infinito** em `while` (condição nunca fica falsa).
- **Índices fora do alcance** ao percorrer listas por índice.
- **Mutação** da coleção enquanto itera (faça cópias quando necessário).

## 11) Mini checklist antes de rodar
- Qual é a **condição de parada**?
- O contador/estado está sendo **atualizado**?
- Preciso mesmo de `while` ou um `for+range` resolve melhor?
- Preciso percorrer **itens** (for x in lista) ou **índices** (for i in range(...))?

---

Feito para acompanhar sua tutoria. Bons estudos e bons loops! :)