# Lista de Exercícios — Loops em Python
# Agora sem funções, apenas blocos de código para facilitar o estudo.

# 1) Imprima os números de 1 a 10 usando for.
for n in range(1, 11):
    print(n)

print("="*30)

# 2) Imprima os números pares de 0 a 20 usando for + range, mas, pule 2 em 2.
for n in range(0, 21, 2):
    print(n)

print("="*30)

# 3) Use while para imprimir de 10 até 1 (decrescente).
n = 10
while n >= 1:
    print(n)
    n -= 1

print("="*30)

# 4) Percorra a lista e imprima "Eu gosto de <item>".
lista_frutas = ["maçã", "banana", "laranja", "uva"]
for fruta in lista_frutas:
    print("Eu gosto de", fruta)

print("="*30)

# 5) Some todos os números de 1 a 100 (for + acumulador).
soma = 0
for n in range(1, 101):
    soma += n
print("Soma:", soma)

print("="*30)

# 6) Peça números ao usuário até ele digitar 0. E some os números digitados (while).
print("Digite números para somar; 0 encerra.")
total = 0
while True:
    n = int(input("> "))
    if n == 0:
        break
    total += n
print("Total:", total)

print("="*30)

# 7) Imprima somente os ímpares de 1 a 20 usando continue.
for n in range(1, 21):
    if n % 2 == 0:
        continue
    print(n)

print("="*30)

# 8) Procure o número 7 em uma lista e pare ao encontrá-lo (break).
numeros = [1, 3, 5, 7, 9, 11]
for n in numeros:
    if n == 7:
        print("Encontrei o 7!")
        break
    print("Lendo:", n)

print("="*30)

# 9) Tabela (matriz 3x3) com loops aninhados imprimindo pares (i, j).
for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i},{j})", end=" ")
    print()

print("="*30)

# 10) Faça a tabuada de 1 a 5 (loops aninhados).
for n in range(1, 6):
    print("Tabuada do", n)
    for m in range(1, 11):
        print(n, "x", m, "=", n*m)
    print("-" * 12)

print("="*30)

# 11) Dada uma string, conte quantas vogais ela possui (for).
texto = input("Digite um texto: ").lower()
vogais = "aeiou"
cont = 0
for ch in texto:
    if ch in vogais:
        cont += 1
print("Vogais:", cont)

print("="*30)

# 12) Leia notas até digitar -1; calcule média (while; trate divisão por zero).
print("Digite notas; -1 encerra.")
soma = 0
qtd = 0
while True:
    nota = float(input("> "))
    if nota == -1:
        break
    soma += nota
    qtd += 1

media = soma / qtd if qtd > 0 else 0.0
print("Média:", round(media, 2))