# GABARITO - ENCONTRO 4: Estruturas condicionais (if / elif / else)
# Monitoria de Python - Engenharia da Computação

"""
GABARITO COMPLETO
Soluções comentadas focando em estruturas condicionais
"""

print("=== GABARITO - ENCONTRO 4 ===")
print()

# ======================================
# EXERCÍCIO 1 - VERIFICADOR DE MAIORIDADE
# ======================================
print("1. VERIFICADOR DE MAIORIDADE")
print("=" * 35)

# Solução:
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("🎉 Você é maior de idade!")
    print("Direitos: votar, dirigir, trabalhar sem restrições")
else:
    anos_faltam = 18 - idade
    print(f"📅 Menor de idade - aguarde {anos_faltam} ano(s)")
    print("Aproveite esta fase da vida!")

# Informações adicionais baseadas na idade
if idade >= 65:
    print("🏆 Direito à meia-entrada em eventos")
elif idade >= 16:
    print("📝 Pode votar (facultativo até 18)")

print("\n💡 EXPLICAÇÃO:")
print("- if/else para classificação binária (maior/menor)")
print("- Cálculo dentro da estrutura condicional")
print("- elif adicional para casos específicos")
print("- Mensagens personalizadas para cada faixa")
print()

print("-" * 60)

# ======================================
# EXERCÍCIO 2 - CALCULADORA DE IMC COM CLASSIFICAÇÃO  
# ======================================
print("2. CALCULADORA DE IMC COM CLASSIFICAÇÃO")
print("=" * 45)

# Solução:
print("=== CALCULADORA DE IMC ===")
peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))

# Validação de entrada
if peso <= 0 or altura <= 0:
    print("❌ ERRO: Peso e altura devem ser positivos!")
else:
    # Cálculo do IMC
    imc = peso / (altura * altura)
    print(f"\nIMC calculado: {imc:.2f}")
    
    # Classificação usando if/elif/else
    if imc < 18.5:
        categoria = "Abaixo do peso"
        recomendacao = "Considere ganhar peso de forma saudável"
        emoji = "⬇️"
    elif imc < 25.0:  # 18.5 <= imc < 25.0
        categoria = "Peso normal"
        recomendacao = "Mantenha seus hábitos saudáveis!"
        emoji = "✅"
    elif imc < 30.0:  # 25.0 <= imc < 30.0
        categoria = "Sobrepeso"
        recomendacao = "Considere exercícios e dieta balanceada"
        emoji = "⚠️"
    else:  # imc >= 30.0
        categoria = "Obesidade"
        recomendacao = "Procure orientação médica"
        emoji = "🚨"
    
    print(f"\n{emoji} Categoria: {categoria}")
    print(f"💡 Recomendação: {recomendacao}")
    
    # Análise adicional
    if imc < 16:
        print("⚠️ IMC muito baixo - consulte um médico")
    elif imc > 35:
        print("🚨 IMC muito alto - atenção médica urgente")

print("\n💡 EXPLICAÇÃO:")
print("- Validação inicial com if para evitar erros")
print("- elif em sequência para faixas de IMC")
print("- Cada elif testa o próximo intervalo automaticamente")
print("- else captura todos os casos restantes (>=30)")
print("- Condicionais adicionais para casos extremos")
print()

print("-" * 60)

# ======================================
# EXERCÍCIO 3 - SISTEMA DE LOGIN
# ======================================
print("3. SISTEMA DE LOGIN")
print("=" * 25)

# Solução:
print("=== SISTEMA DE LOGIN ===")

# Credenciais corretas (hardcoded para o exercício)
USUARIO_CORRETO = "admin"
SENHA_CORRETA = "12345"

usuario = input("Usuário: ")
senha = input("Senha: ")

# Sistema de validação com condições aninhadas
if usuario == USUARIO_CORRETO:
    if senha == SENHA_CORRETA:
        print("🔓 LOGIN REALIZADO COM SUCESSO!")
        print(f"Bem-vindo, {usuario}!")
        print("Acesso ao sistema liberado.")
    else:
        print("🔒 ACESSO NEGADO: Senha incorreta")
        print("💡 Dica: Verifique se o Caps Lock está desligado")
else:
    print("🔒 ACESSO NEGADO: Usuário não encontrado")
    if senha == SENHA_CORRETA:
        print("💡 A senha está correta, mas o usuário está errado")
    else:
        print("💡 Usuário E senha estão incorretos")

# Versão alternativa com condições compostas
print("\n--- VERSÃO ALTERNATIVA ---")
if usuario == USUARIO_CORRETO and senha == SENHA_CORRETA:
    print("✅ Acesso liberado com operador AND")
else:
    print("❌ Falha na autenticação")
    # Diagnóstico específico
    if usuario != USUARIO_CORRETO and senha != SENHA_CORRETA:
        print("- Usuário E senha incorretos")
    elif usuario != USUARIO_CORRETO:
        print("- Apenas usuário incorreto")
    else:
        print("- Apenas senha incorreta")

print("\n💡 EXPLICAÇÃO:")
print("- if aninhado: primeiro valida usuário, depois senha")
print("- Condições compostas: and para validar ambos")
print("- Mensagens específicas para cada tipo de erro")
print("- Diagnóstico detalhado ajuda o usuário")
print()

print("-" * 60)

# ======================================
# EXERCÍCIO 4 - CLASSIFICADOR DE TRIÂNGULOS
# ======================================
print("4. CLASSIFICADOR DE TRIÂNGULOS")
print("=" * 35)

# Solução:
print("=== CLASSIFICADOR DE TRIÂNGULOS ===")
lado1 = float(input("Primeiro lado: "))
lado2 = float(input("Segundo lado: "))
lado3 = float(input("Terceiro lado: "))

# Validação: lados devem ser positivos
if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
    print("❌ ERRO: Todos os lados devem ser positivos!")
else:
    # Validação: desigualdade triangular
    # Para formar triângulo: soma de dois lados > terceiro lado
    if (lado1 + lado2 > lado3 and 
        lado1 + lado3 > lado2 and 
        lado2 + lado3 > lado1):
        
        print("✅ Os valores formam um triângulo válido!")
        print(f"Lados: {lado1}, {lado2}, {lado3}")
        
        # Classificação do triângulo
        if lado1 == lado2 == lado3:
            tipo = "EQUILÁTERO"
            descricao = "Todos os lados são iguais"
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            tipo = "ISÓSCELES"
            descricao = "Dois lados são iguais"
        else:
            tipo = "ESCALENO"
            descricao = "Todos os lados são diferentes"
        
        print(f"\n📐 Tipo: {tipo}")
        print(f"📝 Descrição: {descricao}")
        
        # Análise adicional: tipo de ângulo (usando Pitágoras)
        lados = sorted([lado1, lado2, lado3])
        a, b, c = lados[0], lados[1], lados[2]  # c é o maior lado
        
        if abs(c*c - (a*a + b*b)) < 0.001:  # Pytágoras (com tolerância)
            print("📐 Ângulo: Triângulo retângulo")
        elif c*c > a*a + b*b:
            print("📐 Ângulo: Triângulo obtusângulo")
        else:
            print("📐 Ângulo: Triângulo acutângulo")
            
    else:
        print("❌ Os valores NÃO formam um triângulo!")
        print("💡 Lembre-se: soma de dois lados > terceiro lado")
        
        # Diagnóstico específico
        if lado1 + lado2 <= lado3:
            print(f"- Problema: {lado1} + {lado2} = {lado1 + lado2} ≤ {lado3}")
        elif lado1 + lado3 <= lado2:
            print(f"- Problema: {lado1} + {lado3} = {lado1 + lado3} ≤ {lado2}")
        else:
            print(f"- Problema: {lado2} + {lado3} = {lado2 + lado3} ≤ {lado1}")

print("\n💡 EXPLICAÇÃO:")
print("- Validação em camadas: positivos → desigualdade triangular")
print("- Condições compostas com and para múltiplas verificações")
print("- elif para classificação mutuamente exclusiva")
print("- sorted() para organizar lados e facilitar cálculos")
print("- abs() para lidar com imprecisão de float")
print()

print("-" * 60)

# ======================================
# EXERCÍCIO 5 - SISTEMA DE DESCONTO PROGRESSIVO
# ======================================
print("5. SISTEMA DE DESCONTO PROGRESSIVO")
print("=" * 40)

# Solução:
print("=== E-COMMERCE - SISTEMA DE DESCONTO ===")
valor_compra = float(input("Valor da compra: R$ "))
eh_vip = input("Cliente VIP? (sim/não): ").lower() == "sim"

if valor_compra <= 0:
    print("❌ ERRO: Valor da compra deve ser positivo!")
else:
    print(f"\nValor original: R$ {valor_compra:.2f}")
    print(f"Cliente VIP: {'Sim' if eh_vip else 'Não'}")
    
    # Sistema de desconto com condições aninhadas
    desconto_percentual = 0
    
    if eh_vip:
        # Descontos VIP (maiores)
        if valor_compra >= 1000:
            desconto_percentual = 20
        elif valor_compra >= 500:
            desconto_percentual = 15
        elif valor_compra >= 200:
            desconto_percentual = 10
        else:
            desconto_percentual = 5  # VIP sempre tem desconto
    else:
        # Descontos cliente comum
        if valor_compra >= 1000:
            desconto_percentual = 15
        elif valor_compra >= 500:
            desconto_percentual = 10
        elif valor_compra >= 200:
            desconto_percentual = 5
        # else: sem desconto (0%)
    
    # Cálculos finais
    desconto_valor = valor_compra * desconto_percentual / 100
    valor_final = valor_compra - desconto_valor
    economia = desconto_valor
    
    print(f"\n=== RESUMO DO PEDIDO ===")
    print(f"Desconto aplicado: {desconto_percentual}%")
    print(f"Valor do desconto: R$ {desconto_valor:.2f}")
    print(f"Valor final: R$ {valor_final:.2f}")
    print(f"Economia: R$ {economia:.2f}")
    
    # Incentivos adicionais
    if not eh_vip and valor_compra >= 100:
        print("\n💎 PROMOÇÃO: Torne-se VIP e ganhe desconto extra!")
    
    if desconto_percentual == 0:
        proximo_desconto = 200
        falta = proximo_desconto - valor_compra
        print(f"\n💡 Adicione R$ {falta:.2f} e ganhe 5% de desconto!")
    
    # Análise do benefício VIP
    if eh_vip:
        if valor_compra >= 200:
            desconto_comum = 5 if valor_compra >= 200 else 0
            if valor_compra >= 1000:
                desconto_comum = 15
            elif valor_compra >= 500:
                desconto_comum = 10
            
            beneficio_vip = desconto_percentual - desconto_comum
            if beneficio_vip > 0:
                print(f"\n⭐ Benefício VIP: +{beneficio_vip}% de desconto extra!")

print("\n💡 EXPLICAÇÃO:")
print("- Condições aninhadas: primeiro status VIP, depois valor")
print("- elif em sequência para faixas de desconto")
print("- Cálculos realizados após determinar desconto")
print("- Incentivos baseados em condições específicas")
print("- Comparação entre benefícios VIP e comum")
print()

print("-" * 60)

# ======================================
# EXERCÍCIO 6 - APROVAÇÃO DE EMPRÉSTIMO
# ======================================
print("6. APROVAÇÃO DE EMPRÉSTIMO")
print("=" * 30)

# Solução:
print("=== SISTEMA BANCÁRIO - ANÁLISE DE CRÉDITO ===")
renda = float(input("Renda mensal: R$ "))
idade = int(input("Idade: "))
score = int(input("Score de crédito (0-1000): "))
tempo_trabalho = int(input("Tempo no trabalho atual (meses): "))

# Validação de entrada
dados_validos = True

if renda <= 0:
    print("❌ Renda deve ser positiva")
    dados_validos = False
    
if idade < 18 or idade > 80:
    print("❌ Idade deve estar entre 18 e 80 anos")
    dados_validos = False
    
if score < 0 or score > 1000:
    print("❌ Score deve estar entre 0 e 1000")
    dados_validos = False
    
if tempo_trabalho < 0:
    print("❌ Tempo de trabalho não pode ser negativo")
    dados_validos = False

if dados_validos:
    print(f"\n=== ANÁLISE DE CRÉDITO ===")
    print(f"Renda: R$ {renda:.2f}")
    print(f"Idade: {idade} anos")
    print(f"Score: {score}")
    print(f"Tempo trabalho: {tempo_trabalho} meses")
    
    # Sistema de aprovação com múltiplos critérios
    aprovado = False
    valor_maximo = 0
    taxa_juros = 0
    motivos_recusa = []
    
    # Critérios básicos
    renda_minima = renda >= 1500
    idade_ok = 21 <= idade <= 70
    score_minimo = score >= 300
    tempo_minimo = tempo_trabalho >= 6
    
    print(f"\n=== CRITÉRIOS BÁSICOS ===")
    print(f"Renda mínima (R$1500): {'✅' if renda_minima else '❌'}")
    print(f"Idade ideal (21-70): {'✅' if idade_ok else '❌'}")
    print(f"Score mínimo (300+): {'✅' if score_minimo else '❌'}")
    print(f"Tempo trabalho (6+ meses): {'✅' if tempo_minimo else '❌'}")
    
    # Lógica de aprovação
    if renda_minima and idade_ok and score_minimo and tempo_minimo:
        aprovado = True
        
        # Determinando valor e taxa baseados no perfil
        if score >= 800 and renda >= 5000:
            # Perfil premium
            valor_maximo = renda * 15
            taxa_juros = 1.5
            categoria = "PREMIUM"
        elif score >= 600 and renda >= 3000:
            # Perfil bom
            valor_maximo = renda * 10
            taxa_juros = 2.5
            categoria = "BOM"
        elif score >= 400:
            # Perfil regular
            valor_maximo = renda * 5
            taxa_juros = 4.0
            categoria = "REGULAR"
        else:
            # Perfil básico
            valor_maximo = renda * 3
            taxa_juros = 6.0
            categoria = "BÁSICO"
        
        # Ajustes por idade
        if idade > 60:
            valor_maximo *= 0.8  # Redução de 20%
            print("⚠️ Ajuste por idade: valor reduzido em 20%")
        
        # Ajustes por tempo de trabalho
        if tempo_trabalho >= 24:
            taxa_juros -= 0.5  # Bonus estabilidade
            print("✅ Bônus estabilidade: taxa reduzida em 0.5%")
    
    else:
        # Coletando motivos de recusa
        if not renda_minima:
            motivos_recusa.append("Renda insuficiente (mínimo R$ 1.500)")
        if not idade_ok:
            motivos_recusa.append("Idade fora da faixa aceita (21-70 anos)")
        if not score_minimo:
            motivos_recusa.append("Score muito baixo (mínimo 300)")
        if not tempo_minimo:
            motivos_recusa.append("Pouco tempo no emprego atual (mínimo 6 meses)")
    
    # Resultado final
    print(f"\n=== RESULTADO FINAL ===")
    if aprovado:
        print("🎉 EMPRÉSTIMO APROVADO!")
        print(f"📊 Categoria: {categoria}")
        print(f"💰 Valor máximo: R$ {valor_maximo:.2f}")
        print(f"📈 Taxa de juros: {taxa_juros:.1f}% ao mês")
        
        # Simulação de parcelas
        parcela_12x = (valor_maximo * (1 + taxa_juros/100 * 12)) / 12
        parcela_24x = (valor_maximo * (1 + taxa_juros/100 * 24)) / 24
        
        print(f"\n💳 Simulação (valor máximo):")
        print(f"12x: R$ {parcela_12x:.2f}")
        print(f"24x: R$ {parcela_24x:.2f}")
        
    else:
        print("❌ EMPRÉSTIMO NEGADO")
        print("📋 Motivos da recusa:")
        for i, motivo in enumerate(motivos_recusa, 1):
            print(f"   {i}. {motivo}")
        
        print(f"\n💡 RECOMENDAÇÕES:")
        if score < 600:
            print("- Melhore seu score pagando contas em dia")
        if renda < 3000:
            print("- Comprove renda adicional se possível")
        if tempo_trabalho < 12:
            print("- Aguarde mais tempo no emprego atual")

else:
    print("\n❌ Corrija os dados e tente novamente!")

print("\n💡 EXPLICAÇÃO:")
print("- Validação completa de entrada")
print("- Critérios múltiplos com condições compostas")
print("- if/elif para categorização de perfil")
print("- Cálculos condicionais baseados no perfil")
print("- Coleta de motivos de recusa para feedback")
print()

print("-" * 60)

# ======================================
# EXERCÍCIO 7 - JOGO PEDRA, PAPEL, TESOURA
# ======================================
print("7. JOGO PEDRA, PAPEL, TESOURA")
print("=" * 35)

import random

# Solução:
print("=== PEDRA, PAPEL, TESOURA ===")
print("Opções: pedra, papel, tesoura")

jogada_jogador = input("Sua jogada: ").lower().strip()

# Validação da entrada
opcoes_validas = ["pedra", "papel", "tesoura"]

if jogada_jogador not in opcoes_validas:
    print("❌ JOGADA INVÁLIDA!")
    print(f"Use apenas: {', '.join(opcoes_validas)}")
else:
    # Computador escolhe aleatoriamente
    jogada_computador = random.choice(opcoes_validas)
    
    print(f"\nVocê: {jogada_jogador}")
    print(f"Computador: {jogada_computador}")
    print()
    
    # Determinando o vencedor
    if jogada_jogador == jogada_computador:
        resultado = "EMPATE"
        print("🤝 EMPATE! Vocês escolheram a mesma opção!")
        
    elif (jogada_jogador == "pedra" and jogada_computador == "tesoura") or \
         (jogada_jogador == "papel" and jogada_computador == "pedra") or \
         (jogada_jogador == "tesoura" and jogada_computador == "papel"):
        resultado = "VITÓRIA"
        print("🎉 VOCÊ GANHOU!")
        
        # Explicação da vitória
        if jogada_jogador == "pedra":
            print("✊ Pedra quebra tesoura!")
        elif jogada_jogador == "papel":
            print("📄 Papel embrulha pedra!")
        else:  # tesoura
            print("✂️ Tesoura corta papel!")
            
    else:
        resultado = "DERROTA"
        print("😞 VOCÊ PERDEU!")
        
        # Explicação da derrota
        if jogada_computador == "pedra":
            print("✊ Pedra quebra tesoura!")
        elif jogada_computador == "papel":
            print("📄 Papel embrulha pedra!")
        else:  # tesoura
            print("✂️ Tesoura corta papel!")
    
    # Estatísticas do jogo
    print(f"\n📊 Resultado: {resultado}")
    
    # Versão alternativa mais compacta
    print("\n--- VERSÃO COMPACTA ---")
    vitorias = {
        ("pedra", "tesoura"): "Pedra quebra tesoura",
        ("papel", "pedra"): "Papel embrulha pedra", 
        ("tesoura", "papel"): "Tesoura corta papel"
    }
    
    if jogada_jogador == jogada_computador:
        print("Empate!")
    elif (jogada_jogador, jogada_computador) in vitorias:
        print(f"Você ganhou! {vitorias[(jogada_jogador, jogada_computador)]}")
    else:
        print(f"Você perdeu! {vitorias[(jogada_computador, jogada_jogador)]}")

print("\n💡 EXPLICAÇÃO:")
print("- Validação de entrada com lista de opções válidas")
print("- random.choice() para escolha do computador")
print("- Condições compostas com or para múltiplas vitórias")
print("- if/elif/else para 3 resultados possíveis")
print("- Dicionário como alternativa para regras do jogo")
print()

print("-" * 60)

# ======================================
# EXERCÍCIO 8 - ANALISADOR DE SENHA COMPLEXO
# ======================================
print("8. ANALISADOR DE SENHA COMPLEXO")
print("=" * 40)

# Solução:
print("=== ANALISADOR DE FORÇA DE SENHA ===")
senha = input("Digite sua senha: ")

# Análise dos critérios
comprimento_ok = len(senha) >= 8
tem_minuscula = any(c.islower() for c in senha)
tem_maiuscula = any(c.isupper() for c in senha)
tem_numero = any(c.isdigit() for c in senha)
tem_simbolo = any(not c.isalnum() for c in senha)

print(f"\n=== ANÁLISE DA SENHA ===")
print(f"Comprimento (≥8): {'✅' if comprimento_ok else '❌'} ({len(senha)} caracteres)")
print(f"Minúscula: {'✅' if tem_minuscula else '❌'}")
print(f"Maiúscula: {'✅' if tem_maiuscula else '❌'}")
print(f"Número: {'✅' if tem_numero else '❌'}")
print(f"Símbolo: {'✅' if tem_simbolo else '❌'}")

# Contando critérios atendidos
criterios_atendidos = sum([
    comprimento_ok, tem_minuscula, tem_maiuscula, 
    tem_numero, tem_simbolo
])

print(f"\nCritérios atendidos: {criterios_atendidos}/5")

# Classificação da força
if criterios_atendidos == 5:
    forca = "MUITO FORTE"
    cor = "🟢"
    feedback = "Excelente! Sua senha é muito segura."
elif criterios_atendidos >= 4:
    forca = "FORTE"
    cor = "🔵"
    feedback = "Boa senha! Considere adicionar os critérios faltantes."
elif criterios_atendidos >= 3:
    forca = "MÉDIA"
    cor = "🟡"
    feedback = "Senha razoável, mas pode melhorar."
elif criterios_atendidos >= 2:
    forca = "FRACA"
    cor = "🟠"
    feedback = "Senha vulnerável. Adicione mais critérios."
else:
    forca = "MUITO FRACA"
    cor = "🔴"
    feedback = "Senha muito insegura! Refaça completamente."

print(f"\n{cor} FORÇA DA SENHA: {forca}")
print(f"💬 {feedback}")

# Sugestões específicas usando condições aninhadas
print(f"\n=== SUGESTÕES DE MELHORIA ===")
sugestoes = []

if not comprimento_ok:
    sugestoes.append("• Use pelo menos 8 caracteres")
if not tem_minuscula:
    sugestoes.append("• Adicione letras minúsculas (a-z)")
if not tem_maiuscula:
    sugestoes.append("• Adicione letras maiúsculas (A-Z)")
if not tem_numero:
    sugestoes.append("• Adicione números (0-9)")
if not tem_simbolo:
    sugestoes.append("• Adicione símbolos (!@#$%&*)")

if sugestoes:
    for sugestao in sugestoes:
        print(sugestao)
else:
    print("✅ Sua senha atende todos os critérios!")

# Análises adicionais
print(f"\n=== ANÁLISES EXTRAS ===")

if len(senha) >= 12:
    print("🛡️ Comprimento excelente (12+ caracteres)")
elif len(senha) >= 10:
    print("👍 Bom comprimento (10+ caracteres)")

# Verificação de padrões comuns perigosos
padroes_perigosos = ["123", "abc", "password", "admin", "qwerty"]
senha_lower = senha.lower()

for padrao in padroes_perigosos:
    if padrao in senha_lower:
        print(f"⚠️ ATENÇÃO: Contém padrão comum '{padrao}'")
        break

# Verificação de repetição
if len(set(senha)) < len(senha) * 0.5:  # Muitos caracteres repetidos
    print("⚠️ ATENÇÃO: Muitos caracteres repetidos")

# Dica final baseada na força
if forca in ["MUITO FRACA", "FRACA"]:
    print(f"\n💡 DICA: Crie uma frase e use iniciais + números + símbolos")
    print("Exemplo: 'Eu Amo Python 2024!' → 'EaP2024!'")

print("\n💡 EXPLICAÇÃO:")
print("- any() verifica se pelo menos um caractere atende critério")
print("- sum() conta quantos critérios booleanos são True")  
print("- if/elif em sequência para classificar força")
print("- Loops para verificar padrões perigosos")
print("- set() para analisar diversidade de caracteres")
print()

print("-" * 60)

# ======================================
# DESAFIO EXTRA 🚀
# ======================================
print("DESAFIO EXTRA 🚀")
print("=" * 20)

# Solução:
print("=== QUIZ INTELIGENTE ===")
print("Responda às perguntas e veja como elas se conectam!\n")

# Pergunta 1: Nível básico
print("PERGUNTA 1: Qual linguagem você está aprendendo?")
print("a) Python  b) Java  c) C++  d) JavaScript")
resposta1 = input("Sua resposta: ").lower().strip()

if resposta1 == "a" or "python" in resposta1:
    print("🐍 Excelente escolha! Python é versátil e poderoso!\n")
    acertou_primeira = True
    
    # Pergunta 2: Baseada no acerto da primeira
    print("PERGUNTA 2: Qual estrutura de dados Python é ordenada e mutável?")
    print("a) tuple  b) list  c) set  d) dict")
    resposta2 = input("Sua resposta: ").lower().strip()
    
    if resposta2 == "b" or "list" in resposta2:
        print("🎯 Perfeito! Listas são fundamentais em Python!\n")
        
        # Pergunta 3: Nível avançado (só para quem acertou as 2)
        print("PERGUNTA 3: Qual método adiciona um item ao FINAL de uma lista?")
        print("a) add()  b) insert()  c) append()  d) extend()")
        resposta3 = input("Sua resposta: ").lower().strip()
        
        if resposta3 == "c" or "append" in resposta3:
            print("🏆 IMPRESSIONANTE! Você domina Python!")
            resultado_final = "EXPERT"
        else:
            print("📚 Quase lá! append() adiciona ao final da lista.")
            resultado_final = "INTERMEDIÁRIO"
    else:
        print("📖 Não exatamente. List é ordenada E mutável.\n")
        
        # Pergunta 3: Nível básico (para quem errou a segunda)
        print("PERGUNTA 3: Como você exibe texto na tela em Python?")
        print("a) echo  b) print  c) show  d) display")
        resposta3 = input("Sua resposta: ").lower().strip()
        
        if resposta3 == "b" or "print" in resposta3:
            print("✅ Correto! print() é fundamental em Python!")
            resultado_final = "INICIANTE"
        else:
            print("💡 É print()! Esta é a base de tudo em Python.")
            resultado_final = "PRECISA ESTUDAR"

else:
    print("🤔 Interessante! Mas hoje estamos focando em Python.\n")
    acertou_primeira = False
    
    # Pergunta 2: Motivacional para outras linguagens
    print("PERGUNTA 2: Por que Python é uma boa linguagem para aprender?")
    print("a) É muito rápida  b) Sintaxe simples  c) Só para web  d) É difícil")
    resposta2 = input("Sua resposta: ").lower().strip()
    
    if resposta2 == "b" or "simples" in resposta2:
        print("👍 Exato! Python prioriza legibilidade e simplicidade!\n")
        
        # Pergunta 3: Incentivo a experimentar Python
        print("PERGUNTA 3: Qual é o resultado de print('Hello, World!') ?")
        print("a) Erro  b) Nada  c) Hello, World!  d) Não sei")
        resposta3 = input("Sua resposta: ").lower().strip()
        
        if resposta3 == "c" or "hello" in resposta3:
            print("🎉 Perfeito! Você entende o básico de Python!")
            resultado_final = "CURIOSO"
        else:
            print("💻 Experimente! print() exibe texto na tela.")
            resultado_final = "EXPLORADOR"
    else:
        print("💡 Python é famoso pela sintaxe simples e legível!\n")
        resultado_final = "APRENDIZ"

# Resultado personalizado baseado no caminho
print("\n" + "="*50)
print("🎯 RESULTADO DO QUIZ INTELIGENTE")
print("="*50)

if acertou_primeira:
    if resultado_final == "EXPERT":
        print("🏆 NÍVEL: EXPERT EM PYTHON")
        print("🎓 Você domina conceitos avançados!")
        print("💼 Recomendação: Projetos complexos, frameworks")
        print("📚 Próximos passos: Machine Learning, Web Development")
    elif resultado_final == "INTERMEDIÁRIO":
        print("📈 NÍVEL: INTERMEDIÁRIO EM PYTHON") 
        print("💪 Você conhece os fundamentos!")
        print("💼 Recomendação: Projetos práticos, bibliotecas")
        print("📚 Próximos passos: Estruturas de dados avançadas")
    else:  # INICIANTE
        print("🌱 NÍVEL: INICIANTE EM PYTHON")
        print("✨ Você está no caminho certo!")
        print("💼 Recomendação: Pratique sintaxe básica")
        print("📚 Próximos passos: Loops, funções, listas")
else:
    if resultado_final == "CURIOSO":
        print("🔍 NÍVEL: CURIOSO SOBRE PYTHON")
        print("🌟 Você tem potencial!")
        print("💼 Recomendação: Experimente Python na prática")
        print("📚 Próximos passos: Tutorial básico, exercícios simples")
    else:
        print("🌱 NÍVEL: DESCOBRINDO PROGRAMAÇÃO")
        print("🎯 Todo expert já foi iniciante!")
        print("💼 Recomendação: Comece com conceitos básicos")
        print("📚 Próximos passos: Lógica de programação, Python básico")

print(f"\n🎮 Você seguiu o caminho: ", end="")
if acertou_primeira:
    print("Python → Listas → ", end="")
    if resultado_final == "EXPERT":
        print("Métodos avançados")
    else:
        print("Conceitos básicos")
else:
    print("Outras linguagens → Motivação Python → Experimentação")

print("\n💡 COMO O QUIZ FUNCIONOU:")
print("- Primeira pergunta determinou o 'nível' das próximas")
print("- Condições aninhadas criaram caminhos diferentes")
print("- Cada resposta influenciou as perguntas seguintes")
print("- Resultado personalizado baseado no percurso completo")

print("\n🚀 Isso é o poder das estruturas condicionais!")
print("Com if/elif/else você pode criar experiências interativas!")

print("\n" + "="*70)

# ======================================
# RESUMO FINAL DO GABARITO
# ======================================
print("\n🎯 CONCEITOS DOMINADOS NESTE ENCONTRO:")

print("\n🌳 ESTRUTURAS CONDICIONAIS:")
print("✅ if: executa bloco SE condição for True")
print("✅ elif: 'senão se' - condições mutuamente exclusivas")
print("✅ else: alternativa padrão se nenhuma condição for True")

print("\n📐 INDENTAÇÃO E BLOCOS:")
print("✅ 4 espaços (ou 1 tab) definem hierarquia")
print("✅ Blocos agrupam linhas de código relacionadas")
print("✅ Indentação é OBRIGATÓRIA em Python")

print("\n🔗 CONDIÇÕES COMPOSTAS:")
print("✅ and: TODAS as condições devem ser True")
print("✅ or: PELO MENOS UMA condição deve ser True")
print("✅ not: inverte o resultado booleano")

print("\n🛡️ VALIDAÇÃO E BOAS PRÁTICAS:")
print("✅ Validar entrada do usuário")
print("✅ Tratar casos de erro")
print("✅ Dar feedback específico")
print("✅ Usar condições aninhadas para lógica complexa")

print("\n⚡ PADRÕES IMPORTANTES:")
print("- Ordem do elif: mais específico primeiro")
print("- else opcional: só quando necessário")
print("- Condições mutuamente exclusivas com elif")
print("- Aninhamento para decisões em camadas")

print("\n🚀 PRÓXIMO PASSO:")
print("Encontro 5: Laços de repetição!")
print("Vamos usar essas condicionais dentro de loops!")

print("\n=== FIM DO GABARITO ===")