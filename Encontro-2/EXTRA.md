# Lista de Exercícios — `input` e tipos de variáveis (Python)

Este EXTRA.md reúne atividades para praticar **coleta de dados com `input()`**, **conversões de tipos** e **operadores aritméticos** em Python. Resolva cada problema criando um pequeno programa que **leia dados do teclado** e **imprima o resultado** conforme solicitado.

## Como rodar
1. Use Python 3.11+ (ou similar).
2. Salve cada exercício em um arquivo `.py` separado (ex.: `ex01.py`, `ex02.py`, …).
3. Execute no terminal:  
   ```bash
   python ex01.py
   ```

## Dicas úteis
- Converta entradas numéricas com `int()` ou `float()`, por exemplo: `idade = int(input("Idade: "))`.
- Para **divisão**, valide que o **denominador é diferente de 0** antes de calcular.
- Para exibir números com casas decimais, use `format()` ou *f-strings*, por exemplo: `print(f"{valor:.2f}")`.
- Escreva mensagens claras para a pessoa usuária (prompts e resultados).

---

## Coleta e amostragem de dados

1. **Cumprimento simples**  
   Crie um programa que solicite à pessoa usuária digitar seu nome e imprima:  
   `Olá, [nome]!`

2. **Nome e idade**  
   Crie um programa que solicite à pessoa usuária digitar seu **nome** e **idade**, e imprima:  
   `Olá, [nome], você tem [idade] anos.`

3. **Nome, idade e altura**  
   Crie um programa que solicite à pessoa usuária digitar seu **nome**, **idade** e **altura em metros**, e imprima:  
   `Olá, [nome], você tem [idade] anos e mede [altura] metros!`

---

## Calculadora com operadores

4. **Soma de 2 valores**  
   Solicite **dois valores numéricos** e imprima a **soma** dos dois.

5. **Soma de 3 valores**  
   Solicite **três valores numéricos** e imprima a **soma** dos três.

6. **Subtração**  
   Solicite **dois valores numéricos** e imprima a **subtração do primeiro pelo segundo**.

7. **Multiplicação**  
   Solicite **dois valores numéricos** e imprima a **multiplicação** entre eles.

8. **Divisão**  
   Solicite **dois valores numéricos**, **numerador** e **denominador**, e **realize a divisão** entre eles.  
   > **Atenção:** o denominador **não pode ser 0**. Valide antes de dividir.

9. **Exponenciação**  
   Solicite **dois valores numéricos**, **base** e **expoente**, e **calcule a potência** (exponenciação) entre esses dois valores.

10. **Divisão inteira**  
    Solicite **dois valores numéricos**, **numerador** e **denominador**, e **realize a divisão inteira** entre eles (operador `//`).  
    > **Atenção:** o denominador **não pode ser 0**.

11. **Resto da divisão (módulo)**  
    Solicite **dois valores numéricos**, **numerador** e **denominador**, e **retorne o resto da divisão** (operador `%`).  
    > **Atenção:** o denominador **não pode ser 0**.

12. **Média simples de 3 notas**  
    Solicite **3 notas** de um estudante (valores numéricos) e **imprima a média** das notas.

13. **Média ponderada fixa**  
    Calcule e **imprima a média ponderada** dos números **5, 12, 20 e 15** com **pesos 1, 2, 3 e 4**, respectivamente.

---

## Sugestão de estrutura para cada exercício

```python
# exemplo_exercicio.py
def main():
    # 1) Entrada (input)
    # 2) Processamento (cálculo/validações)
    # 3) Saída (print do resultado)

if __name__ == "__main__":
    main()
```
