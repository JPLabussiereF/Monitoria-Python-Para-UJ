# TAREFA DE CASA - ENCONTRO 4
# "Sistema de Classificação de Filmes"

"""
ENUNCIADO:
Crie um sistema completo de classificação de filmes que:

1. COLETA INFORMAÇÕES:
   - Nome do filme
   - Gênero (ação, comédia, drama, terror, ficção)
   - Nota do usuário (0-10)
   - Idade do usuário
   - É assinante premium? (sim/não)

2. VALIDAÇÕES COM CONDICIONAIS:
   - Nota deve estar entre 0-10
   - Idade deve ser positiva
   - Gênero deve ser válido

3. SISTEMA DE RECOMENDAÇÃO (if/elif/else):
   - Terror: só para idade >= 16
   - Ação: recomendado para >= 13
   - Drama: qualquer idade
   - Comédia: >= 14 para alguns tipos
   - Ficção: >= 12

4. CLASSIFICAÇÃO DA AVALIAÇÃO:
   - 9-10: Obra-prima
   - 7-8.9: Muito bom
   - 5-6.9: Regular  
   - 3-4.9: Ruim
   - 0-2.9: Péssimo

5. BENEFÍCIOS DE ASSINANTE PREMIUM:
   - Acesso antecipado (qualquer nota)
   - Desconto em ingressos (nota >= 7)
   - Conteúdo exclusivo (nota >= 8)

Tempo estimado: 20-25 minutos

EXEMPLO DE SAÍDA ESPERADA:
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
"""

# ==========================================
# ESCREVA SEU CÓDIGO AQUI:
# ==========================================

print("=== SISTEMA DE CLASSIFICAÇÃO DE FILMES ===")

# 1. Coleta de informações


# 2. Validações com condicionais


# 3. Sistema de recomendação por idade


# 4. Classificação da avaliação


# 5. Benefícios premium


# 6. Decisão final e relatório


# ==========================================
# GABARITO (não olhe antes de tentar!)
# ==========================================

"""
# GABARITO DA TAREFA DE CASA - ENCONTRO 4

print("=== SISTEMA DE CLASSIFICAÇÃO DE FILMES ===")

# 1. Coleta de informações
nome_filme = input("Nome do filme: ").strip()
genero = input("Gênero (ação/comédia/drama/terror/ficção): ").lower().strip()
nota = float(input("Sua nota para o filme (0-10): "))
idade = int(input("Sua idade: "))
eh_premium = input("É assinante premium? (sim/não): ").lower().strip() == "sim"

# 2. Validações com condicionais
print("\\n=== VALIDAÇÃO DOS DADOS ===")
dados_validos = True

# Validação da nota
if nota < 0 or nota > 10:
    print("❌ Nota inválida! Deve estar entre 0 e 10.")
    dados_validos = False
else:
    print(f"✅ Nota válida: {nota}")

# Validação da idade
if idade <= 0:
    print("❌ Idade inválida! Deve ser positiva.")
    dados_validos = False
else:
    print(f"✅ Idade válida: {idade}")

# Validação do gênero
generos_validos = ["ação", "comédia", "drama", "terror", "ficção"]
if genero not in generos_validos:
    print(f"❌ Gênero inválido! Use: {', '.join(generos_validos)}")
    dados_validos = False
else:
    print(f"✅ Gênero válido: {genero}")

# Validação do nome
if nome_filme == "":
    print("❌ Nome do filme não pode estar vazio!")
    dados_validos = False
else:
    print(f"✅ Filme: {nome_filme}")

if dados_validos:
    print("\\n" + "="*50)
    print("         ANÁLISE COMPLETA DO FILME")
    print("="*50)
    print(f"🎬 Filme: {nome_filme}")
    print(f"🎭 Gênero: {genero.title()}")
    print(f"⭐ Nota: {nota}")
    print(f"👤 Idade: {idade}")
    print(f"💎 Premium: {'Sim' if eh_premium else 'Não'}")
    
    # 3. Sistema de recomendação por idade usando if/elif/else
    print("\\n=== ADEQUAÇÃO POR IDADE ===")
    adequado_idade = False
    
    if genero == "terror":
        if idade >= 16:
            print("✅ Terror liberado para sua idade (16+)")
            adequado_idade = True
        else:
            anos_faltam = 16 - idade
            print(f"❌ Terror não recomendado. Aguarde {anos_faltam} ano(s)")
            
    elif genero == "ação":
        if idade >= 13:
            print("✅ Ação recomendado para sua idade (13+)")
            adequado_idade = True
        else:
            anos_faltam = 13 - idade
            print(f"⚠️ Ação com restrições. Recomendado aguardar {anos_faltam} ano(s)")
            adequado_idade = True  # Permite mas com aviso
            
    elif genero == "comédia":
        if idade >= 14:
            print("✅ Comédia totalmente liberada (14+)")
            adequado_idade = True
        elif idade >= 10:
            print("⚠️ Comédia com supervisão recomendada")
            adequado_idade = True
        else:
            print("❌ Comédia não recomendada para sua idade")
            
    elif genero == "ficção":
        if idade >= 12:
            print("✅ Ficção científica liberada (12+)")
            adequado_idade = True
        else:
            anos_faltam = 12 - idade
            print(f"⚠️ Ficção pode ser complexa. Aguarde {anos_faltam} ano(s)")
            adequado_idade = True  # Permite com aviso
            
    else:  # drama
        print("✅ Drama adequado para qualquer idade")
        adequado_idade = True
    
    # 4. Classificação da avaliação usando if/elif/else
    print("\\n=== CLASSIFICAÇÃO DA AVALIAÇÃO ===")
    if nota >= 9.0:
        categoria = "OBRA-PRIMA"
        emoji = "🏆"
        comentario = "Um filme excepcional que marcará época!"
    elif nota >= 7.0:
        categoria = "MUITO BOM"
        emoji = "🌟"
        comentario = "Excelente escolha, vale muito a pena!"
    elif nota >= 5.0:
        categoria = "REGULAR"
        emoji = "👍"
        comentario = "Um filme decente para passar o tempo"
    elif nota >= 3.0:
        categoria = "RUIM"
        emoji = "👎"
        comentario = "Não é uma boa opção, considere outros filmes"
    else:
        categoria = "PÉSSIMO"
        emoji = "💩"
        comentario = "Definitivamente não recomendado"
    
    print(f"{emoji} Categoria: {categoria}")
    print(f"💬 {comentario}")
    
    # 5. Benefícios de assinante premium usando condições aninhadas
    print("\\n=== ANÁLISE DE BENEFÍCIOS ===")
    
    if eh_premium:
        print("💎 STATUS: ASSINANTE PREMIUM")
        
        # Acesso antecipado - sempre disponível para premium
        print("✅ Acesso antecipado: LIBERADO")
        
        # Desconto em ingressos - nota >= 7
        if nota >= 7.0:
            desconto = 20
            print(f"🎟️ Desconto em ingressos: {desconto}% (filme bem avaliado)")
        else:
            desconto = 10
            print(f"🎟️ Desconto em ingressos: {desconto}% (desconto básico premium)")
        
        # Conteúdo exclusivo - nota >= 8
        if nota >= 8.0:
            print("🎁 Conteúdo exclusivo: LIBERADO (making-of, cenas extras)")
        else:
            print("❌ Conteúdo exclusivo: Indisponível (nota precisa ser >= 8.0)")
            
        # Benefício extra baseado no gênero
        if genero in ["ficção", "ação"]:
            print("🚀 Bônus premium: Trailers exclusivos de sequências!")
            
    else:
        print("👤 STATUS: USUÁRIO COMUM")
        print("❌ Acesso antecipado: Não disponível")
        print("❌ Desconto em ingressos: Não disponível")  
        print("❌ Conteúdo exclusivo: Não disponível")
        print("💡 Dica: Assine premium para ter acesso a benefícios exclusivos!")
        
    # 6. Decisão final e recomendação usando múltiplas condições
    print("\\n=== DECISÃO FINAL ===")
    
    # Critérios para recomendar o filme
    nota_boa = nota >= 6.0
    idade_ok = adequado_idade
    
    if idade_ok and nota_boa:
        if eh_premium or nota >= 7.0:
            recomendacao = "ALTAMENTE RECOMENDADO"
            emoji_final = "🍿"
            acao = "Deseja assistir? Acesso liberado!"
        else:
            recomendacao = "RECOMENDADO"  
            emoji_final = "👍"
            acao = "Boa escolha para assistir!"
    elif idade_ok and not nota_boa:
        recomendacao = "COM RESSALVAS"
        emoji_final = "⚠️"
        acao = "Pode assistir, mas talvez não seja a melhor opção"
    elif not idade_ok and nota_boa:
        recomendacao = "AGUARDAR IDADE ADEQUADA"
        emoji_final = "⏳"
        acao = "Filme bom, mas aguarde a idade recomendada"
    else:
        recomendacao = "NÃO RECOMENDADO"
        emoji_final = "❌"
        acao = "Considere outras opções de filme"
    
    print(f"{emoji_final} RECOMENDAÇÃO: {recomendacao}")
    print(f"🎯 {acao}")
    
    # Relatório de pontuação
    pontuacao_total = 0
    if adequado_idade:
        pontuacao_total += 30
    if nota >= 7.0:
        pontuacao_total += 40  
    elif nota >= 5.0:
        pontuacao_total += 20
    if eh_premium:
        pontuacao_total += 30
        
    print(f"\\n📊 Pontuação geral: {pontuacao_total}/100")
    
    if pontuacao_total >= 80:
        print("🏆 Combinação perfeita!")
    elif pontuacao_total >= 60:
        print("🌟 Boa combinação!")
    elif pontuacao_total >= 40:
        print("👍 Combinação razoável")
    else:
        print("👎 Talvez não seja ideal")
        
else:
    print("\\n❌ Corrija os dados inválidos e tente novamente!")

print("\\n" + "="*50)
print("🎬 SISTEMA DE FILMES FINALIZADO!")
print("Obrigado por usar nosso serviço!")
print("="*50)

# OBSERVAÇÕES DO GABARITO:
# 1. Validação completa de todos os dados de entrada
# 2. Uso de if/elif/else para classificações múltiplas
# 3. Condições aninhadas para lógica complexa
# 4. Condições compostas (and/or) para decisões finais
# 5. Sistema de pontuação baseado em múltiplos critérios
# 6. Mensagens personalizadas para cada situação
# 7. Estrutura organizada em seções claras
# 8. Tratamento de casos especiais e edge cases

# CONCEITOS APLICADOS:
# ✅ if/elif/else para classificação
# ✅ Condições aninhadas para lógica em camadas
# ✅ Validação robusta de entrada
# ✅ Condições compostas com and/or
# ✅ Personalização baseada em múltiplos fatores
# ✅ Sistema de pontuação e relatórios
"""

print("\\n💡 DICAS PARA DESENVOLVER:")
print("- Use if/elif/else para classificações mutuamente exclusivas")
print("- Valide TODOS os dados de entrada")
print("- Organize código em seções lógicas")  
print("- Use condições aninhadas para decisões complexas")
print("- Dê feedback específico para cada situação")

print("\\n🚀 DESAFIOS EXTRAS:")
print("1. Adicione mais gêneros de filme")
print("2. Crie sistema de recomendação baseado em filmes similares")
print("3. Implemente histórico de avaliações")
print("4. Adicione sistema de favoritos")
print("5. Crie interface com menu de opções")

print("\\n⚡ CRITÉRIOS DE AVALIAÇÃO:")
print("✅ Coleta e valida todas as informações")
print("✅ Usa if/elif/else adequadamente")
print("✅ Implementa condições aninhadas")
print("✅ Aplica lógica de classificação por idade")
print("✅ Sistema de benefícios premium funcional")
print("✅ Decisão final baseada em múltiplos critérios")
print("✅ Código bem organizado e comentado")