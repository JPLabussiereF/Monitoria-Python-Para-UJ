# Tutorial Completo GitHub - Sistemas de Informação

## 🌐 Link Principal
- **GitHub:** https://github.com

---

## 🎯 Slide 1: Primeiros Passos no GitHub

### 📝 Como Criar uma Conta no GitHub

#### Passo a Passo:
1. **Acesse** https://github.com
2. **Clique** em "Sign up" (canto superior direito)
3. **Preencha** os dados:
   - Username (nome de usuário único)
   - Email address (use email acadêmico se possível)
   - Password (senha forte)
4. **Resolva** o puzzle de verificação
5. **Clique** em "Create account"
6. **Verifique** seu email (link de confirmação)
7. **Escolha** o plano Free (gratuito)
8. **Responda** ao questionário inicial (opcional)
9. **Finalize** o cadastro

#### ✅ Dicas para Username:
- Use seu nome real ou uma variação profissional
- Evite números aleatórios ou caracteres especiais
- Exemplo bons: `joao-silva`, `maria-santos`, `pedro-dev`

### 🗂️ Como Criar um Repositório

#### Método 1 - Via Interface Web:
1. **Faça login** no GitHub
2. **Clique** no botão verde "+ New" ou "New repository"
3. **Preencha** as informações:
   - Repository name: nome do projeto
   - Description: breve descrição (opcional)
   - Public/Private: escolha a visibilidade
   - ✅ Initialize with README
   - Add .gitignore: escolha a linguagem/framework
   - Choose a license: MIT é uma boa opção
4. **Clique** em "Create repository"

#### Método 2 - Clonando Localmente:
```bash
# Depois de criar repo vazio no GitHub
git clone https://github.com/seuusername/nomerepositorio.git
cd nomerepositorio
echo "# Meu Projeto" >> README.md
git add README.md
git commit -m "Primeiro commit"
git push origin main
```

### 📄 Como Criar Seu README.md de Perfil

#### O que é o README de Perfil?
É um arquivo especial que aparece na **sua página principal do GitHub** como uma apresentação pessoal!

#### Como Criar:
1. **Crie um repositório** com o **mesmo nome do seu usuário**
   - Exemplo: se seu username é `joao-silva`, crie repo `joao-silva`
2. **Marque como público**
3. **✅ Initialize with README**
4. **Edite o README.md** - ele aparecerá no seu perfil!

#### 🎨 Template de README de Perfil:
```markdown
# Olá! Eu sou o João Silva 👋

## 👨‍💻 Sobre mim
- 🎓 Estudante de **Sistemas de Informação** na UNIJORGE
- 💻 Aprendendo **JavaScript, Python e React**
- 🌱 Focado em **Desenvolvimento Web**
- 📫 Como me encontrar: **joao.silva@email.com**
- ⚡ Curiosidade: **Adoro resolver problemas com código!**

## 🛠️ Tecnologias que estou aprendendo
![JavaScript](https://img.shields.io/badge/-JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)
![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white)
![React](https://img.shields.io/badge/-React-61DAFB?style=flat&logo=react&logoColor=black)
![HTML5](https://img.shields.io/badge/-HTML5-E34F26?style=flat&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/-CSS3-1572B6?style=flat&logo=css3&logoColor=white)

## 📊 GitHub Stats
![João's GitHub stats](https://github-readme-stats.vercel.app/api?username=joao-silva&show_icons=true&theme=radical)

## 📫 Vamos nos conectar!
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/joao-silva)
[![Email](https://img.shields.io/badge/-Email-D14836?style=flat&logo=gmail&logoColor=white)](mailto:joao.silva@email.com)
[![Portfolio](https://img.shields.io/badge/-Portfolio-000000?style=flat&logo=github&logoColor=white)](https://joao-silva.github.io)
```

#### 🚀 Templates Mais Avançados:

**Estilo Minimalista:**
```markdown
### Hi there 👋 I'm João

```
**Backend** Developer | **Computer Science** Student | **Problem Solver**
```

🔭 Currently working on: **Web APIs with Node.js**
🌱 Learning: **Cloud Computing & DevOps**
💬 Ask me about: **JavaScript, Python, Git**

---
📈 **2024 Goals:** Build 5 full-stack projects
```

**Estilo Dinâmico:**
```markdown
<h1 align="center">Oi 👋, Eu sou o João Silva</h1>
<h3 align="center">Estudante de SI apaixonado por tecnologia!</h3>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=joao-silva&color=blue" alt="Profile views" />
</p>

- 🔭 Trabalhando em **Sistema de Biblioteca**
- 🌱 Aprendendo **React e Node.js**
- 💬 Me pergunte sobre **JavaScript, Git, GitHub**
- 📫 Contato: **joao.silva@email.com**
- ⚡ Fato curioso: **Comecei a programar aos 17 anos**

<h3 align="center">Linguagens e Ferramentas:</h3>
<p align="center">
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="40" height="40"/>
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/>
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/react/react-original.svg" alt="react" width="40" height="40"/>
</p>

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api/top-langs?username=joao-silva&show_icons=true&locale=en&layout=compact&theme=radical" alt="Top Languages" />
</p>
```

#### 🎯 Recursos Especiais para README de Perfil:

**GitHub Stats:**
```markdown
![Stats](https://github-readme-stats.vercel.app/api?username=SEUUSERNAME&show_icons=true&theme=radical)
![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=SEUUSERNAME&layout=compact&theme=radical)
```

**Contador de Visitas:**
```markdown
![Profile Views](https://komarev.com/ghpvc/?username=SEUUSERNAME&color=blue)
```

**Activity Graph:**
```markdown
![Activity Graph](https://github-readme-activity-graph.vercel.app/graph?username=SEUUSERNAME&theme=react-dark)
```

---

## 🤝 Slide 2: Colaboração no GitHub

### 🔀 Como Fazer um Pull Request

#### Cenário: Contribuindo para um projeto existente

#### Passo a Passo Completo:

1. **Fork do Repositório:**
   - Vá ao repositório que quer contribuir
   - Clique em "Fork" (canto superior direito)
   - Aguarde a criação da cópia na sua conta

2. **Clone Seu Fork:**
```bash
git clone https://github.com/SEUUSERNAME/nome-do-projeto.git
cd nome-do-projeto
```

3. **Configure o Upstream:**
```bash
git remote add upstream https://github.com/USUARIO-ORIGINAL/nome-do-projeto.git
git remote -v  # Verifica se foi adicionado
```

4. **Crie uma Branch para Sua Feature:**
```bash
git checkout -b minha-nova-feature
```

5. **Faça Suas Alterações:**
   - Edite os arquivos necessários
   - Teste suas modificações
   - Siga as convenções do projeto

6. **Commit e Push:**
```bash
git add .
git commit -m "feat: adiciona nova funcionalidade X"
git push origin minha-nova-feature
```

7. **Abra o Pull Request:**
   - Vá ao seu fork no GitHub
   - Clique em "Compare & pull request"
   - Preencha título e descrição detalhada
   - Clique em "Create pull request"

#### 📝 Template de Pull Request:
```markdown
## 🎯 Objetivo
Descreve brevemente o que foi implementado/corrigido.

## 🔧 Alterações
- [x] Adiciona função de login
- [x] Corrige bug na validação de email
- [x] Atualiza documentação

## 🧪 Como Testar
1. Clone a branch: `git checkout minha-nova-feature`
2. Execute: `npm install && npm start`
3. Acesse: http://localhost:3000
4. Teste a nova funcionalidade

## 📸 Screenshots
![Antes](./before.png) ![Depois](./after.png)

## 📋 Checklist
- [x] Código testado
- [x] Documentação atualizada
- [x] Segue padrões do projeto
```

### 🔄 Workflow Colaborativo Completo

#### Para Manter Seu Fork Atualizado:
```bash
# Busca atualizações do repositório original
git fetch upstream

# Muda para branch main
git checkout main

# Faz merge das atualizações
git merge upstream/main

# Atualiza seu fork no GitHub
git push origin main
```

#### Resolvendo Conflitos:
1. **Quando há conflitos:**
```bash
git pull upstream main  # Puxa últimas alterações
# Git mostrará os conflitos
```

2. **Edite os arquivos** com conflito (procure por `<<<<<<< HEAD`)
3. **Remova** as marcações de conflito
4. **Teste** se tudo funciona
5. **Commit** a resolução:
```bash
git add .
git commit -m "resolve: conflitos de merge"
git push origin minha-nova-feature
```

### 🏷️ Boas Práticas para Pull Requests

#### ✅ Faça:
- Título claro e descritivo
- Descrição detalhada das mudanças
- Teste suas alterações antes de enviar
- Mantenha commits pequenos e focados
- Siga as convenções do projeto
- Responda aos comentários dos revisores

#### ❌ Evite:
- PRs muito grandes (muitas alterações juntas)
- Commits com mensagens genéricas ("fix", "update")
- Alterar arquivos não relacionados à feature
- Ignorar feedback dos revisores
- Fazer push na branch main diretamente

---

## 🎨 Recursos Extras do GitHub

### Issues (Problemas)
```markdown
## 🐛 Bug Report
**Descrição:** O botão de login não funciona no mobile

**Passos para reproduzir:**
1. Acesse pelo celular
2. Clique em "Entrar"
3. Nada acontece

**Comportamento esperado:** Deveria abrir modal de login

**Screenshots:** [anexar imagem]

**Ambiente:**
- Device: iPhone 12
- Browser: Safari
- Versão: iOS 15.0
```

### Releases e Tags
```bash
# Criar tag localmente
git tag -a v1.0.0 -m "Primeira versão estável"

# Enviar tag para GitHub
git push origin v1.0.0
```

### GitHub Pages (Hospedar Site Grátis)
1. Vá em **Settings** do repositório
2. Scroll até **Pages**
3. Escolha source: **Deploy from a branch**
4. Select branch: **main** 
5. Seu site ficará em: `https://seuusername.github.io/nomerepositorio`

---

### Comandos Git + GitHub Essenciais:
```bash
# Configurar credenciais (uma vez só)
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"

# Workflow padrão
git add .
git commit -m "feat: adiciona nova funcionalidade"
git push origin main

# Sincronizar com repositório remoto
git pull origin main
```

---

*Material preparado para monitoria de Sistemas de Informação - 1º Semestre*
*GitHub: Plataforma essencial para todo desenvolvedor! 🚀*