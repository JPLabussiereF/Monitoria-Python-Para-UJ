# Guia Completo do Git - Sistemas de Informação

## 📥 Links para Download

- **Site Oficial do Git:** https://git-scm.com/
- **Download direto para Windows:** https://git-scm.com/download/win
- **Download direto para macOS:** https://git-scm.com/download/mac
- **Download direto para Linux:** https://git-scm.com/download/linux

---

## 🛠️ Slide 1: Instalação do Git Passo a Passo

### Windows
1. **Acesse** o site oficial: https://git-scm.com/
2. **Clique** em "Download for Windows"
3. **Execute** o arquivo baixado (.exe)
4. **Siga o assistente de instalação:**
   - Aceite a licença
   - Escolha o local de instalação (padrão recomendado)
   - Selecione componentes (deixe as opções padrão)
   - Escolha "Use Git from the Windows Command Prompt"
   - Configure line endings como "Checkout Windows-style, commit Unix-style"
   - Use MinTTY como terminal emulator
5. **Finalize** a instalação
6. **Verifique** abrindo o CMD/PowerShell e digite: `git --version`

### macOS
1. **Opção 1 - Site oficial:**
   - Baixe de https://git-scm.com/download/mac
   - Execute o .dmg e siga as instruções
2. **Opção 2 - Homebrew (recomendado):**
   - Instale Homebrew: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
   - Execute: `brew install git`
3. **Verifique** no Terminal: `git --version`

### Linux (Ubuntu/Debian)
1. **Abra** o terminal
2. **Atualize** os repositórios: `sudo apt update`
3. **Instale** o Git: `sudo apt install git`
4. **Verifique** a instalação: `git --version`

### Configuração Inicial (Todos os sistemas)
```bash
git config --global user.name "Seu Nome"
git config --global user.email "seuemail@exemplo.com"
```

---

## ⚡ Slide 2: Principais Comandos do Git

### Configuração
```bash
git config --global user.name "Seu Nome"        # Define nome do usuário
git config --global user.email "seu@email.com"  # Define email do usuário
git config --list                                # Lista todas configurações
```

### Iniciando um Repositório
```bash
git init                    # Inicializa repositório na pasta atual
git clone <url>            # Clona repositório remoto
```

### Comandos Básicos do Dia a Dia
```bash
git status                 # Mostra status dos arquivos
git add <arquivo>          # Adiciona arquivo específico ao stage
git add .                  # Adiciona todos os arquivos ao stage
git commit -m "mensagem"   # Cria commit com mensagem
git commit -am "mensagem"  # Add + commit em arquivos já rastreados
```

### Visualização e Histórico
```bash
git log                    # Mostra histórico de commits
git log --oneline          # Histórico resumido (uma linha por commit)
git diff                   # Mostra diferenças não commitadas
git show <hash>            # Mostra detalhes de um commit específico
```

### Branches (Ramificações)
```bash
git branch                 # Lista branches locais
git branch <nome>          # Cria nova branch
git checkout <branch>      # Muda para uma branch
git checkout -b <branch>   # Cria e muda para nova branch
git merge <branch>         # Faz merge de uma branch na atual
git branch -d <branch>     # Deleta branch local
```

### Repositório Remoto
```bash
git remote add origin <url>    # Adiciona repositório remoto
git push origin <branch>       # Envia commits para repositório remoto
git pull origin <branch>       # Puxa alterações do repositório remoto
git push -u origin main        # Primeira push (define upstream)
git remote -v                  # Lista repositórios remotos
```

### Comandos de "Emergência"
```bash
git reset --hard HEAD~1        # Desfaz último commit (CUIDADO!)
git revert <hash>             # Cria commit que desfaz outro commit
git stash                     # Salva alterações temporariamente
git stash pop                 # Recupera alterações do stash
```

---

## 🎯 Fluxo Básico Recomendado

1. **Clone ou Init:** `git clone <url>` ou `git init`
2. **Trabalhe** nos seus arquivos
3. **Verifique status:** `git status`
4. **Adicione ao stage:** `git add .`
5. **Faça commit:** `git commit -m "Descrição das mudanças"`
6. **Envie para remoto:** `git push origin main`

---

## 📚 Dicas Importantes

- **Sempre** verifique o status antes de fazer commits
- **Escreva** mensagens de commit claras e descritivas
- **Faça** commits pequenos e frequentes
- **Use** branches para features diferentes
- **Nunca** commite arquivos sensíveis (senhas, keys, etc.)
- **Configure** o .gitignore para ignorar arquivos desnecessários

---

## 🆘 Em Caso de Problemas

- **Esqueci de configurar nome/email:** Execute os comandos de configuração global
- **Erro ao fazer push:** Verifique se fez pull das últimas alterações
- **Merge conflict:** Edite o arquivo, resolva os conflitos e faça commit
- **Commitei algo errado:** Use `git revert` em vez de `git reset` se já fez push

---

*Material preparado para monitoria de Sistemas de Informação - 1º Semestre*